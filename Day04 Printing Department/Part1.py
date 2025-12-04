
grid = list()
with open("input.txt", "r") as inf:
    grid = [line.strip() for line in inf.readlines()]
width = len(grid[0])
height = len(grid)

def get_adjacents(x, y) -> int:
    no_rolls = 0
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for x2, y2 in directions:
        if 0 <= x+x2 < width and 0 <= y+y2 < height:
            if grid[x+x2][y+y2] == "@":
                no_rolls += 1
    return no_rolls


total = 0
for y in range(height):
    for x in range(width):
        if grid[x][y] == "@" and get_adjacents(x, y) < 4:
            total += 1

print(total)
