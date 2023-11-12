import tkinter
from tkinter.colorchooser import askcolor
from napari_color_format import NapariColorFormat


def open_seg_color_settings(seg):
    seg = NapariColorFormat(askcolor()[1])


class ColorsWindow:
    def __init__(self, params, is_dark_mode):
        self.params = params
        self.is_dark_mode = is_dark_mode
        self.colors_window = tkinter.Toplevel()

        self.bg = tkinter.PhotoImage(file="backgrounds/dark.png") if self.is_dark_mode else tkinter.PhotoImage(
            file="backgrounds/light.png")

        self.label_liver_img = tkinter.PhotoImage(
            file="buttons_dark/liver.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/liver.png")
        self.label_kidneys_img = tkinter.PhotoImage(
            file="buttons_dark/kidneys.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/kidneys.png")
        self.label_bladder_img = tkinter.PhotoImage(
            file="buttons_dark/bladder.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/bladder.png")
        self.label_lungs_img = tkinter.PhotoImage(
            file="buttons_dark/lungs.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/lungs.png")
        self.label_brain_img = tkinter.PhotoImage(
            file="buttons_dark/brain.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/brain.png")
        self.label_bone_img = tkinter.PhotoImage(file="buttons_dark/bone.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/bone.png")
        self.bt_select_color_img = tkinter.PhotoImage(
            file="buttons_dark/select-color.png") if is_dark_mode else tkinter.PhotoImage(
            file="buttons_light/select-color.png")

        self.colors_window.title("Settings")
        img_bg = tkinter.Label(self.colors_window, image=self.bg)
        img_bg.pack()

    def open(self):
        tkinter.Label(self.colors_window, image=self.label_liver_img).place(x=200, y=100)
        bt_select_color_liver = tkinter.Button(self.colors_window, image=self.bt_select_color_img,
                                               command=lambda: open_seg_color_settings(
                                                   self.params.segmentation_colors.liver_color))
        bt_select_color_liver.place(x=800, y=100)
        tkinter.Label(self.colors_window, height=4, width=8,
                      bg=self.params.segmentation_colors.liver_color.to_rgb).place(x=700, y=100)

        kidneys_label = tkinter.Label(self.colors_window, image=self.label_kidneys_img)
        kidneys_label.place(x=200, y=170)
        bt_select_color_kidneys = tkinter.Button(self.colors_window, image=self.bt_select_color_img,
                                                 command=lambda: open_seg_color_settings(
                                                     self.params.segmentation_colors.kidneys_color))
        bt_select_color_kidneys.place(x=800, y=170)
        tkinter.Label(self.colors_window, height=4, width=8,
                      bg=self.params.segmentation_colors.kidneys_color.to_rgb).place(x=700, y=170)

        bladder_label = tkinter.Label(self.colors_window, image=self.label_bladder_img)
        bladder_label.place(x=200, y=240)
        bt_select_color_bladder = tkinter.Button(self.colors_window, image=self.bt_select_color_img,
                                                 command=lambda: open_seg_color_settings(
                                                     self.params.segmentation_colors.bladder_color))
        bt_select_color_bladder.place(x=800, y=240)
        tkinter.Label(self.colors_window, height=4, width=8,
                      bg=self.params.segmentation_colors.bladder_color.to_rgb).place(x=700, y=240)

        lungs_label = tkinter.Label(self.colors_window, image=self.label_lungs_img)
        lungs_label.place(x=200, y=310)
        bt_select_color_lungs = tkinter.Button(self.colors_window, image=self.bt_select_color_img,
                                               command=lambda: open_seg_color_settings(
                                                   self.params.segmentation_colors.lungs_color))
        bt_select_color_lungs.place(x=800, y=310)
        tkinter.Label(self.colors_window, height=4, width=8,
                      bg=self.params.segmentation_colors.lungs_color.to_rgb).place(x=700, y=310)

        brain_label = tkinter.Label(self.colors_window, image=self.label_brain_img)
        brain_label.place(x=200, y=380)
        bt_select_color_brain = tkinter.Button(self.colors_window, image=self.bt_select_color_img,
                                               command=lambda: open_seg_color_settings(
                                                   self.params.segmentation_colors.brain_color))
        bt_select_color_brain.place(x=800, y=380)
        tkinter.Label(self.colors_window, height=4, width=8,
                      bg=self.params.segmentation_colors.brain_color.to_rgb).place(x=700, y=380)

        bone_label = tkinter.Label(self.colors_window, image=self.label_bone_img)
        bone_label.place(x=200, y=450)
        bt_select_color_bone = tkinter.Button(self.colors_window, image=self.bt_select_color_img,
                                              command=lambda: open_seg_color_settings(
                                                  self.params.segmentation_colors.bone_color))
        bt_select_color_bone.place(x=800, y=450)
        tkinter.Label(self.colors_window, height=4, width=8,
                      bg=self.params.segmentation_colors.bone_color.to_rgb).place(x=700, y=450)

        self.colors_window.mainloop()
