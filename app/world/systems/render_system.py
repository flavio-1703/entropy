from OpenGL.GL import *
from app.world.components.mesh_renderer import MeshRenderer
from app.world.components.transform import Transform


class RenderSystem:
    def __init__(self, renderer):
        self.renderer = renderer

    def render(self, scene):
        for _, transform, mesh_renderer in scene.get_components(Transform, MeshRenderer):
            glPushMatrix()
            glTranslatef(*transform.position)
            glRotatef(transform.rotation[0], 1, 0, 0)
            glRotatef(transform.rotation[1], 0, 1, 0)
            glRotatef(transform.rotation[2], 0, 0, 1)
            glScalef(*transform.scale)
            self.renderer.draw(mesh_renderer.mesh, mesh_renderer.texture)
            glPopMatrix()
