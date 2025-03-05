import pygame
import sys

from assroid import Assroid
from assroidfield import AssroidField
from constants import *
from player import Player
from shot import Shot

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    assroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Assroid.containers = (assroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AssroidField.containers = updatable


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AssroidField()

    while True:
        screen.fill((0,0,0))


        updatable.update(dt)
        
        for assroid in assroids:
            if player.check_collide(assroid):
                print("Game over!")
                sys.exit()

        for assroid in assroids:
            for shot in shots:
                if assroid.check_collide(shot):
                    shot.kill()
                    assroid.kill()

        for obj in drawable:
            obj.draw(screen)


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        delta = clock.tick(60)
        dt = delta / 1000

        


if __name__ == "__main__":
    main()
