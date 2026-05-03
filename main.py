from app.graphics.mesh import Mesh
from app.graphics.texture import Texture
from app.core.engine import Engine
from app.graphics.geometry import create_pyramid, create_sphere


if __name__ == "__main__":
    engine = Engine()

    # Create assets
    earth_vertices, earth_indices = create_sphere()

    earth_mesh = Mesh(earth_vertices, earth_indices)
    earth_texture = Texture("assets/earth.jpg")

    mars_vertices, mars_indices = create_sphere()

    mars_mesh = Mesh(mars_vertices, mars_indices)
    mars_texture = Texture("assets/mars.jpg")

    engine.add_entity(earth_mesh, earth_texture, position=(-1.5, 0, 0))
    engine.add_entity(mars_mesh, mars_texture, position=(1.5, 0, 0))

    engine.run()
