import tkinter
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile
from napari_window import NapariWindow

from params import Params
from save_segmentation_window import SaveSegmentationWindow
from settings_window import SettingsWindow

is_dark_mode = False
myParams = Params


def dark_mode():
    global is_dark_mode
    if not is_dark_mode:
        img.config(image=bg_dark)
        StartButton.config(image=bt_start_img_dark)
        AddFileButton.config(image=bt_add_file_img_dark)
        UploadModelButton.config(image=bt_upload_model_img_dark)
        InstructionDialogButton.config(image=bt_instruction_img_dark)
        SettingsButton.config(image=bt_settings_img_dark)
        DarkModeButton.config(image=bt_mode_img_dark)
        DownloadButton.config(image=bt_download_img_dark)
        is_dark_mode = True
    else:
        img.config(image=bg)
        StartButton.config(image=bt_start_img)
        AddFileButton.config(image=bt_add_file_img)
        UploadModelButton.config(image=bt_upload_model_img)
        InstructionDialogButton.config(image=bt_instruction_img)
        SettingsButton.config(image=bt_settings_img)
        DarkModeButton.config(image=bt_mode_img)
        DownloadButton.config(image=bt_download_img)
        is_dark_mode = False


def open_file_dialog():
    myParams.original_image = askopenfile().name


def open_file_dialog_prim():
    myParams.segmentation = askopenfile().name


def open_instructions_dialog():
    instructions_window = tkinter.Toplevel()
    instructions_window.configure(bg="black")
    instructions_window.geometry("600x600")
    tkinter.Label(
        instructions_window,
        font=("Helvetica", 16),
        bg="black",
        fg="white",
        text="jakaś instrukcja bla bla bla",
    ).place(x=20, y=20)


def start(root):
    myParams.print_params(myParams)
    if myParams.original_image:
        if not myParams.segmentation:
            save_segmentation_window = SaveSegmentationWindow(is_dark_mode=is_dark_mode, params=myParams)
            save_segmentation_window.open()
        else:
            NapariWindow(myParams)
    else:
        label_upload_file = tkinter.Label(
            root, font=("Helvetica", 16), bg="red", text="Please upload file!"
        )
        label_upload_file.place(x=400, y=600)


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
    StartButton = tkinter.Button(root, command=lambda: start(root), image=bt_start_img, bd=0)
    StartButton.place(x=400, y=35)

    bt_add_file_img = tkinter.PhotoImage(file="buttons_light/add-file.png")
    bt_add_file_img_dark = tkinter.PhotoImage(file="buttons_dark/add-file.png")
    AddFileButton = tkinter.Button(
        root, command=open_file_dialog, image=bt_add_file_img, bd=0
    )
    AddFileButton.place(x=400, y=115)

    bt_upload_model_img = tkinter.PhotoImage(file="buttons_light/upload-model.png")
    bt_upload_model_img_dark = tkinter.PhotoImage(file="buttons_dark/upload-model-button-dark.png")
    UploadModelButton = tkinter.Button(
        root, command=open_file_dialog_prim, image=bt_upload_model_img, bd=0
    )
    UploadModelButton.place(x=400, y=195)

    bt_settings_img = tkinter.PhotoImage(file="buttons_light/settings.png")
    bt_settings_img_dark = tkinter.PhotoImage(file="buttons_dark/settings.png")
    SettingsButton = tkinter.Button(
        root, command=open_settings_window, image=bt_settings_img, bd=0
    )
    SettingsButton.place(x=400, y=275)

    bt_instruction_img = tkinter.PhotoImage(file="buttons_light/instruction.png")
    bt_instruction_img_dark = tkinter.PhotoImage(file="buttons_dark/instruction.png")
    InstructionDialogButton = tkinter.Button(
        root, command=open_instructions_dialog, image=bt_instruction_img, bd=0
    )
    InstructionDialogButton.place(x=400, y=355)

    bt_mode_img = tkinter.PhotoImage(file="buttons_light/dark-mode.png")
    bt_mode_img_dark = tkinter.PhotoImage(file="buttons_dark/light-mode.png")
    DarkModeButton = tkinter.Button(root, command=dark_mode, image=bt_mode_img, bd=0)
    DarkModeButton.place(x=400, y=435)

    bt_download_img = tkinter.PhotoImage(file="buttons_light/download.png")
    bt_download_img_dark = tkinter.PhotoImage(file="buttons_dark/download.png")
    DownloadButton = tkinter.Button(root, command=download, image=bt_download_img, bd=0)
    DownloadButton.place(x=400, y=505)

    root.mainloop()
