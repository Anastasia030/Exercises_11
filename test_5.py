from task_5 import Molecule
import pygame
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

number_molecules = int(input('Enter the number of molecules: '))
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

for _ in range(number_molecules):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(0, SCREEN_HEIGHT)
    radius = random.randint(5, 20)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    speed = random.uniform(1, 3)
    Molecule.all_molecules.append(Molecule(x, y, radius, color, speed))

clock = pygame.time.Clock()
run = True
while run:
    screen.fill('white')

    for number, molecule_1 in enumerate(Molecule.all_molecules):
        for molecule_2 in Molecule.all_molecules[number+1:]:
            dx = molecule_2.x - molecule_1.x
            dy = molecule_2.y - molecule_1.y
            distance = math.sqrt(dx ** 2 + dy ** 2)
            if distance < molecule_1.radius + molecule_2.radius:
                overlap = (molecule_1.radius + molecule_2.radius) - distance
                angle = math.atan2(dy, dx)
                force_x = 0.1 * overlap * math.cos(angle)
                force_y = 0.1 * overlap * math.sin(angle)
                molecule_1.direction_movement(-force_x, -force_y)
                molecule_2.direction_movement(force_x, force_y)

    for molecule in Molecule.all_molecules:
        molecule.movement()
        molecule.appearance(screen)

    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()