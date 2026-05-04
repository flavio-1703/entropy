class Orbit:
    def __init__(self, center=(0, 0, 0), radius=1.0, angular_speed=1.0, angle=0.0):
        self.center = list(center)
        self.radius = radius
        self.angular_speed = angular_speed
        self.angle = angle
