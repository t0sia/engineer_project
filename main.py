import tkinter
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
from napari_window import NapariWindow
from params import Params
from settings_window import SettingsWindow

is_dark_mode = False
labels_filepath = "./labels-31.nii.gz"
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
        DownloadButton.config(image=bt_download_img_dark)
        is_dark_mode = True
    else:
        img.config(image=bg)
        StartButton.config(image=bt_start_img)
        AddFileButton.config(image=bt_add_file_img)
        InstructionDialogButton.config(image=bt_instruction_img)
        SettingsButton.config(image=bt_settings_img)
        DarkModeButton.config(image=bt_mode_img)
        DownloadButton.config(image=bt_download_img)
        is_dark_mode = False


def open_file_dialog():
    myParams.original_image = askopenfile().name


def open_instructions_dialog():
    instructions_window = tkinter.Toplevel()
    instructions_window.configure(bg="black")
    instructions_window.geometry("800x500")
    tkinter.Label(
        instructions_window,
        font=("Helvetica", 16),
        bg="black",
        fg="white",
        text="After launching the application, you should upload a NIfTI file\n containing tomographic images. This will enable the application\n to utilize a neural network for segmentation. Alternatively, there\n is an option to add pre-existing images with already labeled\n organ regions. The next step involves adjusting the display parameters\n of the segmented images. This can be done in a window\n that appears after clicking the SETTINGS button in the main menu.\n You can customize colors, font size, frame width around organs,\n as well as gamma and image transparency parameters according\n to their preferences. To view the performed segmentations, simply\n click the START button in the main menu. A window will then\n appear where you can browse images with highlighted organs using\n a slider located at the bottom of the screen. The application\n allows the download of generated labels by clicking the\n DOWNLOAD button. You can choose the file name and save path in the system.\n Additionally, there is an option to change the visual theme using the\n DARK MODE and LIGHT MODE buttons.",
    ).place(x=20, y=20)


def start():
    myParams.print_params(myParams)
    if myParams.original_image:
        NapariWindow(labels_filepath, myParams)
    else:
        label_upload_file = tkinter.Label(
            root, font=("Helvetica", 32), bg="red", text="Please upload file!"
        )
        label_upload_file.place(x=420, y=600)


def open_seg_color_settings(seg):
    seg = askcolor()


def open_settings_window():
    settings_window = SettingsWindow(is_dark_mode=is_dark_mode, params=myParams)
    settings_window.open()


def download():
    print("pobieranko tralalalal")


if __name__ == "__main__":
    root = tkinter.Tk()
    root.geometry("1200x675")

    bg = tkinter.PhotoImage(file="backgrounds/light.png")
    bg_dark = tkinter.PhotoImage(file="backgrounds/dark.png")

    img = tkinter.Label(root, image=bg)
    img.pack()

    bt_start_img = tkinter.PhotoImage(file="buttons_light/start.png")
    bt_start_img_dark = tkinter.PhotoImage(file="buttons_dark/start.png")
    StartButton = tkinter.Button(root, command=start, image=bt_start_img, bd=0)
    StartButton.place(x=400, y=35)

    bt_add_file_img = tkinter.PhotoImage(file="buttons_light/add-file.png")
    bt_add_file_img_dark = tkinter.PhotoImage(file="buttons_dark/add-file.png")
    AddFileButton = tkinter.Button(
        root, command=open_file_dialog, image=bt_add_file_img, bd=0
    )
    AddFileButton.place(x=400, y=125)

    bt_settings_img = tkinter.PhotoImage(file="buttons_light/settings.png")
    bt_settings_img_dark = tkinter.PhotoImage(file="buttons_dark/settings.png")
    SettingsButton = tkinter.Button(
        root, command=open_settings_window, image=bt_settings_img, bd=0
    )
    SettingsButton.place(x=400, y=215)

    bt_instruction_img = tkinter.PhotoImage(file="buttons_light/instruction.png")
    bt_instruction_img_dark = tkinter.PhotoImage(file="buttons_dark/instruction.png")
    InstructionDialogButton = tkinter.Button(
        root, command=open_instructions_dialog, image=bt_instruction_img, bd=0
    )
    InstructionDialogButton.place(x=400, y=305)

    bt_mode_img = tkinter.PhotoImage(file="buttons_light/dark-mode.png")
    bt_mode_img_dark = tkinter.PhotoImage(file="buttons_dark/light-mode.png")
    DarkModeButton = tkinter.Button(root, command=dark_mode, image=bt_mode_img, bd=0)
    DarkModeButton.place(x=400, y=395)

    bt_download_img = tkinter.PhotoImage(file="buttons_light/download.png")
    bt_download_img_dark = tkinter.PhotoImage(file="buttons_dark/download.png")
    DownloadButton = tkinter.Button(root, command=download, image=bt_download_img, bd=0)
    DownloadButton.place(x=400, y=485)

    root.mainloop()
