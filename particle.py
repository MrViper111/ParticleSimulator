import pygame
from physics import Physics, gravity, surface_friction, velocity_dampening
import math


class Particle(pygame.Rect):
    
    display: pygame.surface
    position_x: float
    position_y: float
    mass: float
    radius: int
    color: str
    
    def __init__(self, display, position_x, position_y, mass, radius, color):
        self.display = display
        self.position_x = position_x
        self.position_y = position_y
        self.mass = mass
        self.radius = radius
        self.color = color

        self.dt = 0.17

        #self.particle = pygame.draw.circle(display, color, (position_x, position_y), radius)

        self.net_force_x = 0.0
        self.net_force_y = 0.0

        self.acceleration_x = Physics.get_acceleration(self.net_force_x, self.mass) 
        self.acceleration_y = gravity + Physics.get_acceleration(self.net_force_y, self.mass)

        self.velocity_x = 0.0
        self.velocity_y = 0.0

    def handle_collision(self, particles: list['Particle']):

        if self.position_y + self.radius >= 500:
            self.velocity_y *= velocity_dampening
            self.position_y -= 2

        if self.position_y - self.radius <= 0:
            self.velocity_y *= velocity_dampening
            self.position_y += 2

        elif self.position_x - self.radius <= 0 or self.position_x + self.radius >= 500:
            self.velocity_x *= velocity_dampening

        # please optimize this
        for particle in particles:

            if particle is self:
                continue

            distance = Physics.get_distance(self.position_x, self.position_y, particle.position_x, particle.position_y)
            distance_x = particle.position_x - self.position_x
            distance_y = particle.position_y - self.position_y

            print("dist: ", distance)

            if distance <= self.radius + particle.radius:

                #self.velocity_x -= 1 / self.mass * (self.velocity_x * self.mass + particle.velocity_x * particle.mass)
                #self.velocity_y -= 1 / self.mass * (self.velocity_y * self.mass + particle.velocity_y * particle.mass)
                
                print("COLLIDE")
                self.color = "red"
                particle.color = "red"
                return
            else:
                self.color = "black"
                particle.color = "black"

    def update(self, particles: list['Particle']):
        # might have to pre-compute
        self.handle_collision(particles)

        self.velocity_x += self.acceleration_x * self.dt
        self.velocity_y += self.acceleration_y * self.dt

        self.net_force_x = self.mass * (self.velocity_x / self.dt)
        self.net_force_y = self.mass * (self.velocity_y / self.dt)

        self.position_x += self.velocity_x * self.dt
        self.position_y += self.velocity_y * self.dt

        pygame.draw.circle(self.display, self.color, (self.position_x, self.position_y), self.radius)

