from app.graphics.geometry import create_sphere
from app.graphics.mesh import Mesh
from app.graphics.texture import Texture
from app.world.prefabs import create_renderable, create_spinning_body


class Planet:
    _shared_mesh = None
    texture_path = None
    default_position = (0, 0, 0)
    default_rotation = (0, 0, 0)
    default_size = 1.0
    default_spin_speed = (0, 0, 0)

    scale_to_size = 5.0

    def __init__(
        self,
        position=None,
        rotation=None,
        size=None,
        scale=None,
        spin_speed=None,
    ):
        if self.texture_path is None:
            raise NotImplementedError(
                f"{type(self).__name__} must define a texture_path."
            )

        self.position = position if position is not None else self.default_position
        self.rotation = rotation if rotation is not None else self.default_rotation
        self.size = size if size is not None else self.default_size
        self.scale = scale if scale is not None else self._uniform_scale(self.size)
        self.spin_speed = (
            spin_speed if spin_speed is not None else self.default_spin_speed
        )

    def _uniform_scale(self, size):
        return (size, size, size)

    @classmethod
    def get_mesh(cls):
        if Planet._shared_mesh is None:
            sphere_vertices, sphere_indices = create_sphere()
            Planet._shared_mesh = Mesh(sphere_vertices, sphere_indices)
        return Planet._shared_mesh

    def create(self, scene):
        mesh = self.get_mesh()
        texture = Texture(self.texture_path)
        if any(self.spin_speed):
            return create_spinning_body(
                scene,
                mesh,
                texture,
                position=self.position,
                rotation=self.rotation,
                scale=self.scale,
                rotation_speed=self.spin_speed,
            )

        return create_renderable(
            scene,
            mesh,
            texture,
            position=self.position,
            rotation=self.rotation,
            scale=self.scale,
        )


class Sun(Planet):
    texture_path = "assets/sun.jpg"
    default_spin_speed = (0, 90, 0)
    default_size = 1

class Mercury(Planet): 
    texture_path = "assets/mercury.jpg"
    default_size = 0.15
    default_spin_speed = (0, 18, 0)

class Venus(Planet): 
    texture_path = "assets/venus.jpg"
    default_size = 0.22
    default_spin_speed = (0, 10, 0)

class Earth(Planet):
    texture_path = "assets/earth.jpg"
    default_size = 0.24
    default_spin_speed = (0, 20, 0)

class Mars(Planet):
    texture_path = "assets/mars.jpg"
    default_size = 0.20
    default_spin_speed = (0, 16, 0)

class Jupiter(Planet): 
    texture_path = "assets/jupiter.jpg"
    default_size = 0.70
    default_spin_speed = (0, 26, 0)

class Saturn(Planet): 
    texture_path = "assets/saturn.jpg"
    default_size = 0.60
    default_spin_speed = (0, 24, 0)

class Uranus(Planet): 
    texture_path = "assets/uranus.jpg"
    default_size = 0.42
    default_spin_speed = (0, 14, 0)

class Neptune(Planet): 
    texture_path = "assets/neptune.jpg"
    default_size = 0.40
    default_spin_speed = (0, 15, 0)