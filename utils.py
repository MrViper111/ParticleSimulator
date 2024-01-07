import pygame
from particle import Particle


def get_particles(screen: pygame.display, amount: int, spacing: int, radius: int, mass: float) -> list[Particle]:
    offset = (500 - (amount * (spacing + (radius) * 2))) / 2
    return [Particle(screen, offset + (i * spacing), 10, mass, radius, "black") for i in range(amount)]
    # 3, 30, 8
    # 500 - 114... 192

def append_each(list1: list, list2: list) -> None:
    for element in list1:
        list2.append(element)
