import sys


# Using Dijkstra's traversal algorithm
def main():
    with open(sys.argv[1]) as f:
        lines = [line.strip() for line in f.readlines()]
        mat = [[int(item) for item in line] for line in lines]

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

    end_not_visited = True
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

        unvisited.remove(current)
        min_unvisited = min([tent_dists[item[0]][item[1]] for item in unvisited
                             if tent_dists[item[0]][item[1]] is not None])
        for i, j in unvisited:
            if tent_dists[i][j] == min_unvisited:
                current = (i, j)

        if current == end:
            end_not_visited = False

    print(tent_dists[current[0]][current[1]])




main()
