from OpenGL.GL import *
from app.world.components.mesh_renderer import MeshRenderer
from app.world.components.transform import Transform


class RenderSystem:
    def __init__(self, renderer):
        self.renderer = renderer

    def render(self, scene, show_euclidean_guides=False):
        if show_euclidean_guides:
            self._draw_euclidean_guides()

        for _, transform, mesh_renderer in scene.get_components(Transform, MeshRenderer):
            glPushMatrix()
            glTranslatef(*transform.position)
            glRotatef(transform.rotation[0], 1, 0, 0)
            glRotatef(transform.rotation[1], 0, 1, 0)
            glRotatef(transform.rotation[2], 0, 0, 1)
            glScalef(*transform.scale)
            self.renderer.draw(mesh_renderer.mesh, mesh_renderer.texture)
            glPopMatrix()

    def _draw_euclidean_guides(self):
        glDisable(GL_TEXTURE_2D)
        glLineWidth(1.0)

        glColor4f(0.2, 0.28, 0.38, 0.65)
        glBegin(GL_LINES)
        grid_min = -6
        grid_max = 6
        for index in range(grid_min, grid_max + 1):
            glVertex3f(grid_min, 0, index)
            glVertex3f(grid_max, 0, index)
            glVertex3f(index, 0, grid_min)
            glVertex3f(index, 0, grid_max)
        glEnd()

        glLineWidth(3.0)
        glBegin(GL_LINES)

        glColor3f(0.95, 0.25, 0.25)
        glVertex3f(0, 0, 0)
        glVertex3f(3.5, 0, 0)

        glColor3f(0.3, 0.9, 0.4)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 3.5, 0)

        glColor3f(0.3, 0.55, 0.95)
        glVertex3f(0, 0, 0)
        glVertex3f(0, 0, 3.5)

        glEnd()

        glBegin(GL_TRIANGLES)

        glColor3f(0.95, 0.25, 0.25)
        glVertex3f(3.5, 0, 0)
        glVertex3f(3.2, 0.12, 0)
        glVertex3f(3.2, -0.12, 0)

        glColor3f(0.3, 0.9, 0.4)
        glVertex3f(0, 3.5, 0)
        glVertex3f(0.12, 3.2, 0)
        glVertex3f(-0.12, 3.2, 0)

        glColor3f(0.3, 0.55, 0.95)
        glVertex3f(0, 0, 3.5)
        glVertex3f(0.12, 0, 3.2)
        glVertex3f(-0.12, 0, 3.2)

        glEnd()

        glLineWidth(1.0)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glEnable(GL_TEXTURE_2D)
