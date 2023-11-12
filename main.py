import tkinter
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
from napari_window import NapariWindow
from params import Params


def dark_mode():
    global is_dark_mode
    if not is_dark_mode:
        img.config(image=bg_dark)
        StartButton.config(image=bt_start_img_dark)
        AddFileButton.config(image=bt_add_file_img_dark)
        InstructionDialogButton.config(image=bt_instruction_img_dark)
        SettingsButton.config(image=bt_settings_img_dark)
        DarkModeButton.config(image=bt_mode_img_dark)
        is_dark_mode = True
    else:
        img.config(image=bg)
        StartButton.config(image=bt_start_img)
        AddFileButton.config(image=bt_add_file_img)
        InstructionDialogButton.config(image=bt_instruction_img)
        SettingsButton.config(image=bt_settings_img)
        DarkModeButton.config(image=bt_mode_img)
        is_dark_mode = False


def set_text_color():
    myParams.text_color = askcolor()


def set_border_color():
    myParams.border_color = askcolor()


def open_file_dialog():
    myParams.original_image = askopenfile().name


def start():
    print("Start")
    if myParams.original_image:
        NapariWindow(labels_filepath, myParams)
    else:
        label_upload_file = tkinter.Label(root, font=("Helvetica", 28), bg="red", text='Please upload file!')
        label_upload_file.place(x=400, y=600)


def open_seg_color_settings(seg):
    seg = askcolor()


def open_seg_colors_dialog():
    global bg, is_dark_mode, myParams
    colors_window = tkinter.Toplevel(root)
    colors_window.title("Segmentation Colors")
    tkinter.Label(root, image=bg).pack()

    bt_select_color_img = tkinter.PhotoImage(file="buttons_dark/select-color.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/select-color.png")

    label_liver_img = tkinter.PhotoImage(file="buttons_dark/liver.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/liver.png")
    liver_label = tkinter.Label(colors_window, image=label_liver_img)
    liver_label.place(x=200, y=100)
    bt_select_color_liver = tkinter.Button(colors_window, image=bt_select_color_img, command=lambda: open_seg_color_settings(myParams.segmentation_colors.liver_color))
    bt_select_color_liver.place(x=800, y=100)

    label_kidneys_img = tkinter.PhotoImage(file="buttons_dark/kidneys.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/kidneys.png")
    kidneys_label = tkinter.Label(colors_window, image=label_kidneys_img)
    kidneys_label.place(x=200, y=170)
    bt_select_color_kidneys = tkinter.Button(colors_window, image=bt_select_color_img, command=lambda: open_seg_color_settings(myParams.segmentation_colors.kidneys_color))
    bt_select_color_kidneys.place(x=800, y=170)

    label_bladder_img = tkinter.PhotoImage(file="buttons_dark/bladder.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/bladder.png")
    bladder_label = tkinter.Label(colors_window, image=label_bladder_img)
    bladder_label.place(x=200, y=240)
    bt_select_color_bladder = tkinter.Button(colors_window, image=bt_select_color_img, command=lambda: open_seg_color_settings(myParams.segmentation_colors.bladder_color))
    bt_select_color_bladder.place(x=800, y=240)

    label_lungs_img = tkinter.PhotoImage(file="buttons_dark/lungs.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/lungs.png")
    lungs_label = tkinter.Label(colors_window, image=label_lungs_img)
    lungs_label.place(x=200, y=310)
    bt_select_color_lungs = tkinter.Button(colors_window, image=bt_select_color_img, command=lambda: open_seg_color_settings(myParams.segmentation_colors.lungs_color))
    bt_select_color_lungs.place(x=800, y=310)

    label_brain_img = tkinter.PhotoImage(file="buttons_dark/brain.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/brain.png")
    brain_label = tkinter.Label(colors_window, image=label_brain_img)
    brain_label.place(x=200, y=380)
    bt_select_color_brain = tkinter.Button(colors_window, image=bt_select_color_img, command=lambda: open_seg_color_settings(myParams.segmentation_colors.brain_color))
    bt_select_color_brain.place(x=800, y=380)

    label_bone_img = tkinter.PhotoImage(file="buttons_dark/bone.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/bone.png")
    bone_label = tkinter.Label(colors_window, image=label_bone_img)
    bone_label.place(x=200, y=450)
    bt_select_color_bone = tkinter.Button(colors_window, image=bt_select_color_img, command=lambda: open_seg_color_settings(myParams.segmentation_colors.bone_color))
    bt_select_color_bone.place(x=800, y=450)


