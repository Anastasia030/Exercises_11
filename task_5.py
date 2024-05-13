import random
import pygame
import math


class Molecule:
    """
    The class of the molecule
    """
    all_molecules = []

    def __init__(self, x, y, radius, color, speed):
        """
        Initializes a molecule with given attributes.

        :param x: int, x-coordinate of the molecule's center
        :param y: int, y-coordinate of the molecule's center
        :param radius: int, radius of the molecule
        :param color: tuple, color code of the molecule
        :param speed: float, speed of the molecule
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = speed
        self.primary_direction = random.uniform(0, 2 * math.pi)
        self.dx = self.speed * math.cos(self.primary_direction)
        self.dy = self.speed * math.sin(self.primary_direction)

    def appearance(self, screen):
        """
        Draws the appearance of the molecule on the screen.

        :param screen: the surface to draw on
        """
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def direction_movement(self, movement_x, movement_y):
        """
        Adjusts the movement direction of the molecule.

        :param movement_x: float, amount of movement along the x-axis
        :param movement_y: float, amount of movement along the y-axis
        """
        self.dx += movement_x
        self.dy += movement_y

    def movement(self):
        """
        Updates the position of the molecule based on its current speed and direction.
        """
        self.x += self.dx
        self.y += self.dy

        if self.x < self.radius or self.x > 800 - self.radius:
            self.dx *= -1
        if self.y < self.radius or self.y > 500 - self.radius:
            self.dy *= -1
