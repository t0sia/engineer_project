from engineer.napari_color_format import NapariColorFormat


# contains NapariColorFormat objects for
# each of the organs included in the
# segmentations
class SegmentationColors:
    def __init__(self,
                 liver_color: NapariColorFormat,
                 bladder_color: NapariColorFormat,
                 lungs_color: NapariColorFormat,
                 kidneys_color: NapariColorFormat,
                 bone_color: NapariColorFormat,
                 brain_color: NapariColorFormat):
        self.liver_color = liver_color
        self.bladder_color = bladder_color
        self.lungs_color = lungs_color
        self.kidneys_color = kidneys_color
        self.bone_color = bone_color
        self.brain_color = brain_color
