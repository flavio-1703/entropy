import math
import pygame
from app.world.components.camera import Camera
from app.world.components.input_control import InputControl
from app.world.components.transform import Transform


class CameraInputSystem:
    def update(self, scene, delta_time):
        keys = pygame.key.get_pressed()
        mx, my = pygame.mouse.get_rel()

        for _, transform, camera, input_control in scene.get_components(
            Transform, Camera, InputControl
        ):
            camera.yaw -= mx * camera.mouse_sensitivity
            camera.pitch -= my * camera.mouse_sensitivity
            camera.pitch = max(-89, min(89, camera.pitch))

            speed = input_control.move_speed * delta_time
            yaw_radians = math.radians(-camera.yaw)
            pitch_radians = math.radians(camera.pitch)

            forward_x = math.cos(pitch_radians) * math.sin(yaw_radians)
            forward_y = math.sin(pitch_radians)
            forward_z = -math.cos(pitch_radians) * math.cos(yaw_radians)
            right_x = math.cos(yaw_radians)
            right_z = math.sin(yaw_radians)

            if keys[pygame.K_w]:
                transform.position[0] += forward_x * speed
                transform.position[1] += forward_y * speed
                transform.position[2] += forward_z * speed

            if keys[pygame.K_s]:
                transform.position[0] -= forward_x * speed
                transform.position[1] -= forward_y * speed
                transform.position[2] -= forward_z * speed

            if keys[pygame.K_d]:
                transform.position[0] += right_x * speed
                transform.position[2] += right_z * speed

            if keys[pygame.K_a]:
                transform.position[0] -= right_x * speed
                transform.position[2] -= right_z * speed

            if keys[pygame.K_SPACE]:
                transform.position[1] += speed

            if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]:
                transform.position[1] -= speed
