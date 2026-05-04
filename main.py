from app.core.engine import Engine
from app.states.menu_state import MenuState
from app.world.builders.euclidean_space import build_euclidean_space_game_state
from app.world.builders.solar_system import build_solar_system_game_state


if __name__ == "__main__":
    engine = Engine()
    spaces = [
        ("Solar System", build_solar_system_game_state(engine)),
        ("Euclidean Space", build_euclidean_space_game_state(engine)),
    ]
    for index, (_, state) in enumerate(spaces):
        state.menu_spaces = spaces
        state.menu_selection = index
    engine.change_state(MenuState(engine, spaces))
    engine.run()
