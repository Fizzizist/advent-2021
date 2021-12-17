import sys


class Packet:

    def __init__(self, parent, hex_str, bin_str):
        # unless the length is limited, we set this to a huge number
        self.max_len = 999_999
        self.children = []
        self.parent = parent
        if bin_str is None:
            bin_str = ''
            for c in hex_str:
                bin_str += format(int(c, 16), '04b')
        self._parse_bit_str(bin_str)

    def _give_parent_children(self, bin_str):
        if bin_str == '':
            return

        if int(bin_str, 2) != 0:
            if self.parent.max_len > len(self.parent.children):
                self.parent.children.append(
                    Packet(self.parent, None, bin_str)
                )
            else:
                self.parent.parent.children.append(
                    Packet(self.parent.parent, None, bin_str)
                )

    def _assign_literal(self, bin_str):
        end = False
        bin_num = ''
        while not end:
            if bin_str[0] == '0':
                end = True
            bin_num += bin_str[1:5]
            bin_str = bin_str[5:]
        self.literal = int(bin_num, 2)
        self._give_parent_children(bin_str)

    def _assign_op(self, bin_str):
        if bin_str[0] == '0':
            # next 15 bits are total length of op bits
            bit_len = int(bin_str[1:16], 2)
            bin_str = bin_str[16:]
            if bin_str[:bit_len] != '':
                self.children.append(
                    Packet(self, None, bin_str[:bit_len])
                )
            self._give_parent_children(bin_str[bit_len:])

        elif bin_str[0] == '1':
            # next 11 bits are number of subpackets
            num_subs = int(bin_str[1:12], 2)
            bin_str = bin_str[12:]
            self.max_len = num_subs
            if bin_str != '':
                self.children.append(Packet(self, None, bin_str))

    def _parse_bit_str(self, binary):
        self.version = int(binary[:3], 2)
        self.type_id = int(binary[3:6], 2)

        # literal value
        if self.type_id == 4:
            self._assign_literal(binary[6:])
        else:
            self._assign_op(binary[6:])

    def get_version_sum(self):
        if len(self.children) > 0:
            return self.version + sum([child.get_version_sum()
                                       for child in self.children])
        else:
            return self.version


def main():
    with open(sys.argv[1]) as f:
        hex_str = f.read().strip()

    main_packet = Packet(None, hex_str, None)
    print(main_packet.get_version_sum())


main()
