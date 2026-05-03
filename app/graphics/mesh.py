import ctypes
from OpenGL.GL import *


class Mesh:
    def __init__(self, vertices, indices):
        self.vertex_stride = 5 * ctypes.sizeof(GLfloat)
        self.vertex_count = len(vertices) // 5
        self.index_count = len(indices)

        self.vertices = (GLfloat * len(vertices))(*vertices)
        self.indices = (GLuint * len(indices))(*indices)

        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(
            GL_ARRAY_BUFFER,
            ctypes.sizeof(self.vertices),
            self.vertices,
            GL_STATIC_DRAW,
        )

        self.ebo = glGenBuffers(1)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)
        glBufferData(
            GL_ELEMENT_ARRAY_BUFFER,
            ctypes.sizeof(self.indices),
            self.indices,
            GL_STATIC_DRAW,
        )

    def bind(self):
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, self.ebo)

        glEnableClientState(GL_VERTEX_ARRAY)
        glVertexPointer(3, GL_FLOAT, self.vertex_stride, None)

        glEnableClientState(GL_TEXTURE_COORD_ARRAY)
        glTexCoordPointer(
            2,
            GL_FLOAT,
            self.vertex_stride,
            ctypes.c_void_p(3 * ctypes.sizeof(GLfloat)),
        )

    def draw(self):
        glDrawElements(GL_TRIANGLES, self.index_count, GL_UNSIGNED_INT, None)
