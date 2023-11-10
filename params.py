from napari_color_format import NapariColorFormat
from enums.segmentation_colors import SegmentationColors


class Params:
    original_image = None
    segmentation_colors = SegmentationColors(
                     # aqua marine
                     liver_color=NapariColorFormat('#7FFFD4'),
                     # hot pink
                     bladder_color=NapariColorFormat('#FF69B4'),
                     # gold
                     lungs_color=NapariColorFormat('#FFD700'),
                     # lime green
                     kidneys_color=NapariColorFormat('#32CD32'),
                     # dark orchid
                     bone_color=NapariColorFormat('#9932CC'),
                     # orange red
                     brain_color=NapariColorFormat('#FF4500')
                 )
    segmentation_opacity = 0.8
    segmentation_contour = 2
    image_opacity = 0.7
    image_gamma = 1
    border_color = 'green'
    border_width = 3
    text_color = 'white'
    text_size = 6
