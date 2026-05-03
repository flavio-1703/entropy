from app.world.transform import Transform

class Entity:
    def __init__(self, mesh, texture):
        self.mesh = mesh
        self.texture = texture
        self.transform = Transform()
