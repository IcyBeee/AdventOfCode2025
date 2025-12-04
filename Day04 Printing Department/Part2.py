
grid = list()
with open("input.txt", "r") as inf:
    grid = [list(line.strip()) for line in inf.readlines()]
width = len(grid[0])
height = len(grid)

def get_adjacents(x, y) -> int:
    no_rolls = 0
    directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    for dx, dy in directions:
        adjx = x+dx
        adjy = y+dy
        if 0 <= adjx < width and 0 <= adjy < height:
            if grid[adjx][adjy] == "@":
                no_rolls += 1
    return no_rolls

total = 0
removed = True
while removed:
    removals = list()
    for y in range(height):
        for x in range(width):
            if grid[x][y] == "@" and get_adjacents(x, y) < 4:
                removals.append((x, y))
    if removals:
        for x, y in removals:
            grid[x][y] = "."
            total += 1
    else:
        removed = False

print(total)
