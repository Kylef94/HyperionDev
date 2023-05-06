def minesweeper(grid):
    #set up tuples of offsets for neighbouring cells
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for rc, row in enumerate(grid):  # go through board rows
        for cc, col in enumerate(row):  # go through row's columns

            mines = 0 #set no. of mines to 0 for each entry

            if grid[rc][cc] == '#': #if grid is already # then just move on
                continue
            else:
                for dx, dy in offsets: #iterate through offsets above to get indices for neigbouring squares
                    if (rc + dx) in range(len(grid)) and (cc + dy) in range(len(row)): #checks if field is within range of matrix rows and cols
                        if grid[rc + dx][cc + dy] == '#': #if neibouring cell is a mine, add 1 to mines counter
                            mines += 1
                grid[rc][cc] = mines #set entry equal to no of mines in neibouring cells
    return grid #output result





grid = [['-', '-', '-', '#', '#'],
        ['-', '#', '-', '-', '-'],
        ['-', '-', '#', '-', '-'],
        ['-', '#', '#', '-', '-'],
        ['-', '-', '-', '-', '-']]

print(minesweeper(grid))