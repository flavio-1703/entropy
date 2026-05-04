from app.graphics.geometry import create_sphere
from app.graphics.mesh import Mesh
from app.graphics.texture import Texture
from app.states.game_state import GameState
from app.world.components.orbit import Orbit
from app.world.components.velocity import Velocity
from app.world.prefabs import create_renderable, create_spinning_body


def build_euclidean_space_game_state(engine):
    game_state = GameState(engine)
    game_state.show_euclidean_guides = True

    sphere_vertices, sphere_indices = create_sphere()

    sphere_mesh = Mesh(sphere_vertices, sphere_indices)

    sun_texture = Texture("assets/sun.jpg")
    earth_texture = Texture("assets/earth.jpg")
    mars_texture = Texture("assets/mars.jpg")

    lattice_points = [
        ((0, 0, 0), sun_texture, (0.45, 0.45, 0.45)),
        ((2.0, 0, 0), earth_texture, (0.3, 0.3, 0.3)),
        ((0, 0, -2.0), mars_texture, (0.3, 0.3, 0.3)),
    ]

    center_entity = create_spinning_body(
        game_state.scene,
        sphere_mesh,
        lattice_points[0][1],
        position=lattice_points[0][0],
        rotation=[0, 1, 0],
        scale=lattice_points[0][2],
        rotation_speed=(0, 20, 0),
    )

    drifting_entity = create_spinning_body(
        game_state.scene,
        sphere_mesh,
        lattice_points[1][1],
        position=lattice_points[1][0],
        rotation=[0, 1, 0],
        scale=lattice_points[1][2],
        rotation_speed=(0, 20, 0),
    )
    game_state.scene.add_component(
        drifting_entity,
        Velocity(direction=(-1, 0.25, 0), speed=0.75),
    )

    orbiting_entity = create_spinning_body(
        game_state.scene,
        sphere_mesh,
        lattice_points[2][1],
        position=lattice_points[2][0],
        rotation=[0, 1, 0],
        scale=lattice_points[2][2],
        rotation_speed=(0, 20, 0),
    )
    game_state.scene.add_component(
        orbiting_entity,
        Orbit(center=(0, 0, 0), radius=2.0, angular_speed=1.25, angle=-1.5708),
    )

    for position, texture, scale in [
        ((-2.0, 0, 0), earth_texture, (0.3, 0.3, 0.3)),
        ((0, 2.0, 0), mars_texture, (0.3, 0.3, 0.3)),
        ((0, -2.0, 0), earth_texture, (0.3, 0.3, 0.3)),
        ((0, 0, 2.0), mars_texture, (0.3, 0.3, 0.3)),
    ]:
        create_renderable(
            game_state.scene,
            sphere_mesh,
            texture,
            position=position,
            scale=scale,
        )

    return game_state
