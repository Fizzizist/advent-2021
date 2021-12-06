import sys
from typing import List, Tuple


def main():
    with open(sys.argv[1]) as f:
        raw = [line.strip().split(' -> ') for line in f.readlines()]  # type: List[List[str]]
    raw = [[item.split(',') for item in items] for items in raw]  # type: List[List[List[str]]]
    processed  = [[(int(x), int(y)) for x, y in items] for items in raw]  # type: List[List[Tuple[int]]]

    max_width = max([max([x for x, _ in coords]) for coords in processed]) + 1
    max_len = max([max([y for _, y in coords]) for coords in processed]) + 1

    # generate matrix to fit x,y coordinates
    landscape = [[0 for _ in range(max_width)] for _ in range(max_len)]

    for coord_set in processed:
        x_tuple = (coord_set[0][0], coord_set[1][0])
        y_tuple = (coord_set[0][1], coord_set[1][1])
        x_range = range(min(x_tuple), max(x_tuple) + 1)
        y_range = range(min(y_tuple), max(y_tuple) + 1)
        if coord_set[0][0] == coord_set[1][0]:
            for i in y_range:
                landscape[i][coord_set[0][0]] += 1
        elif coord_set[0][1] == coord_set[1][1]:
            for i in x_range:
                landscape[coord_set[0][1]][i] += 1
        # diagonal case
        else:
            cond0 = (coord_set[0][0] < coord_set[1][0] and coord_set[0][1] < coord_set[1][1])
            cond1 = (coord_set[0][0] > coord_set[1][0] and coord_set[0][1] > coord_set[1][1])
            if cond0 or cond1:   
                for x, y in zip(x_range, y_range):
                    landscape[y][x] += 1
            else:
                for x, y in zip(x_range, reversed(y_range)):
                    landscape[y][x] += 1

    count = 0
    for i in range(max_width):
        for j in range(max_len):
            if landscape[j][i] > 1:
                count += 1
    print(count)

main()