def open_settings_window():
    global bg, is_dark_mode, myParams
    settings_window = tkinter.Toplevel(root)
    settings_window.title("Settings")
    tkinter.Label(settings_window, image=bg).pack()

    label_seg_colors_img = tkinter.PhotoImage(file="buttons_dark/segmentation-colors.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/segmentation-colors.png")
    seg_colors_label = tkinter.Label(settings_window, image=label_seg_colors_img)
    seg_colors_label.place(x=100, y=32)
    bt_select_colors_img = tkinter.PhotoImage(file="buttons_dark/select-colors-dialog.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/select-colors-dialog.png")
    bt_select_colors = tkinter.Button(settings_window, image=bt_select_colors_img, command=open_seg_colors_dialog)
    bt_select_colors.place(x=800, y=32)

    label_seg_opacity_img = tkinter.PhotoImage(file="buttons_dark/segmentation-opacity.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/segmentation-opacity.png")
    seg_opacity_label = tkinter.Label(settings_window, image=label_seg_opacity_img)
    seg_opacity_label.place(x=100, y=102)
    seg_opacity_scale = tkinter.Scale(settings_window, variable=myParams.segmentation_opacity, from_=0, to=1, length=400)
    seg_opacity_scale.place(x=800, y=102)

    label_seg_contour_img = tkinter.PhotoImage(file="buttons_dark/segmentation-contour.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/segmentation-contour.png")
    seg_contour_label = tkinter.Label(settings_window, image=label_seg_contour_img)
    seg_contour_label.place(x=100, y=172)

    label_img_opacity_img = tkinter.PhotoImage(file="buttons_dark/image-opacity.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/image-opacity.png")
    img_opacity_label = tkinter.Label(settings_window, image=label_img_opacity_img)
    img_opacity_label.place(x=100, y=242)
    img_opacity_scale = tkinter.Scale(settings_window, variable=myParams.image_opacity, from_=0, to=1, length=400)
    img_opacity_scale.place(x=800, y=242)

    label_img_gamma_img = tkinter.PhotoImage(file="buttons_dark/image-gamma.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/image-gamma.png")
    img_gamma_label = tkinter.Label(settings_window, image=label_img_gamma_img)
    img_gamma_label.place(x=100, y=312)
    img_gamma_scale = tkinter.Scale(settings_window, variable=myParams.image_gamma, from_=0.2, to=2, length=400)
    img_gamma_scale.place(x=800, y=312)

    label_border_color_img = tkinter.PhotoImage(file="buttons_dark/border-color.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/border-color.png")
    border_color_label = tkinter.Label(settings_window, image=label_border_color_img)
    border_color_label.place(x=100, y=382)
    bt_border_color_img = tkinter.PhotoImage(file="buttons_dark/select-color.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/select-color.png")
    bt_border_color = tkinter.Button(settings_window, image=bt_border_color_img, command=set_border_color)
    bt_border_color.place(x=800, y=382)

    label_border_width_img = tkinter.PhotoImage(file="buttons_dark/border-width.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/border-width.png")
    border_width_label = tkinter.Label(settings_window, image=label_border_width_img)
    border_width_label.place(x=100, y=452)

    label_text_color_img = tkinter.PhotoImage(file="buttons_dark/text-color.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/text-color.png")
    text_color_label = tkinter.Label(settings_window, image=label_text_color_img)
    text_color_label.place(x=100, y=522)
    bt_text_color_img = tkinter.PhotoImage(file="buttons_dark/select-color.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/select-color.png")
    bt_text_color = tkinter.Button(settings_window, image=bt_text_color_img, command=set_text_color)
    bt_text_color.place(x=800, y=382)

    label_text_size_img = tkinter.PhotoImage(file="buttons_dark/text-size.png") if is_dark_mode else tkinter.PhotoImage(file="buttons_light/text-size.png")
    text_size_label = tkinter.Label(settings_window, image=label_text_size_img)
    text_size_label.place(x=100, y=592)


is_dark_mode = False
labels_filepath = './labels-31.nii'
myParams = Params

root = tkinter.Tk()
root.geometry("1200x675")

bg = tkinter.PhotoImage(file="backgrounds/light.png")
bg_dark = tkinter.PhotoImage(file="backgrounds/dark.png")
img = tkinter.Label(root, image=bg)
img.pack()

bt_start_img = tkinter.PhotoImage(file="buttons_light/start.png")
bt_start_img_dark = tkinter.PhotoImage(file="buttons_dark/start.png")
StartButton = tkinter.Button(root, command=start, image=bt_start_img)
StartButton.place(x=400, y=50)

bt_add_file_img = tkinter.PhotoImage(file="buttons_light/add-file.png")
bt_add_file_img_dark = tkinter.PhotoImage(file="buttons_dark/add-file.png")
AddFileButton = tkinter.Button(root, command=open_file_dialog, image=bt_add_file_img)
AddFileButton.place(x=400, y=160)

bt_settings_img = tkinter.PhotoImage(file="buttons_light/settings.png")
bt_settings_img_dark = tkinter.PhotoImage(file="buttons_dark/settings.png")
SettingsButton = tkinter.Button(root, command=open_settings_window, image=bt_settings_img)
SettingsButton.place(x=400, y=270)

bt_instruction_img = tkinter.PhotoImage(file="buttons_light/instruction.png")
bt_instruction_img_dark = tkinter.PhotoImage(file="buttons_dark/instruction.png")
InstructionDialogButton = tkinter.Button(root, image=bt_instruction_img)
InstructionDialogButton.place(x=400, y=380)

bt_mode_img = tkinter.PhotoImage(file="buttons_light/dark-mode.png")
bt_mode_img_dark = tkinter.PhotoImage(file="buttons_dark/light-mode.png")
DarkModeButton = tkinter.Button(root, command=dark_mode, image=bt_mode_img)
DarkModeButton.place(x=400, y=490)

root.mainloop()

