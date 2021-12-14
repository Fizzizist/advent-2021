import sys
from collections import defaultdict
from tqdm import tqdm

# works for both part 1 and part 2. Number of steps is input as second command
#  line argument

def main():
    with open(sys.argv[1]) as f:
        seq = list(f.readline().strip())
        f.readline()
        poly_map = dict([line.strip().split(' -> ') for line in f.readlines()])

    poly_map = {tuple(doub): res for doub, res in poly_map.items()}
    tup_map = {tup: 0 for tup in poly_map}
    letters = set()
    for tup in poly_map:
        letters.update(tup)
    count_map = {letter: 0 for letter in letters}

    # fill count_map
    for letter in seq:
        count_map[letter] += 1

    # fill tup map
    for i in range(1, len(seq)):
        tup_map[(seq[i-1], seq[i])] += 1

    for _ in tqdm(range(int(sys.argv[2]))):
        next_tup_map = tup_map.copy()
        for tup in tqdm(tup_map, leave=False):
            count_map[poly_map[tup]] += tup_map[tup]
            next_tup_map[(tup[0], poly_map[tup])] += tup_map[tup]
            next_tup_map[(poly_map[tup], tup[1])] += tup_map[tup]
            next_tup_map[tup] -= tup_map[tup]

        tup_map = next_tup_map

    counts = [count_map[letter] for letter in count_map]
    print(max(counts) - min(counts))


main()
