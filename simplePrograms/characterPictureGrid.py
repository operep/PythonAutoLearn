#!python2
#Simple program which displays how to print matrix

grid = [
        ['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']
]

j = 0
result = ''

while j < len(grid[0]):
    i = 0
    while i < len(grid):
        result += grid[i][j]
        i += 1
    j += 1

    print(result)
    result = ''
