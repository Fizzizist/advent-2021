import sys

def main():
    zero_list = [0 for _ in range(12)]
    ones_list = [0 for _ in range(12)]
    with open(sys.argv[1]) as f:
        for line in f.readlines():
            for i, digit in enumerate(line.strip()):
                if digit == '1':
                    ones_list[i] += 1
                else:
                    zero_list[i] += 1
    
    gamma = ['1' if ones_list[i] > zero_list[i] else '0' for i in range(12)]
    eps = ['0' if item == '1' else '1' for item in gamma]
    gamma = int(''.join(gamma), 2)
    eps = int(''.join(eps), 2)
    
    print(gamma)
    print(eps)
    print(gamma * eps)

main()
