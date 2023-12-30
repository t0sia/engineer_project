import os
import cv2
import napari
import numpy as np
import tkinter as Tk
import matplotlib
from matplotlib import pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from napari_nifti._reader import load_nifti
import skimage.measure
import imageio.v3 as iio
from qtpy.QtCore import QTimer

from text_alignment import TextAlignment
from enums.blending import Blending
from enums.colormap import Colormap
from napari_color_format import NapariColorFormat
from segmentation_colors import SegmentationColors
from params import Params


class NapariWindow:
    # creates bounding box corners from segmentations array
    def make_corners(self, bbox_extents, i):
        minr = bbox_extents[0]
        minc = bbox_extents[1]
        maxr = bbox_extents[2]
        maxc = bbox_extents[3]

        for j in range(len(minr)):
            self.corners[6 * i + j][0][0] = minr[j]
            self.corners[6 * i + j][0][1] = minc[j]

            self.corners[6 * i + j][1][0] = maxr[j]
            self.corners[6 * i + j][1][1] = minc[j]

            self.corners[6 * i + j][2][0] = maxr[j]
            self.corners[6 * i + j][2][1] = maxc[j]

            self.corners[6 * i + j][3][0] = minr[j]
            self.corners[6 * i + j][3][1] = maxc[j]

    # saves 2D slices from napari viewer to .png format
    def save_images(self):
        for i in range(self.dimensions[0]):
            self.viewer.dims.current_step = (i, self.dimensions[1], self.dimensions[2])
            screenshot = self.viewer.screenshot(canvas_only=True)
            iio.imwrite(f"./screenshots/plane_{i}.png", screenshot)
        return "./screenshots"

    # displays result images in new Tkinter window
    def load_images(self, folder):
        images = []
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder, filename))
            if img is not None:
                images.append(img)
        return images

    def update_view(self, val):
        self.plot.imshow(self.images_array[val])

    def display_images(self):
        fig = plt.Figure()

        matplotlib.use("TkAgg", force=True)

        root = Tk.Tk()
        canvas = FigureCanvasTkAgg(fig, root)
        canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

        Tk.mainloop()

        self.plot = fig.add_subplot(111)

        self.plot.imshow(self.images_array[60])
        # Slider layout
        slider_ax = plt.axes([0.25, 0.1, 0.65, 0.03])

        image_slider = Slider(ax=slider_ax, label="", valmin=0, valmax=90, valinit=60)

        image_slider.on_changed(self.update_view)

    # converts SegmentationColors class instance to dictionary
    # supported as napari labels layer argument
    @staticmethod
    def segmentation_colors_to_layer_argument(segmentation_colors: SegmentationColors):
        colors_dict = {
            0: [0, 0, 0, 0.1],
            1: segmentation_colors.liver_color.to_rgba_array(),
            2: segmentation_colors.bladder_color.to_rgba_array(),
            3: segmentation_colors.lungs_color.to_rgba_array(),
            4: segmentation_colors.kidneys_color.to_rgba_array(),
            5: segmentation_colors.bone_color.to_rgba_array(),
            6: segmentation_colors.brain_color.to_rgba_array(),
        }
        return colors_dict

    def __init__(
        self,
        # path to original image in .nii.gz format
        # original_image,
        # path to segmentation image in .nii.gz format
        # segmentation,
        params,
        # colors for each of the organs
        # segmentation_colors = SegmentationColors(
        #     # aqua marine
        #     liver_color=NapariColorFormat('#7FFFD4'),
        #     # hot pink
        #     bladder_color=NapariColorFormat('#FF69B4'),
        #     # gold
        #     lungs_color=NapariColorFormat('#FFD700'),
        #     # lime green
        #     kidneys_color=NapariColorFormat('#32CD32'),
        #     # dark orchid
        #     bone_color=NapariColorFormat('#9932CC'),
        #     # orange red
        #     brain_color=NapariColorFormat('#FF4500')
        # ),
        # opacity for the segmentation layer (from 0 to 1)
        # segmentation_opacity = 0.8,
        # blending of the segmentation (options as specified in Blending enum)
        segmentation_blending=Blending.translucent.name,
        # contour parameter for segmentation
        # [!!!!] fajny argument sprawdzcie sobie jak to dziala imo spoko by to uwzglednic
        # segmentation_contour = 0,
        # opacity for the original image layer (from 0 to 1)
        # image_opacity = 0.7,
        # gamma for the original image layer (from 0.2 to 2)
        # image_gamma = 1,
        # colormap of the image (options as specified in ColorMap enum)
        image_colormap=Colormap.gray.name,
        # blending of the image (options as specified in Blending enum)
        image_blending=Blending.translucent.name,
        # color of the border (segmentation layer)
        # border_color = 'blue',
        # width of the border edge (more than 5 is too much imo)
        # border_width = 5,
        # color of border labels
        # text_color = 'green',
        # font size of border labels
        # text_size = 8,
        # alignment of border labels (as specified in TextAlignment enum)
        text_alignment=TextAlignment.center.name,
    ):
        self.original_image = params.original_image
        self.segmentation = params.segmentation

        if params.segmentation_opacity > 1 or params.segmentation_opacity < 0:
            raise ValueError(
                "Opacity value for segmentation layer is not within required bounds (between 0 and 1)."
            )

        self.segmentation_colors = self.segmentation_colors_to_layer_argument(
            params.segmentation_colors
        )
        self.segmentation_opacity = params.segmentation_opacity
        self.segmentation_blending = segmentation_blending
        self.segmentation_contour = params.segmentation_contour

        if params.image_opacity > 1 or params.image_opacity < 0:
            raise ValueError(
                "Opacity value for original image layer is not within required bounds (between 0 and 1)."
            )

        if params.image_gamma < 0.2 or params.image_gamma > 2:
            raise ValueError(
                "Gamma value for original image layer is not within required bounds (between 0.2 and 2)."
            )

        self.image_opacity = params.image_opacity
        self.image_gamma = params.image_gamma
        self.image_colormap = image_colormap
        self.image_blending = image_blending

        self.border_color = params.border_color
        self.border_width = params.border_width

        self.text_color = params.text_color
        self.text_size = params.text_size
        self.text_alignment = text_alignment

        self.image_data = load_nifti(self.original_image)
        self.label_data = load_nifti(self.segmentation)
        self.label_data["image"] = self.label_data["image"].astype(int)

        if self.image_data["image"].shape != self.label_data["image"].shape:
            raise ValueError("Segmentation is of different dimensions than input image")

        self.dimensions = self.image_data["image"].shape

        self.slices = (
            np.arange(self.dimensions[0])
            .repeat(repeats=6)
            .reshape((self.dimensions[0] * 6, 1, 1))
        )
        self.slices = np.tile(self.slices, (1, 4, 1))

        self.corners = (
            np.zeros(self.dimensions[0])
            .repeat(repeats=6)
            .reshape((self.dimensions[0] * 6, 1, 1))
        )
        self.corners = np.tile(self.corners, (1, 4, 2))

        self.organ_labels = {
            1: "Liver",
            2: "Bladder",
            3: "Lungs",
            4: "Kidneys",
            5: "Bone",
            6: "Brain",
        }

        self.viewer = napari.Viewer()
        self.viewer.window._toggle_menubar_visible()
        self.viewer.window._qt_viewer.layerButtons.hide()
        self.viewer.window._qt_viewer.layers.hide()
        self.viewer.window._qt_viewer.controls.hide()
        self.viewer.window._qt_viewer.viewerButtons.hide()
        self.viewer.window._qt_viewer.dockLayerList.hide()
        self.viewer.window._qt_viewer.dockLayerControls.hide()

        self.viewer.add_image(
            self.image_data["image"],
            opacity=self.image_opacity,
            gamma=self.image_gamma,
            blending=self.image_blending,
            colormap=self.image_colormap,
        )

        # TODO: contour nie jest parametrem tylko atrybutem więc
        # to trzeba jakoś inaczej zrobić (o ile się da) (albo wcale)
        self.viewer.add_labels(
            self.label_data["image"],
            num_colors=6,
            opacity=self.segmentation_opacity,
            blending=self.segmentation_blending,
            # contour=self.segmentation_contour,
            color=self.segmentation_colors,
        )

        self.properties = {"label": ["" for _ in range(self.dimensions[0] * 6)]}

        for i in range(self.dimensions[0]):
            features = skimage.measure.regionprops_table(
                self.label_data["image"][i],
                properties=("label", "bbox", "perimeter", "area"),
            )
            self.make_corners([features[f"bbox-{j}"] for j in range(4)], i)
            for k in range(len(features["label"])):
                self.properties["label"][i * 6 + k] = self.organ_labels[
                    features["label"][k]
                ]

        self.shapes = np.concatenate((self.slices, self.corners), axis=2)

        self.text_kwargs = {
            "text": "{label}",
            "size": self.text_size,
            "color": self.text_color,
            "anchor": self.text_alignment,
            "translation": [0, 0],
        }

        self.viewer.add_shapes(
            np.array(self.shapes),
            shape_type="polygon",
            edge_color=self.border_color,
            edge_width=self.border_width,
            face_color="transparent",
            name="sliced",
            properties=self.properties,
            text=self.text_kwargs,
        )

        images_folder = self.save_images()

        napari.run()

        # self.viewer.close()

        # self.images_array = self.load_images(images_folder)
        # self.display_images()
