from OpenGL.GL import *


class Renderer:
    def draw(self, entity):
        entity.texture.bind()
        entity.mesh.bind()
        entity.mesh.draw()
