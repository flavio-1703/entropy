from app.core.engine import Engine
from app.states.menu_state import MenuState
from app.world.builders.solar_system import build_solar_system_game_state


if __name__ == "__main__":
    engine = Engine()
    game_state = build_solar_system_game_state(engine)
    engine.change_state(MenuState(engine, game_state))
    engine.run()
