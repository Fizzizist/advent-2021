import sys

def main():
    with open(sys.argv[1]) as f:
        first = True
        meas = 0
        count = 0
        for line in f.readlines():
            print(int(line))
            if first:
                meas = int(line)
                first = False
            else:
                if int(line) > meas:
                    count += 1
                meas = int(line)
    print(count)

main()
