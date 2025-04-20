from tkinter import Tk, Canvas

class Window:
  def __init__(self, width, height):
    self.root = Tk()
    self.root.title("Maze Solver")
    self.root.protocol("WM_DELETE_WINDOW", self.close)
    self.canvas = Canvas(self.root, width=width, height=height, bg="white")
    self.canvas.pack()
    self.is_running = False
    
  def draw_line(self, line, fill_color="black"):
    line.draw(self.canvas, fill_color)

  def redraw(self):
    self.root.update_idletasks()
    self.root.update()

  def wait_for_close(self):
    self.is_running = True
    while self.is_running:
      self.redraw()
    
  def close(self):
    self.is_running = False

class Line:
  def __init__(self, point1, point2):
    self.point1 = point1
    self.point2 = point2

  def draw(self, canvas, fill_color):
    canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color)

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

class Cell:
  def __init__(self, window, x1, y1, x2, y2, has_left_wall=True, has_right_wall=True, has_top_wall=True, has_bottom_wall=True):
    self._x1 = x1
    self._y1 = y1
    self._x2 = x2
    self._y2 = y2
    self._win = window
    self.has_left_wall = has_left_wall
    self.has_right_wall = has_right_wall
    self.has_top_wall = has_top_wall
    self.has_bottom_wall = has_bottom_wall

  def draw(self, top_left, bottom_right):
    if self.has_left_wall:
      self._win.canvas.create_line(top_left.x, top_left.y, bottom_right.x, top_left.y, fill="black")
    if self.has_right_wall:
      self._win.canvas.create_line(bottom_right.x, top_left.y, bottom_right.x, bottom_right.y, fill="black")
    if self.has_top_wall:
      self._win.canvas.create_line(bottom_right.x, bottom_right.y, top_left.x, bottom_right.y, fill="black")
    if self.has_bottom_wall:
      self._win.canvas.create_line(top_left.x, bottom_right.y, top_left.x, top_left.y, fill="black")
    

def main():
  window = Window(800, 600)
  # window.draw_line(Line(Point(100, 100), Point(200, 100)))
  # window.draw_line(Line(Point(200, 100), Point(200, 200)))
  # window.draw_line(Line(Point(200, 200), Point(100, 200)))
  # window.draw_line(Line(Point(100, 200), Point(100, 100)))
  cell = Cell(window, 100, 100, 200, 200)
  cell.has_right_wall = False
  cell.draw(Point(100, 100), Point(200, 200))
  window.wait_for_close()

main()
    