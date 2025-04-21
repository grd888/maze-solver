from cell import Cell
import time
import random

class Maze:
  def __init__(
    self,
    x1,
    y1,
    num_rows,
    num_cols,
    cell_size_x,
    cell_size_y,
    win=None,
    seed=None
  ):
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    if seed is not None:
      random.seed(seed)
    
    self._create_cells()
    self._break_entrance_and_exit()
    self._break_walls_r(0, 0)
    self._reset_cells_visited()
    
  def _create_cells(self):
    # Initialize the cells matrix
    
    for i in range(self._num_cols):
      column = []
      for j in range(self._num_rows):
        # Create a Cell for each position in the grid
        cell = Cell(self._win)
        column.append(cell)
        # Calculate the cell's coordinates
      self._cells.append(column)
    
    for i in range(self._num_cols):
      for j in range(self._num_rows):
        self._draw_cell(i, j)
        
  def _draw_cell(self, i, j):
    if self._win is None:
      return
    # Calculate the cell's coordinates
    x1 = self._x1 + i * self._cell_size_x
    y1 = self._y1 + j * self._cell_size_y
    x2 = x1 + self._cell_size_x
    y2 = y1 + self._cell_size_y
    # Draw the cell
    self._cells[i][j].draw(x1, y1, x2, y2)
    self._animate()
    
  def _animate(self):
    if self._win is None:
      return
    self._win.redraw()
    time.sleep(0.01)
    
  def _break_entrance_and_exit(self):
    entry_cell = self._cells[0][0]
    entry_cell.has_top_wall = False
    exit_cell = self._cells[self._num_cols - 1][self._num_rows - 1]
    exit_cell.has_bottom_wall = False
    self._draw_cell(0, 0)
    self._draw_cell(self._num_cols - 1, self._num_rows - 1)
    
  def _break_walls_r(self, i, j):
    # Mark the current cell as visited
    self._cells[i][j].visited = True
    
    while True:
      # Create a list to hold possible directions (cells that haven't been visited)
      possible_directions = []
      
      # Check adjacent cells (up, right, down, left)
      # Up (j-1)
      if j > 0 and not self._cells[i][j-1].visited:
        possible_directions.append((i, j-1, "up"))
      
      # Right (i+1)
      if i < self._num_cols - 1 and not self._cells[i+1][j].visited:
        possible_directions.append((i+1, j, "right"))
      
      # Down (j+1)
      if j < self._num_rows - 1 and not self._cells[i][j+1].visited:
        possible_directions.append((i, j+1, "down"))
      
      # Left (i-1)
      if i > 0 and not self._cells[i-1][j].visited:
        possible_directions.append((i-1, j, "left"))
      
      # If there are no possible directions, draw the current cell and return
      if len(possible_directions) == 0:
        self._draw_cell(i, j)
        return
      
      # Choose a random direction from the possible directions
      direction_index = random.randrange(len(possible_directions))
      next_i, next_j, direction = possible_directions[direction_index]
      
      # Break down the walls between the current cell and the chosen cell
      if direction == "up":
        self._cells[i][j].has_top_wall = False
        self._cells[next_i][next_j].has_bottom_wall = False
      elif direction == "right":
        self._cells[i][j].has_right_wall = False
        self._cells[next_i][next_j].has_left_wall = False
      elif direction == "down":
        self._cells[i][j].has_bottom_wall = False
        self._cells[next_i][next_j].has_top_wall = False
      elif direction == "left":
        self._cells[i][j].has_left_wall = False
        self._cells[next_i][next_j].has_right_wall = False
      
      # Recursively visit the chosen cell
      self._break_walls_r(next_i, next_j)
      
  def _reset_cells_visited(self):
    for col in self._cells:
      for cell in col:
        cell.visited = False