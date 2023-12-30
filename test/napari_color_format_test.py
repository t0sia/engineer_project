import unittest

import os
import sys
parent_dir_name = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(parent_dir_name + "/test")

from engineer.napari_color_format import NapariColorFormat

class NapariColorFormatTest(unittest.TestCase):

    def test_to_rgba_array(self):
        test_case_1 = NapariColorFormat('#F3E1BA', 0.8)
        expected_result_1 = [243 / 255, 225 / 255, 186 / 255, 0.8]

        test_case_2 = NapariColorFormat('#12a9ef', 1.0)
        expected_result_2 = [18 / 255, 169 / 255, 239 / 255, 1.0]

        test_case_3 = NapariColorFormat('#E9B0AF', 0.0001)
        expected_result_3 = [233 / 255, 176 / 255, 175 / 255, 0.0001]

        self.assertEqual(NapariColorFormat.to_rgba_array(test_case_1), expected_result_1)
        self.assertEqual(NapariColorFormat.to_rgba_array(test_case_2), expected_result_2)
        self.assertEqual(NapariColorFormat.to_rgba_array(test_case_3), expected_result_3)

if __name__ == '__main__':
    unittest.main()