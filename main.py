import pygame

from assroid import Assroid
from assroidfield import AssroidField
from constants import *
from player import Player

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

    Player.containers = (updatable, drawable)
    Assroid.containers = (assroids, updatable, drawable)
    AssroidField.containers = (updatable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    field = AssroidField()

    while True:
        screen.fill((0,0,0))


        updatable.update(dt)
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
