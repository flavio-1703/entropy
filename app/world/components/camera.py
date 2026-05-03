class Camera:
    def __init__(self, yaw=0.0, pitch=0.0, mouse_sensitivity=0.05, active=True):
        self.yaw = yaw
        self.pitch = pitch
        self.mouse_sensitivity = mouse_sensitivity
        self.active = active
