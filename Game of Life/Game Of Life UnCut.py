#essential Libraries
import numpy as np
from tkinter import *
from tkinter import ttk
import time as time

#Global Variables
cols = 50
rows = 30
res_width = int(1920)
res_height = int(1080)
no_of_blocks = 30
block_size = 15
padding = 0


def make2Darray(rows, cols):

    make2Darray.__doc__ = "Array creation function"

    arr = np.zeros((rows,cols))
    #np.random.seed(1)

    arr1 = arr[padding:rows-padding, padding:cols-padding]

    arr[padding:rows-padding, padding:cols-padding] = arr[padding:rows-padding, padding:cols-padding] + np.random.choice([0,1]  ,size = arr1.shape  )
    
    return arr



def neighbourCount(grid, i, j, rows, cols):

    sum = 0

    # Approach no. 01 ( wrapping around Grid)
    for x in range(-1, 2):
        for y in range(-1, 2):
            row = (i + x + rows) % rows
            col = (j + y + cols) % cols
            sum += grid[row][col]

    sum -= grid[i][j]


    # approach no. 02 to just ignore the edges // the easiest approach
    # if ( i == 0 or j ==0 or i == rows - 1 or j == cols - 1 ):
    #     return sum


    # else:
        
    #     sum += grid[i-1][j-1]       #block no. 1
    #     sum += grid[i][j-1]         #block no. 2
    #     sum += grid[i+1][j-1]       #block no. 3
    #     sum += grid[i-1][j]         #block no. 4
    #     sum += grid[i+1][j]         #block no. 6
    #     sum += grid[i-1][j+1]       #block no. 7
    #     sum += grid[i][j+1]         #block no. 8
    #     sum += grid[i+1][j+1]       #block no. 9


    return sum



def newGrid(grid, rows, cols):

    new_grid = np.copy(grid)


    # Take no. 1  // Original
    for j in range(cols):
        for i in range(rows):
            

            if ( grid[i][j] == 0 and neighbourCount(grid, i, j , rows, cols) == 3 ):
                # any dead cell with 3 neighbours alive, becomes alive by reproduction (rule no. 01)
                grid[i][j] = 1

            

            elif (grid[i][j] == 1 and (neighbourCount(grid, i, j , rows, cols) < 2 or neighbourCount(grid, i, j, rows, cols ) > 3  or i == 0 or j== 0 or i == rows -1 or j == cols - 1)):
                # cell dies due to under or over population (rule np. 02 and 03)
                grid[i][j] = 0
            
            

    # return grid

    # Take no.2 on these rules

    # for i in range(rows):
    #     for j in range(cols):
    #         live_neighbors = neighbourCount(grid, i, j, rows, cols)
    #         if grid[i][j] == 1:
    #             # Rule 1: Any live cell with fewer than two live neighbors dies
    #             if live_neighbors < 2:
    #                 grid[i][j] = 0
    #             # Rule 2: Any live cell with two or three live neighbors lives on to the next generation
    #             elif live_neighbors == 2 or live_neighbors == 3:
    #                 grid[i][j] = 1
    #             # Rule 3: Any live cell with more than three live neighbors dies
    #             elif live_neighbors > 3:
    #                 grid[i][j] = 0
    #         else:
    #             # Rule 4: Any dead cell with exactly three live neighbors becomes a live cell
    #             if live_neighbors == 3:
    #                 grid[i][j] = 1

    #grid = new_grid
    return grid


    





def draw(grid): 

    '''The Display function for the game'''


    grid = newGrid(grid, rows, cols)

    print(grid)
    
    
    cnvs.delete("all")

    # Creating Grid for the game
    for j in range(cols):             #use no_of_blocks if something goes wrong
        for i in range(rows):
            if (grid[i][j] == 1):
                life_state = "white"
            if ( grid[i][j] == 0):
                life_state = "black"

            # old method 
            # cnvs.create_rectangle((j*block_size)+2,(i*block_size)+2,((j*block_size)+50), ((i*block_size)+block_size), fill=life_state) # here the first 2 are coordinates of top left and other of bottom right
    
            # new method
            cnvs.create_rectangle(
            j * block_size,
            i * block_size,
            (j + 1) * block_size,
            (i + 1) * block_size,
            fill=life_state
            )
    

    mainFrame.update()
    




if __name__ == "__main__":

    grid = make2Darray(rows, cols)
    

    mainFrame = Tk(className = "Game of life")
    cnvs = Canvas(mainFrame, height=res_height, width=res_width, bg = "grey")
    cnvs.pack()
    
    while True: #Loop to update Grid at 200 milisecs
        draw(grid)         
        time.sleep(0.05)

    

    mainFrame.mainloop()