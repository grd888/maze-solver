from cell import Cell
import time

class Maze:
  def __init__(
    self,
    x1,
    y1,
    num_rows,
    num_cols,
    cell_size_x,
    cell_size_y,
    win=None
  ):
    self._cells = []
    self._x1 = x1
    self._y1 = y1
    self._num_rows = num_rows
    self._num_cols = num_cols
    self._cell_size_x = cell_size_x
    self._cell_size_y = cell_size_y
    self._win = win
    
    self._create_cells()
    self._break_entrance_and_exit()
    
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
    
    