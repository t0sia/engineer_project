import unittest

import os
import sys

parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/test")

from engineer.napari_window import NapariWindow
from engineer.napari_color_format import NapariColorFormat
from engineer.segmentation_colors import SegmentationColors
from engineer.params import Params


class NapariWindowTest(unittest.TestCase):
    def test_segmentation_colors_to_layer_argument(self):
        test_case = SegmentationColors(
            liver_color=NapariColorFormat("#A5FE89", 0.8),
            bladder_color=NapariColorFormat("#F0ACDD", 0.7),
            lungs_color=NapariColorFormat("#CBF1E9", 1.0),
            kidneys_color=NapariColorFormat("#DCF5A1", 0.988),
            bone_color=NapariColorFormat("#9BADDC", 0.0),
            brain_color=NapariColorFormat("#FDDF00", 0.5),
        )

        colors_dict = {
            0: [0, 0, 0, 0.1],
            1: [165 / 255, 254 / 255, 137 / 255, 0.8],
            2: [240 / 255, 172 / 255, 221 / 255, 0.7],
            3: [203 / 255, 241 / 255, 233 / 255, 1.0],
            4: [220 / 255, 245 / 255, 161 / 255, 0.988],
            5: [155 / 255, 173 / 255, 220 / 255, 0.0],
            6: [253 / 255, 223 / 255, 0 / 255, 0.5],
        }

        self.assertEqual(
            NapariWindow.segmentation_colors_to_layer_argument(test_case), colors_dict
        )


if __name__ == "__main__":
    unittest.main()
