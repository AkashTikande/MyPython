#GAME DOES WORK'S USING ARROWS KEYS.
import pygame
import random

# Initialize Pygame
pygame.init()

   # Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Simple Game")

# Set up colors
BLACK = (0, 0, 0)
RED= (255, 255, 255)

# Set up player
player = pygame.Rect(400, 300, 50, 50)

# Set up clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 20
    if keys[pygame.K_RIGHT]:
        player.x += 20
    if keys[pygame.K_UP]:
        player.y -= 20
    if keys[pygame.K_DOWN]:
        player.y += 20          # defines  block speed in terms of pix
        # ( by how many pixels does the block moves in given direction )
    clock.tick(600)              # assigned duel clock tick ,( observe speed and pixel move difference)


    # add a button to switch in between both speed modes ( fast and slow )
    # use while loop to switch betwwn 2 speeds



    if keys[pygame.K_END]:
        player.x -= 10         # VARIABLE SPEED BY ASSIGNING LESS SPEED
    if keys[pygame.K_HOME]:
        player.x += 10
    if keys[pygame.K_PAUSE]:
        player.y -= 10
    if keys[pygame.K_SPACE]:
        player.y += 10
    pygame.draw.rect(screen,RED, player)

    pygame.display.flip()
    clock.tick(30)              # control the speed of block

pygame.quit()

#This code sets up a simple game using Pygame where you control a player rectangle using the arrow keys.
#The player rectangle can move left, right, up, and down within the game window (800x600 pixels).
#When you press the arrow keys, the player rectangle moves accordingly.

#The game loop continues running until you close the game window.
#The player rectangle is drawn on the screen in white color against a black background.

#To run this code and see the output,
#you would need to have Pygame installed on your system.
#When you run the code, a Pygame window will open,
#and you can control the movement of the player rectangle using the arrow keys.#

#If you encounter any issues or errors while running this code,
#please let me know so I can assist you further.#