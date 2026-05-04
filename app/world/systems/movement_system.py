from app.world.components.transform import Transform
from app.world.components.velocity import Velocity


class MovementSystem:
    def update(self, scene, delta_time):
        for _, transform, velocity in scene.get_components(Transform, Velocity):
            for axis in range(3):
                transform.position[axis] += (
                    velocity.direction[axis] * velocity.speed * delta_time
                )
