import math


gravity = 9.807
velocity_dampening = -0.85 # calculate later
surface_friction = 0.4

class Physics:

    def get_acceleration(force: float, mass: float):
        return force / mass
    
    # I need to make this rolling friction?
    def get_static_frictional_force(mass: float):
        return surface_friction * gravity * mass
    
    def get_distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
