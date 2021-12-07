import sys

def get_fuel_cons(target, positions):
    fuel = 0
    for pos in positions:
        if pos > target:
            fuel += pos - target
        else:
            fuel += target - pos
    return fuel


def main():
    with open(sys.argv[1]) as f:
        positions = [int(num) for num in f.readline().strip().split(',')]
    min_pos = min(positions)
    max_pos = max(positions)
    for i in range(min_pos, max_pos + 1):
        fuel1 = get_fuel_cons(i, positions)
        fuel2 = get_fuel_cons(i+1, positions)
        #print(fuel1)
        #print(fuel2)
        #print('\n')
        if fuel1 < fuel2:
            print(fuel1)
            return


main()
