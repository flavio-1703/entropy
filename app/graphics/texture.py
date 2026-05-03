from OpenGL.GL import *
from PIL import Image


class Texture:
    def __init__(self, path):
        img = Image.open(path)
        img = img.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = img.convert("RGBA").tobytes()

        self.id = glGenTextures(1)
        glBindTexture(GL_TEXTURE_2D, self.id)

        glTexImage2D(GL_TEXTURE_2D,
                     0,
                     GL_RGBA,
                     img.width,
                     img.height,
                     0,
                     GL_RGBA,
                     GL_UNSIGNED_BYTE,
                     img_data)

        glTexParameteri(GL_TEXTURE_2D,
                         GL_TEXTURE_MIN_FILTER,
                         GL_LINEAR)

        glTexParameteri(GL_TEXTURE_2D,
                         GL_TEXTURE_MAG_FILTER,
                         GL_LINEAR)

        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    def bind(self):
        glBindTexture(GL_TEXTURE_2D, self.id)
