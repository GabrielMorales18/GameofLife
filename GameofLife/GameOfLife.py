"""
conway.py 
A simple Python/matplotlib implementation of Conway's Game of Life.
"""

import sys, argparse
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib.animation as animation
from datetime import date

ON = 255
OFF = 0
vals = [ON, OFF]

def randomGrid(N,M):
    """returns a grid of NxN random values"""
    return np.random.choice(vals, N*M, p=[0.2, 0.8]).reshape(N, M)
def addGlider(i, j, grid):
    """adds a glider with top left cell at (i, j)"""
    glider = np.array([[0,  0, 255], 
                       [255,  0, 255], 
                       [0,  255, 255]])
    grid[i:i+3, j:j+3] = glider

def update(frameNum, img, grid, N, M, document):
    # copy grid since we require 8 neighbors for calculation
    # and we go line by line 
    newGrid = grid.copy()

    #The grids for every figure to check

    Block = np.array([[0,   0,   0, 0],
                      [0, 255, 255, 0],
                      [0, 255, 255, 0],
                      [0,   0,  0,  0]])
    
    Beehive = np.array([[  0,   0,   0,   0,   0,   0],
                        [  0,   0, 255, 255,   0,   0],
                        [  0, 255,   0,   0, 255,   0],
                        [  0,   0, 255, 255,   0,   0],
                        [  0,   0,   0,   0,   0,   0]])

    Loaf = np.array([[  0,   0,   0,   0,   0,   0],
                     [  0,   0, 255, 255,   0,   0],
                     [  0, 255,   0,   0, 255,   0],
                     [  0,   0, 255,   0, 255,   0],
                     [  0,   0,   0, 255,   0,   0],
                     [  0,   0,   0,   0,   0,   0]])

    Boat = np.array([[  0,   0,   0,   0,   0],
                     [  0, 255, 255,   0,   0],
                     [  0, 255,   0, 255,   0],
                     [  0,   0, 255,   0,   0],
                     [  0,   0,   0,   0,   0]])
    
    Tub = np.array([[  0,    0,   0,   0,   0],
                     [  0,   0, 255,   0,   0],
                     [  0, 255,   0, 255,   0],
                     [  0,   0, 255,   0,   0],
                     [  0,   0,   0,   0,   0]])
    
    Blinker1 = np.array([[  0,    0,   0],
                         [  0,  255,   0],
                         [  0,  255,   0],
                         [  0,  255,   0],
                         [  0,    0,   0]])
                    
    Blinker2 = np.array([[  0,   0,   0,   0,   0],
                         [  0, 255, 255, 255,   0],
                         [  0,   0,   0,   0,   0]])
    
    Toad1 = np.array([[  0,    0,   0,   0,   0,   0],
                      [  0,    0,   0, 255,   0,   0],
                      [  0,  255,   0,   0, 255,   0],
                      [  0,  255,   0,   0, 255,   0],
                      [  0,    0, 255,   0,   0,   0],
                      [  0,    0,   0,   0,   0,   0]])
                    
    Toad2 = np.array([[  0,    0,   0,   0,   0,   0],
                      [  0,    0, 255, 255, 255,   0],
                      [  0,  255, 255, 255,   0,   0],
                      [  0,    0,   0,   0,   0,   0]])

    Beacon1 = np.array([[  0,    0,   0,   0,   0,   0],
                        [  0,  255, 255,   0,   0,   0],
                        [  0,  255, 255,   0,   0,   0],
                        [  0,    0,   0, 255, 255,   0],
                        [  0,    0,   0, 255, 255,   0],
                        [  0,    0,   0,   0,   0,   0]])

    Beacon2 = np.array([[  0,    0,   0,   0,   0,   0],
                        [  0,  255, 255,   0,   0,   0],
                        [  0,  255,   0,   0,   0,   0],
                        [  0,    0,   0,   0, 255,   0],
                        [  0,    0,   0, 255, 255,   0],
                        [  0,    0,   0,   0,   0,   0]])

    Glider1 = np.array([[  0,    0,   0,   0,   0],
                        [  0,    0, 255,   0,   0],
                        [  0,    0,   0, 255,   0],
                        [  0,  255, 255, 255,   0],
                        [  0,    0,   0,   0,   0]])

    Glider2 = np.array([[  0,    0,   0,   0,   0],
                        [  0,  255,   0, 255,   0],
                        [  0,    0, 255, 255,   0],
                        [  0,    0, 255,   0,   0],
                        [  0,    0,   0,   0,   0]])

    Glider3 = np.array([[  0,    0,   0,   0,   0],
                        [  0,    0,   0, 255,   0],
                        [  0,  255,   0, 255,   0],
                        [  0,    0, 255, 255,   0],
                        [  0,    0,   0,   0,   0]])

    Glider4 = np.array([[  0,    0,   0,   0,   0],
                        [  0,  255,   0,   0,   0],
                        [  0,    0, 255, 255,   0],
                        [  0,  255, 255,   0,   0],
                        [  0,    0,   0,   0,   0]])

    SpaceShip1 = np.array([[  0,    0,   0,   0,   0,   0,   0],
                           [  0,  255,   0,   0, 255,   0,   0],
                           [  0,    0,   0,   0,   0, 255,   0],
                           [  0,  255,   0,   0,   0, 255,   0],
                           [  0,    0, 255, 255, 255, 255,   0],
                           [  0,    0,   0,   0,   0,   0,   0]])

    SpaceShip2 = np.array([[  0,    0,   0,   0,   0,   0,   0],
                           [  0,    0,   0, 255, 255,   0,   0],
                           [  0,  255, 255,   0, 255, 255,   0],
                           [  0,  255, 255, 255, 255,   0,   0],
                           [  0,    0, 255, 255,   0,   0,   0],
                           [  0,    0,   0,   0,   0,   0,   0]])

    SpaceShip3 = np.array([[  0,    0,   0,   0,   0,   0,   0],
                           [  0,    0, 255, 255, 255, 255,   0],
                           [  0,  255,   0,   0,   0, 255,   0],
                           [  0,    0,   0,   0,   0, 255,   0],
                           [  0,  255,   0,   0, 255,   0,   0],
                           [  0,    0,   0,   0,   0,   0,   0]])

    SpaceShip4 = np.array([[  0,    0,   0,   0,   0,   0,   0],
                           [  0,    0, 255, 255,   0,   0,   0],
                           [  0,  255, 255, 255, 255,   0,   0],
                           [  0,  255, 255,   0, 255, 255,   0],
                           [  0,    0,   0, 255, 255,   0,   0],
                           [  0,    0,   0,   0,   0,   0,   0]])

    #Number of figures found

    block = 0
    beehive = 0
    loaf = 0
    boat = 0
    tub = 0
    blinker = 0
    toad = 0
    beacon = 0
    glider = 0
    lgSpaceShip = 0
    total = 0

    # TODO: Implement the rules of Conway's Game of Life
    for i in range(0,M+3):
        for j in range(0,N+3):
            neighbors = 0
            #Check neighbors
            if i>0 and i<M+1 and j>0 and j<N+1:
                if grid[i-1,j-1] == 255:
                    neighbors += 1
                if grid[i-1,j] == 255:
                    neighbors += 1    
                if grid[i-1,j+1] == 255:
                    neighbors += 1
                if grid[i,j-1] == 255:
                    neighbors += 1
                if grid[i,j+1] == 255:
                    neighbors += 1
                if grid[i+1,j-1] == 255:
                    neighbors += 1
                if grid[i+1,j] == 255:
                    neighbors += 1    
                if grid[i+1,j+1] == 255:
                    neighbors += 1
                if grid[i,j] == 255:
                    if neighbors == 2 or neighbors == 3:
                        newGrid[i,j] = 255
                    else:
                        newGrid[i,j] = 0
                if grid[i,j] == 0:
                    if neighbors == 3:
                        newGrid[i,j] = 255
            #Block
            if np.array_equal(grid[i:i+4, j:j+4], Block, equal_nan=True):
                block+=1
            #Beehive
            if np.array_equal(grid[i:i+5, j:j+6], Beehive, equal_nan=True):
                beehive+=1
            #Loaf
            if np.array_equal(grid[i:i+6, j:j+6], Loaf, equal_nan=True):
                loaf+=1
            #Boat
            if np.array_equal(grid[i:i+5, j:j+5], Boat, equal_nan=True):
                boat+=1
            #Tub
            if np.array_equal(grid[i:i+5, j:j+5], Tub, equal_nan=True):
                tub+=1
            #Blinker
            if np.array_equal(grid[i:i+5, j:j+3], Blinker1, equal_nan=True) or np.array_equal(grid[i:i+3, j:j+5], Blinker2, equal_nan=True):
                blinker+=1
            #Toad
            if np.array_equal(grid[i:i+6, j:j+6], Toad1, equal_nan=True) or np.array_equal(grid[i:i+4, j:j+6], Toad2, equal_nan=True):
                toad+=1
            #Beacon
            if np.array_equal(grid[i:i+6, j:j+6], Beacon1, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+6], Beacon2, equal_nan=True):
                beacon+=1
            #Glider
            if np.array_equal(grid[i:i+5, j:j+5], Glider1, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5], Glider2, equal_nan=True) or \
                np.array_equal(grid[i:i+5, j:j+5], Glider3, equal_nan=True) or np.array_equal(grid[i:i+5, j:j+5], Glider4, equal_nan=True):
                glider+=1
            #SpaceShip
            if np.array_equal(grid[i:i+6, j:j+7 ], SpaceShip1, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+7], SpaceShip2, equal_nan=True) or \
                np.array_equal(grid[i:i+6, j:j+7], SpaceShip3, equal_nan=True) or np.array_equal(grid[i:i+6, j:j+7], SpaceShip4, equal_nan=True):
                lgSpaceShip+=1

    total = block+beehive+loaf+boat+tub+blinker+toad+beacon+glider+lgSpaceShip

    #In case there are no figure it place 1 to evade division by 0
    cero = False
    if total == 0:
        total = 1
        cero = True

    if frameNum == 0:
        document.write("Iteration: " + str(frameNum+1) + "\n")
    else:
        document.write("Iteration: " + str(frameNum+2) + "\n")
                                                    
    document.write("--------------------------------\n")
    document.write("|            | Count | Percent |\n")
    document.write("--------------------------------\n")
    document.write("|    Block   | "+str(block)+" | "+str((block/total)*100)+" |\n")
    document.write("|   Beehive  | "+str(beehive)+" | "+str((beehive/total)*100)+" |\n")
    document.write("|    Loaf    | "+str(loaf)+" | "+str((loaf/total)*100)+" |\n")
    document.write("|    Boat    | "+str(boat)+" | "+str((boat/total)*100)+" |\n")
    document.write("|     Tub    | "+str(tub)+" | "+str((tub/total)*100)+" |\n")
    document.write("|   Blinker  | "+str(blinker)+" | "+str((blinker/total)*100)+" |\n")
    document.write("|    Toad    | "+str(toad)+" | "+str((toad/total)*100)+" |\n")
    document.write("|   Beacon   | "+str(beacon)+" | "+str((beacon/total)*100)+" |\n")
    document.write("|   Glidier  | "+str(glider)+" | "+str((glider/total)*100)+" |\n")
    document.write("| LG sp ship | "+str(lgSpaceShip)+" | "+str((lgSpaceShip/total)*100)+" |\n")
    document.write("--------------------------------\n")
    if cero:
        document.write("|    Total   | "+str(total-1)+" |         |\n")
    else:
        document.write("|    Total   | "+str(total)+" |         |\n")
    document.write("--------------------------------\n")

    # update data
    img.set_data(grid[1:M+1,1:N+1])
    grid[:] = newGrid[:]

    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    f = open("GameGrid-5.txt", "r")
    g = open("SimulationOutput.txt", "w")

    # set grid size
    size = f.readline().split()
    M = int(size[1])
    N = int(size[0])

    gen = f.readline().split()
    generations = int(gen[0])

    # set animation update interval
    updateInterval = 10

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    #grid = randomGrid(N,M)
    # Uncomment lines to see the "glider" demo
    
    #Create a bigger grid to evade corner and border cases
    grid = np.zeros((M+2)*(N+2)).reshape(M+2,N+2)
    #addGlider(1, 1, grid)

    g.write("Simulation at " + str(date.today()) + "\n")
    g.write("Universe size " + str(N) + " x " + str(M) + "\n")

    for line in f:
        cell = line.split()
        grid[int(cell[1])+1,int(cell[0])+1] = 255

    # set up animation
    fig, ax = plt.subplots()
    #Evade the extra cells of the grid in the image
    img = ax.imshow(grid[1:M+1,1:N+1], interpolation='nearest')
    plt.axis('off')
    
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N, M, g),
                                  frames = generations-1,
                                  interval=updateInterval,
                                  save_count=50, 
                                  repeat=False)


    plt.show()
    f.close()
    g.close()

# call main
if __name__ == '__main__':
    main()