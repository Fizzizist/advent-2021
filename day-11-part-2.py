import sys

class Octopus():

    def __init__(self, energy, location, is_null=False):
        self.energy = energy
        self.location = location
        self.neighbors = []
        self.is_null = is_null
        self.flashed = False
        self.flashes = 0

    def assign_neighbors(self, mat):
        y, x = self.location
        self.neighbors = [mat[y - 1][x - 1], mat[y - 1][x], mat[y - 1][x + 1],
                          mat[y][x - 1], mat[y][x +1],
                          mat[y + 1][x - 1], mat[y +1][x], mat[y + 1][x + 1]]

    def add_energy(self):
        if not self.is_null and not self.flashed:
            self.energy += 1
            if self.energy > 9:
                self._flash()

    def _flash(self):
        self.energy = 0
        self.flashed = True
        self.flashes += 1
        for octo in self.neighbors:
            octo.add_energy()


def main():
    with open(sys.argv[1]) as f:
        lines = [list(line.strip()) for line in f.readlines()]
        mat = [[int(item) for item in line] for line in lines]

    # pad the mat with null octopi
    for row in mat:
        row.insert(0, Octopus(0, None, is_null=True))
        row.append(Octopus(0, None, is_null=True))

    mat.insert(0, [Octopus(0, None, is_null=True) for _ in range(len(mat[0]))])
    mat.append([Octopus(0, None, is_null=True) for _ in range(len(mat[0]))])


    # fill the matrix with octopi
    for i in range(1, len(mat) - 1):
        for j in range(1, len(mat[i]) - 1):
            mat[i][j] = Octopus(mat[i][j], (i, j))


    # assign neighbors
    for row in mat[1:-1]:
        for octo in row[1:-1]:
            octo.assign_neighbors(mat)

    synced = False
    steps = 0
    while not synced:
        # add energy and produce flashing
        for row in mat:
            for octo in row:
                octo.add_energy()

        energies = set()
        for row in mat:
            for octo in row:
                energies.add(octo.energy)

        if len(energies) == 1:
            synced = True

        # reset flashes before next step
        for row in mat:
            for octo in row:
                octo.flashed = False

        steps += 1
        print(steps)

    print(steps)

main()
