import sys

def main():
    with open(sys.argv[1]) as f:
        measurements = [int(line) for line in f.readlines()]
    
    first = True
    meas = 0
    count = 0
    for i in range(3, len(measurements) + 1):
        j = i - 3
        if first:
            meas = sum(measurements[j:i])
            print(measurements[j:i])
            first = False
        else:
            print(meas)
            print(sum(measurements[j:i]))
            print(measurements[j:i])
            if sum(measurements[j:i]) > meas:
                count += 1
            meas = sum(measurements[j:i])

    print(count)

main()
