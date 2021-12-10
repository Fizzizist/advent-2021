import sys


CHECKED = set()


def check_coords(coords, mat):
    x, y = coords
    global CHECKED

    if mat[x][y] == 9 or coords in CHECKED:
        return
    else:
        CHECKED.add(coords)

    to_check = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for item in to_check:
        check_coords(item, mat)


def main():
    with open(sys.argv[1]) as f:
        mat = [[int(i) for i in list(item.strip())] for item in f.readlines()]
    # pad the matrix with 9s so that its easier to loop through
    for i in mat:
        i.insert(0, 9)
        i.append(9)
    mat.insert(0, [9 for _ in range(len(mat[0]))])
    mat.append([9 for _ in range(len(mat[0]))])

    mat_height = len(mat) - 1
    mat_width = len(mat[0]) - 1

    # get inner low points
    low_points = []
    for i in range(1, mat_height):
        print('')
        for j in range(1, mat_width):
            low_point = min([mat[i-1][j], mat[i][j-1], mat[i][j+1], mat[i+1][j]])
            if mat[i][j] < low_point:
                low_points.append((i, j))
                print(f'\033[92m{mat[i][j]}\033[0m', end='')
            else:
                print(mat[i][j], end='')

    global CHECKED
    basins = []
    for item in low_points:
        check_coords(item, mat)
        basins.append(len(CHECKED))
        CHECKED = set()

    top_three = sorted(basins)[-3:]
    print(f'\n\n{top_three[0] * top_three[1] * top_three[2]}')



main()
