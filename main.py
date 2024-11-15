import sys
import pygame
from constants import*
from player import Player
from asteroid import*
from asteroidfield import*
from shot import*


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Shot.containers = (shots, updatable, drawable)

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                print("Game Over!")
                sys.exit()
        
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # limit framerate to 60 FPS
        dt = clock.tick(60) / 1000





if __name__ == "__main__":
    main()