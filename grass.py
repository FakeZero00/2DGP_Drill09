from pico2d import load_image


class Grass:
    image = None

    def __init__(self, y = 30):
        if self.image is None:
            self.image = load_image('grass.png')
        self. y = y

    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        pass
