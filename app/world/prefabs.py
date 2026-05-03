from app.world.components.camera import Camera
from app.world.components.input_control import InputControl
from app.world.components.mesh_renderer import MeshRenderer
from app.world.components.spin import Spin
from app.world.components.transform import Transform


def create_camera(scene, position=(0, 0, 3), yaw=0.0, pitch=0.0, move_speed=5.0):
    entity = scene.create_entity()
    scene.add_component(entity, Transform(position=position))
    scene.add_component(entity, Camera(yaw=yaw, pitch=pitch))
    scene.add_component(entity, InputControl(move_speed=move_speed))
    return entity


def create_renderable(
    scene,
    mesh,
    texture,
    position=None,
    rotation=None,
    scale=None,
):
    entity = scene.create_entity()
    scene.add_component(entity, Transform(position, rotation, scale))
    scene.add_component(entity, MeshRenderer(mesh, texture))
    return entity


def create_spinning_body(
    scene,
    mesh,
    texture,
    position=None,
    rotation=None,
    scale=None,
    rotation_speed=(0, 0, 0),
):
    entity = create_renderable(scene, mesh, texture, position, rotation, scale)
    scene.add_component(entity, Spin(rotation_speed))
    return entity
