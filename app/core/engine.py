import pygame
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
from app.core.renderer import Renderer
from app.core.ui import UIOverlay


class Engine:
    def __init__(self):
        pygame.init()
        self.width = 1920
        self.height = 1080
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.DOUBLEBUF | pygame.OPENGL)
        self.clock = pygame.time.Clock()
        self.state = None

        glViewport(0, 0, self.width, self.height)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, self.width / self.height, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glClearColor(0.02, 0.02, 0.05, 1.0)

        self.renderer = Renderer()
        self.ui = UIOverlay()
        self.running = True

    def change_state(self, new_state):
        if self.state is not None:
            self.state.exit()

        self.state = new_state
        self.state.enter()

    def set_mouse_capture(self, enabled):
        pygame.mouse.set_visible(not enabled)
        pygame.event.set_grab(enabled)
        pygame.mouse.get_rel()

    def run(self):
        self.delta_time = 0
        while self.running:
            self.delta_time = self.clock.tick(60) / 1000.0
            
            self.handle_events()
            if self.state is not None:
                self.state.update(self.delta_time)
                self.state.render()
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif self.state is not None:
                self.state.handle_event(event)
