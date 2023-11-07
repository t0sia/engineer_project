import napari
import numpy as np
from napari_nifti._reader import load_nifti
from napari_nifti._writer import write_single_image
import skimage.measure
import imageio.v3 as iio


labels_filepath = './labels-31.nii'
img_filepath = './volume-31.nii'

class NapariWindow():

    def make_corners(self, bbox_extents, i):
        minr = bbox_extents[0]
        minc = bbox_extents[1]
        maxr = bbox_extents[2]
        maxc = bbox_extents[3]

        #nie spierdol wymiarow tu pls
        for j in range(len(minr)):
            self.corners[6*i+j][0][0] = minr[j]
            self.corners[6*i+j][0][1] = minc[j]

            self.corners[6*i+j][1][0] = maxr[j]
            self.corners[6*i+j][1][1] = minc[j]

            self.corners[6*i+j][2][0] = maxr[j]
            self.corners[6*i+j][2][1] = maxc[j]

            self.corners[6*i+j][3][0] = minr[j]
            self.corners[6*i+j][3][1] = maxc[j]

    def __init__(self, original_image,
                 segmentation,
                 ):

        self.original_image = original_image
        self.segmentation = segmentation

        self.image_data = load_nifti(self.original_image)
        write_single_image(self.original_image, self.image_data['image'], self.image_data['metadata'])

        self.label_data = load_nifti(self.segmentation)
        write_single_image(self.segmentation, self.label_data['image'], self.label_data['metadata'])

        if self.image_data['image'].shape != self.label_data['image'].shape:
            raise ValueError('Segmentation is of different dimensions than input image')

        self.dimensions = self.image_data['image'].shape

        self.slices = np.arange(self.dimensions[0]).repeat(repeats=6).reshape((self.dimensions[0]*6, 1, 1))
        self.slices = np.tile(self.slices, (1, 4, 1))

        self.corners = np.zeros(self.dimensions[0]).repeat(repeats=6).reshape((self.dimensions[0]*6, 1, 1))
        self.corners = np.tile(self.corners, (1, 4, 2))

        # TODO: dodać własne colormaps (ale to powinno być łatwe)
        viewer = napari.Viewer()

        viewer.add_image(self.image_data['image'])
        viewer.add_labels(self.label_data['image'])

        for i in range(self.dimensions[0]):
            features = skimage.measure.regionprops_table(
                self.label_data['image'][i], properties=('label', 'bbox', 'perimeter', 'area')
            )
            self.make_corners([features[f'bbox-{j}'] for j in range(4)], i)

        self.shapes = np.concatenate((self.slices, self.corners), axis=2)

        layer = viewer.add_shapes(
            np.array(self.shapes),
            shape_type='polygon',
            edge_color='green',
            edge_width = 5,
            face_color='transparent',
            name='sliced',
        )


        for i in range(self.dimensions[0]):
            viewer.dims.current_step = (i, self.dimensions[1], self.dimensions[2])
            screenshot = viewer.screenshot(canvas_only=True)
            iio.imwrite(f'./screenshots/plane_{i}.png', screenshot)

        #napari.run()


NapariWindow(img_filepath, labels_filepath)