import math

from app.world.components.orbit import Orbit
from app.world.components.transform import Transform


class OrbitSystem:
    def update(self, scene, delta_time):
        for _, transform, orbit in scene.get_components(Transform, Orbit):
            orbit.angle += orbit.angular_speed * delta_time
            transform.position[0] = orbit.center[0] + orbit.radius * math.cos(orbit.angle)
            transform.position[1] = orbit.center[1]
            transform.position[2] = orbit.center[2] + orbit.radius * math.sin(orbit.angle)
