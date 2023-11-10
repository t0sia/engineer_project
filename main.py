import tkinter
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
from napari_window import NapariWindow
from params import Params

segments = [
    {"name": "LIVER", "color": "blue"},
    {"name": "BRAIN", "color": "red"},
    {"name": "LUNGS", "color": "yellow"},
    {"name": "BLADDER", "color": "green"},
    {"name": "KIDNEY", "color": "white"}
]

is_dark_mode = True
mode_button_text = 'Switch to light mode'
labels_filepath = './labels-31.nii'
img_filepath = './volume-31.nii'
myParams = Params


def dark_mode():
    global is_dark_mode, img, bg_dark
    img.config(image=bg_dark)
    is_dark_mode = not is_dark_mode


def color():
    new_color = askcolor()
    return new_color


def open_file_dialog():
    myParams.original_image = askopenfile().name


def start():
    print("Start")
    if myParams.original_image:
        NapariWindow(labels_filepath, myParams)
    else:
        label_upload_file = tkinter.Label(root, font=("Helvetica", 28), bg="red", text='Please upload file!')
        label_upload_file.place(x=400, y=600)


def open_settings_window():
    global bg
    settings_window = tkinter.Toplevel(root)
    settings_window.title("Settings")
    img_settings = tkinter.Label(settings_window, image=bg).pack()

    bt_seg_colors_img = tkinter.PhotoImage(file="buttons_light/segmentation-colors.png")
    bt_seg_colors_img_dark = tkinter.PhotoImage(file="buttons_dark/segmentation-colors.png")
    seg_colors_label = tkinter.Label(settings_window, image=bt_seg_colors_img)
    seg_colors_label.place(x=100, y=32)

    bt_seg_opacity_img = tkinter.PhotoImage(file="buttons_light/segmentation-opacity.png")
    bt_seg_opacity_img_dark = tkinter.PhotoImage(file="buttons_dark/segmentation-opacity.png")
    seg_opacity_label = tkinter.Label(settings_window, image=bt_seg_opacity_img)
    seg_opacity_label.place(x=100, y=102)

    bt_seg_contour_img = tkinter.PhotoImage(file="buttons_light/segmentation-contour.png")
    bt_seg_contour_img_dark = tkinter.PhotoImage(file="buttons_dark/segmentation-contour.png")
    seg_contour_label = tkinter.Label(settings_window, image=bt_seg_contour_img)
    seg_contour_label.place(x=100, y=172)

    bt_img_opacity_img = tkinter.PhotoImage(file="buttons_light/image-opacity.png")
    bt_img_opacity_img_dark = tkinter.PhotoImage(file="buttons_dark/image-opacity.png")
    img_opacity_label = tkinter.Label(settings_window, image=bt_img_opacity_img)
    img_opacity_label.place(x=100, y=242)

    bt_img_gamma_img = tkinter.PhotoImage(file="buttons_light/image-gamma.png")
    bt_img_gamma_img_dark = tkinter.PhotoImage(file="buttons_dark/image-gamma.png")
    img_gamma_label = tkinter.Label(settings_window, image=bt_img_gamma_img)
    img_gamma_label.place(x=100, y=312)

    bt_border_color_img = tkinter.PhotoImage(file="buttons_light/border-color.png")
    bt_border_color_img_dark = tkinter.PhotoImage(file="buttons_dark/border-color.png")
    border_color_label = tkinter.Label(settings_window, image=bt_border_color_img)
    border_color_label.place(x=100, y=382)

    bt_border_width_img = tkinter.PhotoImage(file="buttons_light/border-width.png")
    bt_border_width_img_dark = tkinter.PhotoImage(file="buttons_dark/border-width.png")
    border_width_label = tkinter.Label(settings_window, image=bt_border_width_img)
    border_width_label.place(x=100, y=452)

    bt_text_color_img = tkinter.PhotoImage(file="buttons_light/text-color.png")
    bt_text_color_img_dark = tkinter.PhotoImage(file="buttons_dark/text-color.png")
    text_color_label = tkinter.Label(settings_window, image=bt_text_color_img)
    text_color_label.place(x=100, y=522)

    bt_text_size_img = tkinter.PhotoImage(file="buttons_light/text-size.png")
    bt_text_size_img_dark = tkinter.PhotoImage(file="buttons_dark/text-size.png")
    text_size_label = tkinter.Label(settings_window, image=bt_text_size_img)
    text_size_label.place(x=100, y=592)

    img_settings.pack()


root = tkinter.Tk()
root.geometry("1200x675")

bg = tkinter.PhotoImage(file="backgrounds/light.png")
bg_dark = tkinter.PhotoImage(file="backgrounds/dark.png")
img = tkinter.Label(root, image=bg)
img.pack()

bgexit = tkinter.PhotoImage("exit.png")

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

