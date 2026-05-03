class Transform:
    def __init__(self, position=None, rotation=None, scale=None):
        self.position = list(position) if position is not None else [0, 0, 0]
        self.rotation = list(rotation) if rotation is not None else [0, 0, 0]
        self.scale = list(scale) if scale is not None else [1, 1, 1]
