import math

def create_sphere(radius=1.0, stacks=20, slices=20):
    vertices = []
    indices = []

    for i in range(stacks + 1):
        lat = math.pi * i / stacks

        for j in range(slices + 1):
            lon = 2 * math.pi * j / slices

            x = radius * math.sin(lat) * math.cos(lon)
            y = radius * math.cos(lat)
            z = radius * math.sin(lat) * math.sin(lon)
            u = j / slices
            v = i / stacks

            vertices += [x, y, z, u, v]

    for i in range(stacks):
        for j in range(slices):
            first = i * (slices + 1) + j
            second = first + slices + 1

            indices += [
                first, second, first + 1,
                second, second + 1, first + 1
            ]

    return vertices, indices


def create_pyramid(size=1.0, height=1.5):
    half = size / 2

    vertices = [
        # Base
        -half, -half, -half, 0.0, 0.0,
         half, -half, -half, 1.0, 0.0,
         half, -half,  half, 1.0, 1.0,
        -half, -half,  half, 0.0, 1.0,

        # Front face
        -half, -half,  half, 0.0, 0.0,
         half, -half,  half, 1.0, 0.0,
         0.0,   height, 0.0, 0.5, 1.0,

        # Right face
         half, -half,  half, 0.0, 0.0,
         half, -half, -half, 1.0, 0.0,
         0.0,   height, 0.0, 0.5, 1.0,

        # Back face
         half, -half, -half, 0.0, 0.0,
        -half, -half, -half, 1.0, 0.0,
         0.0,   height, 0.0, 0.5, 1.0,

        # Left face
        -half, -half, -half, 0.0, 0.0,
        -half, -half,  half, 1.0, 0.0,
         0.0,   height, 0.0, 0.5, 1.0,
    ]

    indices = [
        0, 1, 2,
        0, 2, 3,
        4, 5, 6,
        7, 8, 9,
        10, 11, 12,
        13, 14, 15,
    ]

    return vertices, indices
