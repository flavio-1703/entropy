from app.world.components.spin import Spin
from app.world.components.transform import Transform


class SpinSystem:
    def update(self, scene, delta_time):
        for _, transform, spin in scene.get_components(Transform, Spin):
            for axis in range(3):
                transform.rotation[axis] += spin.speed[axis] * delta_time
