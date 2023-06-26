import numpy as np
from tkinter import *
import time

# Global Variables
cols = 50
rows = 35
res_width = int(1920)
res_height = int(1080)
block_size = 10
padding = 0


def make2Darray(rows, cols):
    arr = np.zeros((rows, cols))
    arr1 = arr[padding:rows-padding, padding:cols-padding]
    arr[padding:rows-padding, padding:cols-padding] = np.random.choice([0, 1], size=arr1.shape)
    return arr


def neighbourCount(grid, i, j, rows, cols):
    sum = 0
    for x in range(-1, 2):
        for y in range(-1, 2):
            row = (i + x + rows) % rows
            col = (j + y + cols) % cols
            sum += grid[row][col]
    sum -= grid[i][j]
    return sum


def newGrid(grid, rows, cols):
    new_grid = np.copy(grid)
    for j in range(cols):
        for i in range(rows):
            live_neighbors = neighbourCount(grid, i, j, rows, cols)
            if grid[i][j] == 1:
                # Rule 1: Any live cell with fewer than two live neighbors dies
                if live_neighbors < 2:
                    new_grid[i][j] = 0
                # Rule 2: Any live cell with two or three live neighbors lives on to the next generation
                elif live_neighbors == 2 or live_neighbors == 3:
                    new_grid[i][j] = 1
                # Rule 3: Any live cell with more than three live neighbors dies
                elif live_neighbors > 3:
                    new_grid[i][j] = 0
            else:
                # Rule 4: Any dead cell with exactly three live neighbors becomes a live cell
                if live_neighbors == 3:
                    new_grid[i][j] = 1
    return new_grid


def draw(grid):
    cnvs.delete("all")

    # Calculate the offset to center the grid on the canvas
    grid_width = cols * block_size
    grid_height = rows * block_size
    offset_x = (res_width - grid_width) // 3
    offset_y = (res_height - grid_height) // 4

    for j in range(cols):
        for i in range(rows):
            if grid[i][j] == 1:
                life_state = "white"
            else:
                life_state = "black"
            cnvs.create_rectangle(
                offset_x + j * block_size,
                offset_y + i * block_size,
                offset_x + (j + 1) * block_size,
                offset_y + (i + 1) * block_size,
                fill=life_state
            )
    mainFrame.update()


if __name__ == "__main__":
    grid = make2Darray(rows, cols)
    mainFrame = Tk(className="Game of life")
    cnvs = Canvas(mainFrame, height=res_height, width=res_width, bg="dark grey")
    cnvs.pack()
    while True:
        grid = newGrid(grid, rows, cols)
        draw(grid)
        time.sleep(0.05)
    mainFrame.mainloop()
