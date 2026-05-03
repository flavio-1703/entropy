import pygame
from OpenGL.GL import *


class UIOverlay:
    def __init__(self):
        pygame.font.init()
        self.font = pygame.font.SysFont("consolas", 18)
        self.title_font = pygame.font.SysFont("consolas", 36)

    def draw_hud(self, width, height, camera, transform):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, width, height, 0, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glDisable(GL_DEPTH_TEST)
        glDisable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        self._draw_panel(width, height)
        self._draw_crosshair(width, height)
        self._draw_text(camera, transform)

        glDisable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_DEPTH_TEST)

        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

    def draw_menu(self, width, height):
        self._begin_overlay(width, height)

        glColor4f(0.01, 0.02, 0.04, 0.92)
        glBegin(GL_QUADS)
        glVertex2f(0, 0)
        glVertex2f(width, 0)
        glVertex2f(width, height)
        glVertex2f(0, height)
        glEnd()

        self._draw_centered_text(width / 2, height / 2 - 60, "ENTROPY", self.title_font)
        self._draw_centered_text(width / 2, height / 2 - 8, "Press Enter to Start", self.font)
        self._draw_centered_text(width / 2, height / 2 + 18, "Press Esc to Quit", self.font)

        self._end_overlay()

    def _begin_overlay(self, width, height):
        glMatrixMode(GL_PROJECTION)
        glPushMatrix()
        glLoadIdentity()
        glOrtho(0, width, height, 0, -1, 1)

        glMatrixMode(GL_MODELVIEW)
        glPushMatrix()
        glLoadIdentity()

        glDisable(GL_DEPTH_TEST)
        glDisable(GL_TEXTURE_2D)
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    def _end_overlay(self):
        glDisable(GL_BLEND)
        glEnable(GL_TEXTURE_2D)
        glEnable(GL_DEPTH_TEST)

        glPopMatrix()
        glMatrixMode(GL_PROJECTION)
        glPopMatrix()
        glMatrixMode(GL_MODELVIEW)

    def _draw_panel(self, width, height):
        panel_width = 260
        panel_height = 86
        x = 16
        y = 16

        glColor4f(0.03, 0.05, 0.08, 0.8)
        glBegin(GL_QUADS)
        glVertex2f(x, y)
        glVertex2f(x + panel_width, y)
        glVertex2f(x + panel_width, y + panel_height)
        glVertex2f(x, y + panel_height)
        glEnd()

        glColor4f(0.45, 0.8, 0.95, 0.9)
        glBegin(GL_LINE_LOOP)
        glVertex2f(x, y)
        glVertex2f(x + panel_width, y)
        glVertex2f(x + panel_width, y + panel_height)
        glVertex2f(x, y + panel_height)
        glEnd()

    def _draw_crosshair(self, width, height):
        cx = width / 2
        cy = height / 2
        size = 8

        glColor4f(0.92, 0.95, 0.98, 0.85)
        glBegin(GL_LINES)
        glVertex2f(cx - size, cy)
        glVertex2f(cx + size, cy)
        glVertex2f(cx, cy - size)
        glVertex2f(cx, cy + size)
        glEnd()

    def _draw_text(self, camera, transform):
        lines = [
            "Entropy Debug HUD",
            "Move: WASD   Look: Mouse",
            f"Pos: {transform.position[0]: .2f} {transform.position[1]: .2f} {transform.position[2]: .2f}",
            f"Yaw/Pitch: {camera.yaw: .1f} / {camera.pitch: .1f}",
        ]

        y = 24
        for line in lines:
            self._draw_text_line(28, y, line)
            y += 18

    def _draw_text_line(self, x, y, text):
        self._draw_text_surface(x, y, text, self.font)

    def _draw_centered_text(self, center_x, y, text, font):
        surface = font.render(text, True, (235, 244, 252), (0, 0, 0, 0))
        x = center_x - surface.get_width() / 2
        self._draw_surface(surface, x, y)

    def _draw_text_surface(self, x, y, text, font):
        surface = font.render(text, True, (235, 244, 252), (0, 0, 0, 0))
        self._draw_surface(surface, x, y)

    def _draw_surface(self, surface, x, y):
        text_data = pygame.image.tostring(surface, "RGBA", True)
        glColor4f(1.0, 1.0, 1.0, 1.0)
        glWindowPos2d(x, y + surface.get_height())
        glDrawPixels(
            surface.get_width(),
            surface.get_height(),
            GL_RGBA,
            GL_UNSIGNED_BYTE,
            text_data,
        )
