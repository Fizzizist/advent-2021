import sys
from typing import List, Tuple


def main():
    with open(sys.argv[1]) as f:
        raw = [line.strip().split(' -> ') for line in f.readlines()]  # type: List[List[str]]
    raw = [[item.split(',') for item in items] for items in raw]  # type: List[List[List[str]]]
    processed  = [[(int(x), int(y)) for x, y in items] for items in raw]  # type: List[List[Tuple[int]]]
    
    # filter out non horiz/vertical
    processed = [item for item in processed if (item[0][0] == item[1][0]) or (item[0][1] == item[1][1])]
    
    print(processed)

    max_width = max([max([x for x, _ in coords]) for coords in processed]) + 1
    max_len = max([max([y for _, y in coords]) for coords in processed]) + 1

    print(max_width, max_len)

    # generate matrix to fit x,y coordinates
    landscape = [[0 for _ in range(max_width)] for _ in range(max_len)]
    
    print(len(landscape[0]))

    for coord_set in processed:
        print(coord_set)
        if coord_set[0][0] == coord_set[1][0]:
            y_tuple = (coord_set[0][1], coord_set[1][1])
            for i in range(min(y_tuple), max(y_tuple) + 1):
                landscape[i][coord_set[0][0]] += 1
        else:
            x_tuple = (coord_set[0][0], coord_set[1][0])
            for i in range(min(x_tuple), max(x_tuple) + 1):
                landscape[coord_set[0][1]][i] += 1

    count = 0
    for i in range(max_width):
        for j in range(max_len):
            if landscape[j][i] > 1:
                count += 1
    print(count)
main()
