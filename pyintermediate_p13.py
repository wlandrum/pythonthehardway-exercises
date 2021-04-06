# Object oriented programming using Pygame
# This is the entire blob project
# This also has an inherited class from pyintermediate_pBlob.py

import pygame
import random
from pyintermediate_pBlob import Blob

STARTING_BLUE_BLOBS = 10
STARTING_RED_BLOBS = 3 

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()

# Base class
# Super class
# Parent Class
# All the above are the same that describes the BlueBlob class below
class BlueBlob(Blob):

    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        # Can do this too Blob.__init__(self, color, x_boundary, y_boundary) but will cause problems when doing multiple inheritance
        self.color = BLUE
    
    def move_fast(self):
        self.x += random.randrange(-7, 7)
        self.y += random.randrange(-7, 7)

class RedBlob(Blob):
    
    def __init__(self, color, x_boundary, y_boundary):
        super().__init__(color, x_boundary, y_boundary)
        # Can do this too Blob.__init__(self, color, x_boundary, y_boundary) but will cause problems when doing multiple inheritance
        self.color = RED

    def move_fast(self):
        self.x += random.randrange(-7, 7)
        self.y += random.randrange(-7, 7)

def draw_environment(blob_list):
    game_display.fill(WHITE)

    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move_fast()
            blob.check_bounds()
    pygame.display.update()

def main():
    blue_blobs = dict(enumerate([BlueBlob(BLUE, WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)])) # assign blob an id
    red_blobs = dict(enumerate([RedBlob(RED, WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        draw_environment([blue_blobs, red_blobs])
        clock.tick(60)

if __name__ == '__main__':
    main()