import pygame
from OpenGL.GL import *

class Camera:
    def __init__(self):
        self.position = [0, 0, 3]

        self.yaw = 0    # left/right
        self.pitch = 0  # up/down

        self.mouse_sensitivity = 0.05
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)

    def apply(self):
        glLoadIdentity()
        glRotatef(-self.pitch, 1, 0, 0)
        glRotatef(-self.yaw, 0, 1, 0)
        glTranslatef(-self.position[0],
                     -self.position[1],
                     -self.position[2])
