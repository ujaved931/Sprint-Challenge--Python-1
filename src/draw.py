import pygame #TODO:  Fix intellisense
import random
import sys

from pygame.math import Vector2

from ball import GameBall
from block import KineticBlock, Paddle, RowsOfBlock

SCREEN_SIZE = [400, 800]
BACKGROUND_COLOR = [255, 255, 255]

def debug_create_objects(object_list):
    kinetic = GameBall(1, object_list, SCREEN_SIZE, 
                                    Vector2(random.randint(20, SCREEN_SIZE[0] - 20), random.randint(20, SCREEN_SIZE[1] - 20)),
                                    Vector2(4*random.random() - 2, 4*random.random() - 2),
                                    [255, 10, 0], 20)
    object_list.append(kinetic)

    paddle = Paddle(Vector2(200, 750), 100, 20, [0, 255, 0])
    object_list.append(paddle)
    
    block = RowsOfBlock(Vector2(40, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(130, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(220, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(310, 100), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(400, 100), 80, 30, [0, 255, 0])
    object_list.append(block)
    block = RowsOfBlock(Vector2(40, 60), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(130, 60), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(220, 60), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(310, 60), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(400, 60), 80, 30, [0, 255, 0])
    object_list.append(block)
    block = RowsOfBlock(Vector2(40, 140), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(130, 140), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(220, 140), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(310, 140), 80, 30, [0, 255, 0])
    object_list.append(block)

    block = RowsOfBlock(Vector2(400, 140), 80, 30, [0, 255, 0])
    object_list.append(block)

    
def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
 
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
 
    object_list = [] # list of objects of all types in the toy
    
    debug_create_objects(object_list)
 
    while True: # TODO:  Create more elegant condition for loop
        left = False
        right = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        #TODO:  Feed input variables into update for objects that need it.
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            direction = "l"
        if keys[pygame.K_RIGHT]:
            direction = "r"
        for object in object_list:
            if isinstance(object, Paddle):
                object.move_paddle(direction)
            object.update()
            object.check_collision()
 
        # Draw Updates
        screen.fill(BACKGROUND_COLOR)
        for ball in object_list:
            ball.draw(screen, pygame)
 
        clock.tick(60)
        pygame.display.flip()
 
    # Close everything down
    pygame.quit()
 
if __name__ == "__main__":
    main()
