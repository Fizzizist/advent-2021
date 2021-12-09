import sys

def main():
    outputs = []
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            _output = line.strip().split(' | ')[1]
            outputs.extend(_output.split(' '))

    # counts for 1, 4, 7, and 8
    letter_counts = {2, 4, 3, 7}

    print(outputs)

    print(len([item for item in outputs if len(item) in letter_counts]))


main()
