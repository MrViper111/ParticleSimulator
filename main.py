import pygame
import math

from utils import get_particles, append_each
from particle import Particle


pygame.init()
screen = pygame.display.set_mode([500, 500])
clock = pygame.time.Clock()

# having multiple types of particles is fine
particles = get_particles(
    screen=screen,
    amount=10,
    spacing=30,
    radius=10,
    mass=1
)

manual_vertical_force = 20
manual_horizontal_force = 5

running = True
while running:
    dt = clock.tick(70) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # TODO make these actual forces
        # TODO have onclick events that attract and repulse
        if event.type == pygame.KEYDOWN:
            for particle in particles:
                if event.key == pygame.K_UP:
                    particle.velocity_y -= manual_vertical_force / particle.mass
                elif event.key == pygame.K_DOWN:
                    particle.velocity_y += manual_vertical_force / particle.mass
                elif event.key == pygame.K_RIGHT:
                    particle.velocity_x += manual_horizontal_force / particle.mass
                elif event.key == pygame.K_LEFT:
                    particle.velocity_x -= manual_horizontal_force / particle.mass

    screen.fill((255, 255, 255))

    for particle in particles:
        particle.update(particles)
    
    pygame.display.flip()
