class BaseState:
    def __init__(self, engine):
        self.engine = engine

    def enter(self):
        pass

    def exit(self):
        pass

    def handle_event(self, event):
        pass

    def update(self, delta_time):
        pass

    def render(self):
        pass
