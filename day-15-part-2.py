import sys
from tqdm import tqdm


def expand_mat(mat):
    next_mat = mat.copy()
    final_mat = mat.copy()
    for _ in range(4):
        next_mat = [[item + 1 if item != 9 else 1 for item in row] for row in next_mat]
        for i in range(len(final_mat)):
            final_mat[i].extend(next_mat[i])

    next_mat = final_mat.copy()
    for _ in range(4):
        next_mat = [[item + 1 if item != 9 else 1 for item in row] for row in next_mat]
        final_mat.extend(next_mat)

    return final_mat

# Using Dijkstra's traversal algorithm
def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
        mat = [[int(item) for item in line] for line in lines]

    mat = expand_mat(mat)

    # Mark all nodes unvisited. Create a set of all the unvisited nodes
    #  called the unvisited set.
    unvisited = set()
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            unvisited.add((i, j))

    # Assign every node a tentative distance value
    tent_dists = [[None for _ in item] for item in mat]
    # set to zero for initial node
    tent_dists[0][0] = 0

    # set the initial node as "current"
    current = (0, 0)

    end = (len(mat) - 1, len(mat[0]) - 1)

    pbar = tqdm()
    end_not_visited = True
    assigned_unvisited = dict()
    while end_not_visited:
        neighbors  = [(current[0] + 1, current[1]),
                      (current[0] - 1, current[1]),
                      (current[0], current[1] + 1),
                      (current[0], current[1] - 1)]
        neighbors = [item for item in neighbors if item in unvisited]
        for neighbor in neighbors:
            dist = tent_dists[current[0]][current[1]] + mat[neighbor[0]][neighbor[1]]
            if tent_dists[neighbor[0]][neighbor[1]] is None or tent_dists[neighbor[0]][neighbor[1]] > dist:
                tent_dists[neighbor[0]][neighbor[1]] = dist
                assigned_unvisited[neighbor] = dist

        assigned_unvisited.pop(current, None)
        unvisited.remove(current)

        min_unvisited = min([val for _, val in assigned_unvisited.items()])
        for tup in assigned_unvisited:
            if min_unvisited == assigned_unvisited[tup]:
                current = tup

        if current == end:
            end_not_visited = False

        pbar.update(1)

    pbar.close()
    print(tent_dists[current[0]][current[1]])




main()
