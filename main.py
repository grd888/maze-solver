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

def main():
  window = Window(800, 600)
  window.draw_line(Line(Point(100, 100), Point(200, 100)))
  window.draw_line(Line(Point(200, 100), Point(200, 200)))
  window.draw_line(Line(Point(200, 200), Point(100, 200)))
  window.draw_line(Line(Point(100, 200), Point(100, 100)))
  window.wait_for_close()

main()
    