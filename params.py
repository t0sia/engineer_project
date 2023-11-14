from napari_color_format import NapariColorFormat
from enums.segmentation_colors import SegmentationColors


class Params:
    original_image = None
    segmentation_colors = SegmentationColors(
        # aqua marine
        liver_color=NapariColorFormat("#7FFFD4"),
        # hot pink
        bladder_color=NapariColorFormat("#FF69B4"),
        # gold
        lungs_color=NapariColorFormat("#FFD700"),
        # lime green
        kidneys_color=NapariColorFormat("#32CD32"),
        # dark orchid
        bone_color=NapariColorFormat("#9932CC"),
        # orange red
        brain_color=NapariColorFormat("#FF4500"),
    )
    segmentation_opacity = 0.8
    segmentation_contour = 10
    image_opacity = 0.7
    image_gamma = 1
    border_color = "green"
    border_width = 3
    text_color = "white"
    text_size = 6

    def __init__(self):
        pass

    def print_params(self):
        print("original img", self.original_image)
        print("segmentation_opacity", self.segmentation_opacity)
        print("segmentation_contour", self.segmentation_contour)
        print("image_opacity", self.image_opacity)
        print("image_gamma", self.image_gamma)
        print("border_color", self.border_color)
        print("border_width", self.border_width)
        print("text_color", self.text_color)
        print("text_size", self.text_size)
        print("lungs_color", self.segmentation_colors.lungs_color)
        print("brain_color", self.segmentation_colors.brain_color)
        print("bone_color", self.segmentation_colors.bone_color)
        print("kidneys_color", self.segmentation_colors.kidneys_color)
        print("bladder_color", self.segmentation_colors.bladder_color)
        print("liver_color", self.segmentation_colors.liver_color)
