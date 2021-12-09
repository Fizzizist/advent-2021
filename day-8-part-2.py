import sys

class SevenSeg():

    def __init__(self, inputs_str):
        self.inputs = inputs_str.split(' ')
        # replicating behavior that is necessary later
        self.inputs = [''.join(sorted(item)) for item in self.inputs]
        self.combo_map = dict()
        self._determine_numbers()

    def _determine_numbers(self):
        known_count_map = {2: 1, 4: 4, 3:7, 7:8}

        self.combo_map = {item: known_count_map[len(item)]
                          for item in self.inputs
                          if len(item) in known_count_map}

        unknown = [set(item) for item in self.inputs
                   if item not in self.combo_map]

        opp_combo_map = {value: set(key)
                         for key, value in self.combo_map.items()}

        for combo in unknown:
            if len(combo) == 5 and opp_combo_map[7].issubset(combo):
                    self.combo_map[''.join(sorted(combo))] = 3
            # case of 6 letters
            elif len(combo) == 6:
                if opp_combo_map[4].issubset(combo):
                    self.combo_map[''.join(sorted(combo))] = 9
                elif opp_combo_map[7].issubset(combo):
                    self.combo_map[''.join(sorted(combo))] = 0
                elif not opp_combo_map[7].issubset(combo):
                    self.combo_map[''.join(sorted(combo))] = 6
                    opp_combo_map[6] = combo

        # assign 2 and 5 with 6
        unknown = [set(item) for item in self.inputs
                   if item not in self.combo_map]

        # ensure the rest were assigned already
        for combo in unknown:
            if combo.issubset(opp_combo_map[6]):
                self.combo_map[''.join(sorted(combo))] = 5
            else:
                self.combo_map[''.join(sorted(combo))] = 2


def main():
    outputs = []
    inputs = []
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            _input, _output = line.strip().split(' | ')
            outputs.append(_output.split(' '))
            inputs.append(SevenSeg(_input))

    count = 0
    for i in range(len(outputs)):
        combo_map = inputs[i].combo_map
        num = ''.join([str(combo_map[''.join(sorted(j))])
                           for j in outputs[i]])
        count += int(num)

    print(count)


main()
