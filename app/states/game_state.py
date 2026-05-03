import pygame
from OpenGL.GL import *
from app.states.base_state import BaseState
from app.world.components.camera import Camera
from app.world.components.transform import Transform
from app.world.prefabs import create_camera
from app.world.scene import Scene
from app.world.systems.camera_input_system import CameraInputSystem
from app.world.systems.camera_view_system import CameraViewSystem
from app.world.systems.render_system import RenderSystem
from app.world.systems.spin_system import SpinSystem


class GameState(BaseState):
    def __init__(self, engine):
        super().__init__(engine)
        self.scene = Scene()
        self.scene.add_system(CameraInputSystem())
        self.scene.add_system(SpinSystem())
        self.camera_view_system = CameraViewSystem()
        self.render_system = RenderSystem(self.engine.renderer)
        self.camera_entity = create_camera(self.scene, position=(0, 0, 3))

    def enter(self):
        self.engine.set_mouse_capture(True)

    def exit(self):
        self.engine.set_mouse_capture(False)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            from app.states.menu_state import MenuState

            self.engine.change_state(MenuState(self.engine, self))

    def update(self, delta_time):
        self.scene.update(delta_time)

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        self.camera_view_system.apply(self.scene)
        self.render_system.render(self.scene)
        self.engine.ui.draw_hud(
            self.engine.width,
            self.engine.height,
            self.scene.get_component(self.camera_entity, Camera),
            self.scene.get_component(self.camera_entity, Transform),
        )
