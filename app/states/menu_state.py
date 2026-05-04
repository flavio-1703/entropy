import pygame
from OpenGL.GL import *
from app.states.base_state import BaseState


class MenuState(BaseState):
    def __init__(self, engine, spaces, selected_index=0):
        super().__init__(engine)
        self.spaces = spaces
        self.selected_index = selected_index

    def enter(self):
        self.engine.set_mouse_capture(False)

    def handle_event(self, event):
        if event.type != pygame.KEYDOWN:
            return

        if event.key in (pygame.K_UP, pygame.K_w):
            self.selected_index = (self.selected_index - 1) % len(self.spaces)
        elif event.key in (pygame.K_DOWN, pygame.K_s):
            self.selected_index = (self.selected_index + 1) % len(self.spaces)
        if event.key in (pygame.K_RETURN, pygame.K_SPACE):
            self.engine.change_state(self.spaces[self.selected_index][1])
        elif event.key == pygame.K_ESCAPE:
            self.engine.running = False

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        options = [label for label, _ in self.spaces]
        self.engine.ui.draw_menu(
            self.engine.width,
            self.engine.height,
            options,
            self.selected_index,
        )
