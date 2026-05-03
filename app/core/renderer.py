from OpenGL.GL import *


class Renderer:
    def draw(self, mesh, texture):
        texture.bind()
        mesh.bind()
        mesh.draw()
