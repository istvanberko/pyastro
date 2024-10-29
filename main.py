# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main ():
    pygame.init()
    screen = pygame.display.set_mode(size = (SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    print("Updatable group contents:", updatable.sprites())
    print("Drawable group contents:", drawable.sprites())

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        for tobj in updatable:
            tobj.update(dt)
        #player.update(dt)
        screen.fill("black")

        for tobj in drawable:
            tobj.draw(screen)
        #player.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()
