import pygame
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective
from app.core.camera import Camera
from app.core.input_controller import InputController
from app.core.renderer import Renderer
from app.core.ui import UIOverlay
from app.world.entity import Entity
from app.world.scene import Scene


class Engine:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        pygame.mouse.get_rel()
        pygame.mouse.set_pos(400, 300)
        self.screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.OPENGL)
        self.clock = pygame.time.Clock()

        glViewport(0, 0, 800, 600)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, 800 / 600, 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)

        glEnable(GL_DEPTH_TEST)
        glEnable(GL_TEXTURE_2D)
        glClearColor(0.02, 0.02, 0.05, 1.0)

        self.renderer = Renderer()
        self.scene = Scene()
        self.camera = Camera()
        self.input_controller = InputController(self.camera)
        self.ui = UIOverlay()
        self.running = True

    def run(self):
        self.delta_time = 0
        while self.running:
            self.delta_time = self.clock.tick(60) / 1000.0
            
            self.handle_events()
            self.input_controller.process_frame(self.delta_time)
            self.update()
            self.render()
            pygame.display.flip()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def update(self):
        for e in self.scene.entities:
            e.transform.rotation[1] += 90 * self.delta_time

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.camera.apply()

        for e in self.scene.entities:
            glPushMatrix()

            t = e.transform

            glTranslatef(*t.position)
            glRotatef(t.rotation[0], 1, 0, 0)
            glRotatef(t.rotation[1], 0, 1, 0)
            glRotatef(t.rotation[2], 0, 0, 1)
            glScalef(*t.scale)

            self.renderer.draw(e)

            glPopMatrix()

        self.ui.draw(800, 600, self.camera)

    def set_scene(self, mesh, texture):
        self.scene.add(Entity(mesh, texture))

    def add_entity(self, mesh, texture, position=None, rotation=None, scale=None):
        entity = Entity(mesh, texture)

        if position is not None:
            entity.transform.position = list(position)
        if rotation is not None:
            entity.transform.rotation = list(rotation)
        if scale is not None:
            entity.transform.scale = list(scale)

        self.scene.add(entity)
        return entity
