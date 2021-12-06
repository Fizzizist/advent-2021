import sys
from tqdm import tqdm

# Works for both part1 and part2. Takes in number of generations from second
#  command line argument.
def main():
    fish_ages = [0,0,0,0,0,0,0,0,0]
    with open(sys.argv[1]) as f:
        for num in f.readline().split(','):
            fish_ages[int(num)] += 1


    for _ in tqdm(range(int(sys.argv[2]))):
        babies = fish_ages[0]
        for i in range(8):
            fish_ages[i] = fish_ages[i+1]
        fish_ages[8] = babies
        fish_ages[6] += babies

    print(sum(fish_ages))

main()
