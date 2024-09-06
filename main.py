import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():

    # START GAME PROCESSES
    pygame.init()

    # CREATE SURFACE
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # CREATE CLOCK AND INITIALIZE FRAMERATE TRACKER
    clock = pygame.time.Clock()
    dt = 0

    # GROUPS OF OBJECTS
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    
    # PLACE OBJECTS INTO GROUPS
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # CREATE STARTING OBJECTS
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    ast_field = AsteroidField()

    # MAIN GAME LOOP
    while True:
        
        # CHECK IF USER EXITED WINDOW
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # NUMBER IN BRACKETS = FRAMERATE
        # EVERYTHING IS TIED TO FRAMERATE
        dt = clock.tick(60)/1000

        # CREATE SCREEN
        pygame.Surface.fill(screen, (0,0,0))

        # UPDATE OBJECTS AND DRAW TO SCREEN
        for k in updatable:
            k.update(dt)
        for k in drawable:
            k.draw(screen)

        # CHECK COLLISIONS
        for k in asteroids:
            if k.check_collision(player1):
                print("Game over!")
                sys.exit()
            for s in shots:
                if k.check_collision(s):
                    k.split()
                    s.kill()
            
                
        # DISPLAY EVERYTHING
        pygame.display.flip()
        
# THIS FILE WILL ONLY EXECUTE IF CALLED DIRECTLY
if __name__ == "__main__":
    main()