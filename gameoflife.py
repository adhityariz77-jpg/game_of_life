def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 1:
                print("■", end=" ")
            else:
                print(".", end=" ")
        print()
    print()


def count_neighbors(grid, r, c):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            nr = r + i
            nc = c + j
            if 0 <= nr < rows and 0 <= nc < cols:
                count += grid[nr][nc]

    return count


# input manual untuk grid awal
grid = [
    [0,0,1],
    [0,1,0],
    [0,1,0]
]

generasi = 5

for g in range(generasi):
    print("Generasi", g)
    print_grid(grid)

    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0]*cols for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            tetangga = count_neighbors(grid, r, c)

            if grid[r][c] == 1:
                if tetangga == 2 or tetangga == 3:
                    new_grid[r][c] = 1
                else:
                    new_grid[r][c] = 0
            else:
                if tetangga == 3:
                    new_grid[r][c] = 1

    grid = new_grid