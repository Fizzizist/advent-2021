import sys


def print_coords(coords):
    max_width = max([x for x, _ in coords])
    max_height = max([y for _, y in coords])

    for y in range(max_height + 1):
        print('')
        for x in range(max_width + 1):
            print('.' if (x, y) not in coords else '#', end='')




def main():
    coords = []
    folds = []
    with open(sys.argv[1]) as f:
        coord = True
        for line in f.readlines():
            if line == '\n':
                coord = False
            elif coord:
                coords.append(line.strip().split(','))
            else:
                folds.append(line.strip().split(' ')[2])

    fold = folds[0].split('=')
    fold = (fold[0], int(fold[1]))

    coords = [[int(item[0]), int(item[1])] for item in coords]

    #print_coords([tuple(item) for item in coords])

    ch_idx = 0 if fold[0] == 'x' else 1
    for i in range(len(coords)):
        if coords[i][ch_idx] > fold[1]:
            coords[i][ch_idx] = coords[i][ch_idx] + ((coords[i][ch_idx] - fold[1]) * -2)

    coords = {tuple(item) for item in coords}

    #print('')
    #print_coords(coords)

    #print('\n\n')
    print(len(coords))


main()
