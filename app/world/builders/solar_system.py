from app.states.game_state import GameState
from app.world.planet import Earth, Mars, Sun, Mercury, Jupiter, Venus, Saturn, Uranus, Neptune
from app.world.components.orbit import Orbit


def build_solar_system_game_state(engine):
    game_state = GameState(engine)

    game_state.show_euclidean_guides = True

    sun = Sun(position=(0, 0, 0)).create(game_state.scene)
    mercury = Mercury(position=(1, 0, 0)).create(game_state.scene)
    venus = Venus(position=(0, 0, 0)).create(game_state.scene)
    earth = Earth(position=(2, 0, 0)).create(game_state.scene)
    mars = Mars(position=(2.5, 0, 0)).create(game_state.scene)
    jupiter = Jupiter(position=(3, 0, 0)).create(game_state.scene)
    saturn = Saturn(position=(3, 0, 0)).create(game_state.scene)
    uranus = Uranus(position=(3, 0, 0)).create(game_state.scene)
    neptune = Neptune(position=(3, 0, 0)).create(game_state.scene)

    game_state.scene.add_component(
        mercury, 
        Orbit(center=(0, 0, 0), radius=2.2, angular_speed=1, angle=-1.8)
    )

    game_state.scene.add_component(
        venus, 
        Orbit(center=(0, 0, 0), radius=3.1, angular_speed=1, angle=-1.4)
    )

    game_state.scene.add_component(
        earth, 
        Orbit(center=(0, 0, 0), radius=4.0, angular_speed=1.25, angle=-1.1)
    )

    game_state.scene.add_component(
        mars, 
        Orbit(center=(0, 0, 0), radius=5.0, angular_speed=1, angle=-0.9)
    )

    game_state.scene.add_component(
        jupiter, 
        Orbit(center=(0, 0, 0), radius=6.8, angular_speed=0.083, angle=-0.65)
    )

    game_state.scene.add_component(
        saturn, 
        Orbit(center=(0, 0, 0), radius=8.8, angular_speed=0.083, angle=-0.5)
    )

    game_state.scene.add_component(
        uranus, 
        Orbit(center=(0, 0, 0), radius=10.6, angular_speed=0.083, angle=-0.38)
    )

    game_state.scene.add_component(
        neptune, 
        Orbit(center=(0, 0, 0), radius=12.2, angular_speed=0.083, angle=-0.3)
    )

    return game_state
