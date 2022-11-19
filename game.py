import pygame
import os
import time
import random

# Set up pygame window
WIDTH, HEIGHT = 750, 740
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aleja's Space Shooter")

# Load Images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player Ship
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow_small.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BG = pygame.image.load(os.path.join("assets", "background-black.png"))


# Drawing and Getting Main Loop

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
   
    while run:
        clock.tick(FPS)
        
# Check for Events (Check is user quit game window )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

main()
