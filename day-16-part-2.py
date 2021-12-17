import sys


class Packet:

    def __init__(self, parent, hex_str, bin_str):
        # unless the length is limited, we set this to a huge number
        self.children = []
        self.parent = parent
        if bin_str is None:
            bin_str = ''
            for c in hex_str:
                bin_str += format(int(c, 16), '04b')
        self._parse_bit_str(bin_str)

    def _assign_literal(self, binary):
        end = False
        bin_num = ''
        while not end:
            if binary[0] == '0':
                end = True
            bin_num += binary[1:5]
            binary = binary[5:]
        self.literal = int(bin_num, 2)
        if binary != '' and int(binary, 2) != 0:
            self.parent.pass_back(binary)

    def _assign_op(self, binary):
        self.length_type_id = int(binary[0])
        if self.length_type_id == 0:
            bit_len = int(binary[1:16], 2)
            binary = binary[16:]
            self.children.append(Packet(self, None, binary[:bit_len]))
            if binary[bit_len:] != '' and int(binary[bit_len:], 2) != 0:
                self.parent.pass_back(binary[bit_len:])

        elif self.length_type_id == 1:
            self.num_subs = int(binary[1:12], 2)
            binary = binary[12:]
            self.num_children = 1
            self.children.append(Packet(self, None, binary))

    def _parse_bit_str(self, binary):
        self.version = int(binary[:3], 2)
        self.type_id = int(binary[3:6], 2)

        if self.type_id == 4:
            self._assign_literal(binary[6:])
        else:
            self._assign_op(binary[6:])

    def pass_back(self, binary):
        """callback function from child packet"""
        if self.length_type_id == 0:
            self.children.append(Packet(self, None, binary))
        elif self.length_type_id == 1:
            if self.num_subs > self.num_children:
                self.num_children += 1
                self.children.append(Packet(self, None, binary))
            else:
                self.parent.pass_back(binary)

    def get_packet_value(self):
        if self.type_id == 4:
            return self.literal
        elif self.type_id == 0:
            return sum([child.get_packet_value() for child in self.children])
        elif self.type_id == 1:
            prod = self.children[0].get_packet_value()
            if len(self.children) > 1:
                for child in self.children[1:]:
                    prod *= child.get_packet_value()
            return prod
        elif self.type_id == 2:
            return min([child.get_packet_value() for child in self.children])
        elif self.type_id == 3:
            return max([child.get_packet_value() for child in self.children])
        elif self.type_id == 5:
            vals = [child.get_packet_value() for child in self.children]
            return 1 if vals[1] > vals[0] else 0
        elif self.type_id == 6:
            vals = [child.get_packet_value() for child in self.children]
            return 1 if vals[1] < vals[0] else 0
        elif self.type_id == 7:
            vals = [child.get_packet_value() for child in self.children]
            return 1 if vals[0] == vals[1] else 0

    def print_packet(self):
        if self.type_id == 4:
            print(f'Literal {self.literal}')
        else:
            print(f'PACKET v{self.version} type:{self.type_id} '
                  f'length type:{self.length_type_id} '
                  f'# of children: {len(self.children)}')
            if self.length_type_id == 1:
                print(f'Num Subs: {self.num_subs}')
            print('Children:')
            print('\n')
            for child in self.children:
                child.print_packet()
            print('\n')


def main():
    with open(sys.argv[1]) as f:
        hex_str = f.read().strip()

    main_packet = Packet(None, hex_str, None)
    print(main_packet.get_packet_value())


main()
