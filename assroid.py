import pygame
import random
from circleshape import CircleShape
from constants import *

class Assroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2) # 2 width

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASSROID_MIN_RADIUS:
            return

        rand_angle = random.uniform(20,50)
        a = self.velocity.rotate(rand_angle)
        b = self.velocity.rotate(-rand_angle)
        new_radius = self.radius - ASSROID_MIN_RADIUS

        new_1 = Assroid(self.position.x, self.position.y, new_radius)
        new_1.velocity = a * 1.2
        new_2 = Assroid(self.position.x, self.position.y, new_radius)
        new_2.velocity = a * 1.2
        