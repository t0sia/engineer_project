from PIL import ImageColor

class NapariColorFormat():

    def __init__(self, hex_code, alpha=0.8):
        rgb_tuple = ImageColor.getcolor(hex_code, 'RGB')
        self.red = rgb_tuple[0] / 255
        self.green = rgb_tuple[1] / 255
        self.blue = rgb_tuple[2] / 255
        self.alpha = alpha

    def to_rgba_array(self):
        return [self.red, self.green, self.blue, self.alpha]