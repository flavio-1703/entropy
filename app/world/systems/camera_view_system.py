from OpenGL.GL import *
from app.world.components.camera import Camera
from app.world.components.transform import Transform


class CameraViewSystem:
    def apply(self, scene):
        active_camera = scene.find_first(Camera, Transform, predicate=lambda camera, _: camera.active)
        if active_camera is None:
            glLoadIdentity()
            return

        _, camera, transform = active_camera
        glLoadIdentity()
        glRotatef(-camera.pitch, 1, 0, 0)
        glRotatef(-camera.yaw, 0, 1, 0)
        glTranslatef(-transform.position[0], -transform.position[1], -transform.position[2])
