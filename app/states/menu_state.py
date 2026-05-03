import pygame
from OpenGL.GL import *
from app.states.base_state import BaseState


class MenuState(BaseState):
    def __init__(self, engine, game_state):
        super().__init__(engine)
        self.game_state = game_state

    def enter(self):
        self.engine.set_mouse_capture(False)

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key in (pygame.K_RETURN, pygame.K_SPACE):
            self.engine.change_state(self.game_state)
        elif event.key == pygame.K_ESCAPE:
            self.engine.running = False

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        self.engine.ui.draw_menu(self.engine.width, self.engine.height)
