import sys

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
                low_points.append(mat[i][j])
                print(f'\033[92m{mat[i][j]}\033[0m', end='')
            else:
                print(mat[i][j], end='')

    low_points = [i + 1 for i in low_points]

    print(f'\n\n{sum(low_points)}')

main()
