import math
import pygame


class InputController:
    def __init__(self, camera, move_speed=5.0):
        self.camera = camera
        self.move_speed = move_speed

    def process_frame(self, delta_time):
        self._handle_mouse()
        self._handle_keyboard(delta_time)

    def _handle_keyboard(self, delta_time):
        keys = pygame.key.get_pressed()
        speed = self.move_speed * delta_time

        forward_x = math.sin(math.radians(self.camera.yaw))
        forward_z = -math.cos(math.radians(self.camera.yaw))

        right_x = math.cos(math.radians(self.camera.yaw))
        right_z = math.sin(math.radians(self.camera.yaw))

        if keys[pygame.K_w]:
            self.camera.position[0] += forward_x * speed
            self.camera.position[2] += forward_z * speed

        if keys[pygame.K_s]:
            self.camera.position[0] -= forward_x * speed
            self.camera.position[2] -= forward_z * speed

        if keys[pygame.K_d]:
            self.camera.position[0] += right_x * speed
            self.camera.position[2] += right_z * speed

        if keys[pygame.K_a]:
            self.camera.position[0] -= right_x * speed
            self.camera.position[2] -= right_z * speed

    def _handle_mouse(self):
        mx, my = pygame.mouse.get_rel()

        self.camera.yaw += mx * self.camera.mouse_sensitivity
        self.camera.pitch -= my * self.camera.mouse_sensitivity
        self.camera.pitch = max(-89, min(89, self.camera.pitch))
