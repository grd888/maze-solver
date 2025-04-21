# Maze Solver

A Python application that generates and solves mazes using depth-first search algorithms.

## Overview

This project implements a maze generator and solver with a graphical interface. It creates random mazes using a recursive depth-first search algorithm and then solves them using a similar approach. The solution path is visualized in real-time.

## Features

- Random maze generation using depth-first search
- Maze solving with path visualization
- Configurable maze dimensions
- Customizable animation speed
- Support for setting random seeds for reproducible mazes

## Project Structure

- `main.py` - Entry point for the application
- `maze.py` - Contains the Maze class for generating and solving mazes
- `cell.py` - Contains the Cell class representing individual maze cells
- `graphics.py` - Provides the graphical interface for visualization
- `tests.py` - Unit tests for the project

## Requirements

- Python 3.6 or higher
- No external dependencies beyond the Python standard library

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd maze_solver
   ```

2. No additional installation steps are required as the project uses only Python's standard library.

## Usage

### Running the Application

To run the maze generator and solver:

```
python main.py
```

This will:
1. Create a window with a randomly generated maze
2. Pause briefly to allow you to view the maze
3. Automatically solve the maze, showing the path from start to finish

### Customizing the Maze

You can modify parameters in `main.py` to customize the maze:

- `num_rows` and `num_cols` - Change the dimensions of the maze
- `margin` - Adjust the margin around the maze
- `screen_x` and `screen_y` - Change the window size
- The seed value in the Maze constructor (e.g., `win, 10`) - Change to get different maze patterns

### Running Tests

To run the unit tests:

```
python tests.py
```

## How It Works

### Maze Generation

The maze is generated using a recursive depth-first search algorithm:
1. Start at a random cell
2. Mark the current cell as visited
3. While there are unvisited adjacent cells:
   - Choose a random unvisited neighbor
   - Remove the wall between the current cell and the chosen cell
   - Recursively apply the algorithm to the chosen cell

### Maze Solving

The maze is solved using another depth-first search algorithm:
1. Start at the entrance (top-left)
2. Mark the current cell as visited
3. If the current cell is the exit (bottom-right), the maze is solved
4. Otherwise, for each direction (up, right, down, left):
   - If there's no wall in that direction and the adjacent cell hasn't been visited:
     - Move to that cell and recursively try to solve the maze
     - If the recursive call returns true, the maze is solved
     - Otherwise, backtrack and try another direction

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
