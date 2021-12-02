import sys

def main():
    with open(sys.argv[1]) as f:
        instructions = [item.split(' ') for item in f.readlines()]
    instructions = [(instr, int(val)) for instr, val in instructions]
    horiz = 0
    depth = 0
    for inst, val in instructions:
        if inst == 'forward':
            horiz += val
        elif inst == 'down':
            depth += val
        elif inst == 'up':
            depth -= val

    print(horiz * depth)

main()
