## Game of Life hack together using some pygame grid and updates.
# Space to pause animation
# Left Click to set cells alive
# Right Click to set cells dead
# R to reset screen

# Quincy S. 19MAY2020

import pygame
import numpy as np

screen_width = 1080
screen_height = 840
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GREY = (50, 50, 50)
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 10
HEIGHT = 10

# This sets the margin between each cell
MARGIN = 2

rows = screen_height//(HEIGHT+MARGIN)
cols = screen_width//(WIDTH+MARGIN)
print(rows,cols)

grid = np.zeros((cols,rows))


def board_evolve():
    
    new_grid = grid.copy()

    for x in range(0, cols):
        for y in range(0, rows):
            state = grid[x,y]
            neighbors = (grid[x,(y-1)%rows] + grid[x,(y+1)%rows] +
                        grid[(x-1)%cols,y] + grid[(x+1)%cols,y] +
                        grid[(x-1)%cols,(y-1)%rows] + grid[(x+1)%cols,(y-1)%rows] +
                         grid[(x-1)%cols, (y+1)%rows] + grid[(x+1)%cols,(y+1)%rows])
            
            #Rules
            if state == 0 and neighbors == 3: 
                    new_grid[x,y] = 1
            elif state == 1 and (neighbors < 2):
                new_grid[x,y] = 0
            elif state == 1 and (neighbors > 3):
                new_grid[x,y] = 0
            else:
                new_grid[x,y] = state
    return new_grid


# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [screen_width, screen_height]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Game of Life")
 
# Loop until the user clicks the close button.
done = False
running = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # event handling
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            ## evolution pause toggle
            if running == True:
                running = False
            else:
                running = True
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            ## r to reset grid
            grid = np.zeros((cols, rows))
            running = False
            

    if  pygame.mouse.get_pressed()[0]:
        # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
        column = pos[0] // (WIDTH + MARGIN)
        row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
        grid[column,row] = 1
    if pygame.mouse.get_pressed()[2]:
            # User clicks the mouse. Get the position
        pos = pygame.mouse.get_pos()
        # Change the x/y screen coordinates to grid coordinates
        column = pos[0] // (WIDTH + MARGIN)
        row = pos[1] // (HEIGHT + MARGIN)
        # Set that location to one
        grid[column,row] = 0
 
     # Set the screen background
    screen.fill(GREY)
 
    # Draw the grid
    for row in range(rows):
        for column in range(cols):
            color = BLACK
            if grid[column,row] == 1:
                color = WHITE
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    #update evolution
    if running:
        grid = board_evolve()

    # Limit to 20 frames per second it makes the evolution easier to see
    clock.tick(20)
    #draw
    pygame.display.flip()
 
pygame.quit()