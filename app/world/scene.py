class Scene:
    def __init__(self):
        self._next_entity_id = 1
        self.entities = []
        self._components = {}
        self.systems = []

    def create_entity(self):
        from app.world.entity import Entity

        entity = Entity(self._next_entity_id)
        self._next_entity_id += 1
        self.entities.append(entity)
        return entity

    def add_component(self, entity, component):
        self._components.setdefault(type(component), {})[entity.id] = component
        return component

    def get_component(self, entity, component_type):
        return self._components.get(component_type, {}).get(entity.id)

    def get_components(self, *component_types):
        for entity in self.entities:
            components = []
            for component_type in component_types:
                component = self.get_component(entity, component_type)
                if component is None:
                    break
                components.append(component)
            else:
                yield (entity, *components)

    def find_first(self, *component_types, predicate=None):
        for entity, *components in self.get_components(*component_types):
            if predicate is None or predicate(*components):
                return (entity, *components)
        return None

    def add_system(self, system):
        self.systems.append(system)

    def update(self, delta_time):
        for system in self.systems:
            system.update(self, delta_time)
