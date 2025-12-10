grid = []

# Create 10x10 grid

for i in range(10):

    grid.append(["."] * 10)


target_r = int(input("Row (0-9): "))
target_c = int(input("Col (0-9): "))
grid[target_r][target_c]="X"
x=target_r
y=target_c-1
if 10>x>=0 and 10>y>=0:
    grid[x][y]="*"
x=target_r
y=target_c+1
if 10>x>=0 and 10>y>=0:
    grid[x][y]="*"
x=target_r-1
y=target_c
if 10>x>=0 and 10>y>=0:
    grid[x][y]="*"
x=target_r+1
y=target_c
if 10>x>=0 and 10>y>=0:
    grid[x][y]="*"
x=target_r-1
y=target_c-1
if 10>x>=0 and 10>y>=0:
    grid[x][y]="*"
x=target_r-1
y=target_c+1
if 10>x>=0 and 10>y>=0:
    grid[x][y]="*"
x=target_r+1
y=target_c-1
if 10>x>=0 and 10>y>=0:
    grid[x][y]="*"
x=target_r+1
y=target_c+1
if 10>x>=0 and 10>y>=0:
    grid[x][y]="*"

for i in range(len(grid)):
    print(grid[i])
