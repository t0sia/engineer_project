import tkinter
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
# from napari_window import NapariWindow
from params import Params
from settings_window import SettingsWindow

is_dark_mode = False
labels_filepath = './labels-31.nii'
myParams = Params


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



def open_file_dialog():
    myParams.original_image = askopenfile().name


def start():
    myParams.print_params(myParams)
    if myParams.original_image:
        print('start napari')
        # NapariWindow(labels_filepath, myParams)
    else:
        label_upload_file = tkinter.Label(root, font=("Helvetica", 28), bg="red", text='Please upload file!')
        label_upload_file.place(x=400, y=600)


def open_seg_color_settings(seg):
    seg = askcolor()


def open_seg_colors_dialog():
    global is_dark_mode, myParams
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
    settings_window = SettingsWindow(is_dark_mode=is_dark_mode, params=myParams, root=root)
    settings_window.open()


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

