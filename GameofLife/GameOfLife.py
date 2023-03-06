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
    for i in range(0,N):
        for j in range(0,M):
            neighbors = 0
            if i>0 and i<N-1 and j>0 and j<M-1:
                for a in range(-1,2):
                    for b in range(-1,2):
                        if grid[i+a][j+b] == 255:
                            neighbors += 1
                        if a==0 and b==0 and grid[i+a][j+b] == 255:
                            neighbors -= 1
                if grid[i][j] == 255:
                    if neighbors == 2 or neighbors == 3:    
                        newGrid[i][j] = 255
                    else:
                        newGrid[i][j] = 0
                if grid[i][j] == 0:
                    if neighbors == 3:
                        newGrid[i][j] = 255
            if i == 0 and j == 0:
                for a in range(0,2):
                    for b in range(0,2):
                        if grid[i+a][j+b] == 255:
                            neighbors += 1
                        if a==0 and b==0 and grid[i+a][j+b] == 255:
                            neighbors -= 1
                if grid[i][j] == 255:
                    if neighbors == 2 or neighbors == 3:    
                        newGrid[i][j] = 255
                    else:
                        newGrid[i][j] = 0
                if grid[i][j] == 0:
                    if neighbors == 3:
                        newGrid[i][j] = 255
            if i == 0 and j == M-1:
                for a in range(0,2):
                    for b in range(-1,1):
                        if grid[i+a][j+b] == 255:
                            neighbors += 1
                        if a==0 and b==0 and grid[i+a][j+b] == 255:
                            neighbors -= 1
                if grid[i][j] == 255:
                    if neighbors == 2 or neighbors == 3:    
                        newGrid[i][j] = 255
                    else:
                        newGrid[i][j] = 0
                if grid[i][j] == 0:
                    if neighbors == 3:
                        newGrid[i][j] = 255
            if i == N-1 and j == 0:
                for a in range(-1,1):
                    for b in range(0,2):
                        if grid[i+a][j+b] == 255:
                            neighbors += 1
                        if a==0 and b==0 and grid[i+a][j+b] == 255:
                            neighbors -= 1
                if grid[i][j] == 255:
                    if neighbors == 2 or neighbors == 3:    
                        newGrid[i][j] = 255
                    else:
                        newGrid[i][j] = 0
                if grid[i][j] == 0:
                    if neighbors == 3:
                        newGrid[i][j] = 255
            if i == N-1 and j == M-1:
                for a in range(-1,1):
                    for b in range(-1,1):
                        if grid[i+a][j+b] == 255:
                            neighbors += 1
                        if a==0 and b==0 and grid[i+a][j+b] == 255:
                            neighbors -= 1
                if grid[i][j] == 255:
                    if neighbors == 2 or neighbors == 3:    
                        newGrid[i][j] = 255
                    else:
                        newGrid[i][j] = 0
                if grid[i][j] == 0:
                    if neighbors == 3:
                        newGrid[i][j] = 255
            if i == 0 and j > 1 and j < M-1:
                for a in range(0,2):
                    for b in range(-1,2):
                        if grid[i+a][j+b] == 255:
                            neighbors += 1
                        if a==0 and b==0 and grid[i+a][j+b] == 255:
                            neighbors -= 1
                if grid[i][j] == 255:
                    if neighbors == 2 or neighbors == 3:    
                        newGrid[i][j] = 255
                    else:
                        newGrid[i][j] = 0
                if grid[i][j] == 0:
                    if neighbors == 3:
                        newGrid[i][j] = 255
            if j == 0 and i > 1 and i < N-1:
                for a in range(-1,2):
                    for b in range(0,2):
                        if grid[i+a][j+b] == 255:
                            neighbors += 1
                        if a==0 and b==0 and grid[i+a][j+b] == 255:
                            neighbors -= 1
                if grid[i][j] == 255:
                    if neighbors == 2 or neighbors == 3:    
                        newGrid[i][j] = 255
                    else:
                        newGrid[i][j] = 0
                if grid[i][j] == 0:
                    if neighbors == 3:
                        newGrid[i][j] = 255
            if i == N-1 and j > 1 and j < M-1:
                for a in range(-1,1):
                    for b in range(-1,2):
                        if grid[i+a][j+b] == 255:
                            neighbors += 1
                        if a==0 and b==0 and grid[i+a][j+b] == 255:
                            neighbors -= 1
                if grid[i][j] == 255:
                    if neighbors == 2 or neighbors == 3:    
                        newGrid[i][j] = 255
                    else:
                        newGrid[i][j] = 0
                if grid[i][j] == 0:
                    if neighbors == 3:
                        newGrid[i][j] = 255
            if j == M-1 and i > 1 and i < N-1:
                for a in range(-1,2):
                    for b in range(-1,1):
                        if grid[i+a][j+b] == 255:
                            neighbors += 1
                        if a==0 and b==0 and grid[i+a][j+b] == 255:
                            neighbors -= 1
                if grid[i][j] == 255:
                    if neighbors == 2 or neighbors == 3:    
                        newGrid[i][j] = 255
                    else:
                        newGrid[i][j] = 0
                if grid[i][j] == 0:
                    if neighbors == 3:
                        newGrid[i][j] = 255
            #Block
            if i == 0 and j== 0:   
                if grid[i][j]==255 and grid[i][j+1]==255 and grid[i+1][j]==255 and grid[i+1][j+1]==255 \
                    and grid[i+2][j] == 0 and grid[i+2][j+1] == 0 and grid[i+2][j+2] == 0 and grid[i][j+2] == 0 \
                        and grid[i+1][j+2] == 0:
                    block+=1
            if i == N-2 and j== 0:   
                if grid[i][j]==255 and grid[i][j+1]==255 and grid[i+1][j]==255 and grid[i+1][j+1]==255 \
                    and grid[i-1][j] == 0 and grid[i-1][j+1] == 0 and grid[i-1][j+2] == 0 and grid[i][j+2] == 0 \
                        and grid[i+1][j+2] == 0:
                    block+=1
            if i == 0 and j== M-2:   
                if grid[i][j]==255 and grid[i][j+1]==255 and grid[i+1][j]==255 and grid[i+1][j+1]==255 \
                    and grid[i+2][j] == 0 and grid[i+2][j+1] == 0 and grid[i+2][j-1] == 0 and grid[i][j-1] == 0 \
                        and grid[i+1][j-1] == 0:
                    block+=1
            if i == N-2 and j== M-2:   
                if grid[i][j]==255 and grid[i][j+1]==255 and grid[i+1][j]==255 and grid[i+1][j+1]==255 \
                    and grid[i-1][j] == 0 and grid[i-1][j+1] == 0 and grid[i-1][j-1] == 0 and grid[i][j-1] == 0 \
                        and grid[i+1][j-1] == 0:
                    block+=1
            if i > 0 and i < N-2 and j == 0:
                if grid[i][j]==255 and grid[i][j+1]==255 and grid[i+1][j]==255 and grid[i+1][j+1]==255 \
                    and grid[i+2][j] == 0 and grid[i+2][j+1] == 0 and grid[i+2][j+2] == 0 and grid[i][j+2] == 0 \
                        and grid[i+1][j+2] == 0 and grid[i-1][j] == 0 and grid[i-1][j+1] == 0 and grid[i-1][j+2] == 0:
                    block+=1
            if i > 0 and i < N-2 and j == M-2:
                if grid[i][j]==255 and grid[i][j+1]==255 and grid[i+1][j]==255 and grid[i+1][j+1]==255 \
                    and grid[i-1][j] == 0 and grid[i-1][j+1] == 0 and grid[i-1][j-1] == 0 and grid[i][j-1] == 0 \
                        and grid[i+1][j-1] == 0 and grid[i+2][j] == 0 and grid[i+2][j+1] == 0 and grid[i+2][j-1]:
                    block+=1
            if j > 0 and j < M-2 and i== 0:
                if grid[i][j]==255 and grid[i][j+1]==255 and grid[i+1][j]==255 and grid[i+1][j+1]==255 \
                    and grid[i+2][j] == 0 and grid[i+2][j+1] == 0 and grid[i+2][j-1] == 0 and grid[i][j-1] == 0 \
                        and grid[i+1][j-1] == 0 and grid[i+2][j+2] == 0 and grid[i][j+2] == 0 and grid[i+1][j+2] == 0:
                    block+=1
            if j > 0 and j < M-2 and i== N-2:
                if grid[i][j]==255 and grid[i][j+1]==255 and grid[i+1][j]==255 and grid[i+1][j+1]==255 \
                    and grid[i-1][j] == 0 and grid[i-1][j+1] == 0 and grid[i-1][j+2] == 0 and grid[i][j+2] == 0 \
                        and grid[i+1][j+2] == 0 and grid[i-1][j-1] == 0 and grid[i][j-1] == 0 and grid[i+1][j-1] == 0:
                    block+=1
            if j > 0 and j < M-2 and i > 0 and i < N-2:
                if grid[i][j]==255 and grid[i][j+1]==255 and grid[i+1][j]==255 and grid[i+1][j+1]==255 \
                    and grid[i-1][j] == 0 and grid[i-1][j+1] == 0 and grid[i-1][j+2] == 0 and grid[i][j+2] == 0 \
                        and grid[i+1][j+2] == 0 and grid[i-1][j-1] == 0 and grid[i][j-1] == 0 and grid[i+1][j-1] == 0 \
                            and grid[i+2][j+2] == 0 and grid[i][j+2] == 0 and grid[i+1][j+2] == 0:
                    block+=1
            

    total = block+beehive+loaf+boat+tub+blinker+toad+beacon+glider+lgSpaceShip

    if total == 0:
        total = 1

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
    document.write("|    Total   | "+str(total)+" |         |\n")
    document.write("--------------------------------\n")

    # update data
    img.set_data(grid)
    grid[:] = newGrid[:]

    return img,

# main() function
def main():
    # Command line args are in sys.argv[1], sys.argv[2] ..
    # sys.argv[0] is the script name itself and can be ignored
    # parse arguments
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life system.py.")
    # TODO: add arguments
    f = open("GameGrid-1.txt", "r")
    g = open("SimulationOutput.txt", "w")

    # set grid size
    size = f.readline().split()
    M = int(size[1])
    N = int(size[0])

    gen = f.readline().split()
    generations = int(gen[0])

    # set animation update interval
    updateInterval = 500

    # declare grid
    grid = np.array([])
    # populate grid with random on/off - more off than on
    #grid = randomGrid(N,M)
    # Uncomment lines to see the "glider" demo
    
    grid = np.zeros(N*M).reshape(N, M)
    #addGlider(1, 1, grid)

    g.write("Simulation at " + str(date.today()) + "\n")
    g.write("Universe size " + str(M) + " x " + str(N) + "\n")


    for line in f:
        cell = line.split()
        grid[int(cell[1])][int(cell[0])] = 255

    # set up animation
    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation='nearest')
    
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