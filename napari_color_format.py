from PIL import ImageColor


# creates object with nomralised RGBA format
# (napari-supported) from hex code ('#' included)
class NapariColorFormat:

    def __init__(self, hex_code, alpha=0.8):
        self.hex_code = hex_code
        rgb_tuple = ImageColor.getcolor(hex_code, 'RGB')
        self.red = rgb_tuple[0] / 255
        self.green = rgb_tuple[1] / 255
        self.blue = rgb_tuple[2] / 255
        self.alpha = alpha

    # returns RGBA array from class instance
    def to_rgba_array(self):
        return [self.red, self.green, self.blue, self.alpha]
