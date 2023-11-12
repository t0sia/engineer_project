import tkinter
from tkinter.colorchooser import askcolor
from tkinter import HORIZONTAL
from colors_window import ColorsWindow


class SettingsWindow:
    def __init__(self, params, is_dark_mode):
        self.params = params
        self.is_dark_mode = is_dark_mode

        self.settings_window = tkinter.Toplevel()

        self.bg = tkinter.PhotoImage(file="backgrounds/dark.png") if self.is_dark_mode else tkinter.PhotoImage(
            file="backgrounds/light.png")

        self.label_seg_colors_img = tkinter.PhotoImage(
            file="buttons_dark/segmentation-colors.png") if self.is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/segmentation-colors.png")
        self.bt_select_colors_img = tkinter.PhotoImage(
            file="buttons_dark/select-colors-dialog.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/select-colors-dialog.png")
        self.label_seg_opacity_img = tkinter.PhotoImage(
            file="buttons_dark/segmentation-opacity.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/segmentation-opacity.png")
        self.label_seg_contour_img = tkinter.PhotoImage(
            file="buttons_dark/segmentation-contour.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/segmentation-contour.png")
        self.label_img_opacity_img = tkinter.PhotoImage(
            file="buttons_dark/image-opacity.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/image-opacity.png")
        self.label_img_gamma_img = tkinter.PhotoImage(
            file="buttons_dark/image-gamma.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/image-gamma.png")
        self.label_border_color_img = tkinter.PhotoImage(
            file="buttons_dark/border-color.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/border-color.png")
        self.bt_select_color_img = tkinter.PhotoImage(
            file="buttons_dark/select-color.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/select-color.png")
        self.label_border_width_img = tkinter.PhotoImage(
            file="buttons_dark/border-width.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/border-width.png")
        self.label_text_color_img = tkinter.PhotoImage(
            file="buttons_dark/text-color.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/text-color.png")
        self.label_text_size_img = tkinter.PhotoImage(
            file="buttons_dark/text-size.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/text-size.png")

        self.settings_window.title("Settings")
        img_bg = tkinter.Label(self.settings_window, image=self.bg)
        img_bg.pack()

    def gamma_scale(self, var):
        self.params.image_gamma = var

    def img_opacity_scale(self, var):
        self.params.image_opacity = var

    def seg_opacity_scale(self, var):
        self.params.segmentation_opacity = var

    def set_text_color(self):
        self.params.text_color = askcolor()[1]

    def set_border_color(self):
        self.params.border_color = askcolor()[1]

    def open_seg_colors_dialog(self):
        color_window = ColorsWindow(is_dark_mode=self.is_dark_mode, params=self.params)
        color_window.open()

    def open(self):
        seg_colors_label = tkinter.Label(self.settings_window, image=self.label_seg_colors_img)
        seg_colors_label.place(x=100, y=32)
        bt_select_colors = tkinter.Button(self.settings_window, image=self.bt_select_colors_img, command=self.open_seg_colors_dialog)
        bt_select_colors.place(x=800, y=32)

        seg_opacity_label = tkinter.Label(self.settings_window, image=self.label_seg_opacity_img)
        seg_opacity_label.place(x=100, y=102)
        seg_opacity_scale = tkinter.Scale(self.settings_window, command=self.seg_opacity_scale, from_=0, to=1,
                                          length=300, orient=HORIZONTAL, resolution=0.1)
        seg_opacity_scale.place(x=800, y=102)

        seg_contour_label = tkinter.Label(self.settings_window, image=self.label_seg_contour_img)
        seg_contour_label.place(x=100, y=172)

        img_opacity_label = tkinter.Label(self.settings_window, image=self.label_img_opacity_img)
        img_opacity_label.place(x=100, y=242)
        img_opacity_scale = tkinter.Scale(self.settings_window, command=self.img_opacity_scale, from_=0, to=1,
                                          length=300, orient=HORIZONTAL, resolution=0.1)
        img_opacity_scale.place(x=800, y=242)

        img_gamma_label = tkinter.Label(self.settings_window, image=self.label_img_gamma_img)
        img_gamma_label.place(x=100, y=312)
        img_gamma_scale = tkinter.Scale(self.settings_window, command=self.gamma_scale, from_=0.2, to=2,
                                        length=300, orient=HORIZONTAL, resolution=0.1)
        img_gamma_scale.place(x=800, y=312)

        border_color_label = tkinter.Label(self.settings_window, image=self.label_border_color_img)
        border_color_label.place(x=100, y=382)
        bt_border_color = tkinter.Button(self.settings_window, image=self.bt_select_color_img, command=self.set_border_color)
        bt_border_color.place(x=800, y=382)

        border_width_label = tkinter.Label(self.settings_window, image=self.label_border_width_img)
        border_width_label.place(x=100, y=452)

        text_color_label = tkinter.Label(self.settings_window, image=self.label_text_color_img)
        text_color_label.place(x=100, y=522)
        bt_text_color = tkinter.Button(self.settings_window, image=self.bt_select_color_img, command=self.set_text_color)
        bt_text_color.place(x=800, y=522)

        text_size_label = tkinter.Label(self.settings_window, image=self.label_text_size_img)
        text_size_label.place(x=100, y=592)

        self.settings_window.mainloop()

