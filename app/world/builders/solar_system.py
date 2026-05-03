from app.graphics.geometry import create_sphere
from app.graphics.mesh import Mesh
from app.graphics.texture import Texture
from app.states.game_state import GameState
from app.world.prefabs import create_renderable, create_spinning_body


def build_solar_system_game_state(engine):
    game_state = GameState(engine)

    sphere_vertices, sphere_indices = create_sphere()

    sun_mesh = Mesh(sphere_vertices, sphere_indices)
    sun_texture = Texture("assets/sun.jpg")

    earth_mesh = Mesh(sphere_vertices, sphere_indices)
    earth_texture = Texture("assets/earth.jpg")

    mars_mesh = Mesh(sphere_vertices, sphere_indices)
    mars_texture = Texture("assets/mars.jpg")

    create_renderable(game_state.scene, sun_mesh, sun_texture, position=(0, 0, 0))
    create_spinning_body(
        game_state.scene,
        earth_mesh,
        earth_texture,
        position=(-1.5, 0, 0),
        rotation_speed=(0, 90, 0),
    )
    create_spinning_body(
        game_state.scene,
        mars_mesh,
        mars_texture,
        position=(1.5, 0, 0),
        rotation_speed=(0, 90, 0),
    )

    return game_state
