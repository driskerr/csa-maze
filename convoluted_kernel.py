#9
from random import randint

#1
def build_maze(m, n, swag):
  #2
  grid = []
  #3
  for i in range(m):
    row = ["wall" for i in range(n)]
    grid.append(row)
  #9
  start_i = randint(0, m-1)
  start_j = randint(0,n-1)
  grid[start_i][start_j] = "start"
  #20
  mow(grid, start_i, start_j)
  #34
  explore_maze(grid, start_i, start_j, swag)
  #4
  return grid

#5
def print_maze(grid):
  #6
  for row in grid:
    printable_row = ""
    #7
    for cell in row:
      if cell == "wall":
        char = "|"
      #33
      elif cell == "empty":
        char = " "
      else:
        char = cell[0]
      printable_row += char
    #8
    print(printable_row)
    
#10
def mow(grid, i, j):
  #11
  directions = ["U", "D", "L", "R"]
  #12
  while len(directions) > 0:
    #13
    directions_index = randint(0, len(directions)-1)
    #14
    direction = directions.pop(directions_index)
    #15
    # U 	i -			j same
    # D		i +			j same
    # L		i same	j -
    # R		i same	j +
    #16
    if direction == "U":
     #17
      if i-2 < 0:
        continue
      #18
      elif grid[i-2][j] == "wall":
          grid[i-1][j] = "empty"
          grid[i-2][j] = "empty"
          #19
          mow(grid, i-2, j)
    elif direction == "D":
      if i+2 >= len(grid):
        continue
      elif grid[i+2][j] == "wall":
        grid[i+1][j] = "empty"
        grid[i+2][j] = "empty"
        mow(grid, i+2, j)
    elif direction == "L":
      if j-2 < 0:
        continue
      elif grid[i][j-2] == "wall":
        grid[i][j-1] = "empty"
        grid[i][j-2] = "empty"
        mow(grid, i, j-2)
    else: #direction == "R"
      if j+2 >= len(grid[0]):
        continue
      elif grid[i][j+2] == "wall":
        grid[i][j+1] = "empty"
        grid[i][j+2] = "empty"
        mow(grid, i, j+2)
        
#21
def explore_maze(grid, start_i, start_j, swag):
  #22
  grid_copy = [row[:] for row in grid]
  #23
  bfs_queue = [ [start_i, start_j] ]
  directions = ["U", "D", "L", "R"]
  #24
  while bfs_queue:
    i, j = bfs_queue.pop(0)
    
    #25
    if grid[i][j] != "start" and randint(1,10) == 1:
      #26
      grid[i][j] = swag[randint(0, len(swag) - 1)]
    #27
    grid_copy[i][j] = "visited"
    
    #28
    for direction in directions:
      explore_i = i
      explore_j = j
      
      #29
      if direction == "U":
        explore_i = i - 1
      elif direction == "D":
        explore_i = i + 1
      elif direction == "L":
        explore_j = j - 1
      else: # direction == "R"
        explore_j = j + 1
        
      #30
      if explore_i < 0 or explore_j < 0 or explore_i >= len(grid) or explore_j >= len(grid[0]):
        continue
      #31
      elif grid[explore_i][explore_j] != "wall" and grid_copy[explore_i][explore_j] != "visited":
        bfs_queue.append([explore_i, explore_j])
  #32
  grid[i][j] = "end"
        
    
    

#4, cont
#print(build_maze(5,10,None))
#8, cont / 20, cont
#print_maze(build_maze(5,10,None))
#34
print_maze(build_maze(15,25,['candy corn','werewolf', 'pumpkin']))
