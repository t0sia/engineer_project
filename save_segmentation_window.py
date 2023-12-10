import tkinter
from tkinter import filedialog
from napari_window import NapariWindow
from waiting_window import WaitingWindow


class SaveSegmentationWindow:
    def __init__(self, params, is_dark_mode):
        self.params = params
        self.is_dark_mode = is_dark_mode

        self.save_segmentation_window = tkinter.Toplevel()
        self.save_segmentation_window.geometry("1200x675")
        self.save_segmentation_window.protocol('WM_DELETE_WINDOW', self.close_and_process)

        self.bg = (
            tkinter.PhotoImage(file="backgrounds/dark.png")
            if self.is_dark_mode
            else tkinter.PhotoImage(file="backgrounds/light.png")
        )

        self.browse_img = (
            tkinter.PhotoImage(file="buttons_dark/browse.png")
            if self.is_dark_mode
            else tkinter.PhotoImage(file="buttons_light/browse.png")
        )

        self.save_img = (
            tkinter.PhotoImage(file="buttons_dark/save.png")
            if self.is_dark_mode
            else tkinter.PhotoImage(file="buttons_light/save.png")
        )

        self.save_segmentation_window.title("Save labels")
        img_bg = tkinter.Label(self.save_segmentation_window, image=self.bg)
        img_bg.pack()

    def open(self):
        label_save_segmentation_question = tkinter.Label(
            self.save_segmentation_window, font=("Helvetica", 16),
            text="If you wish to save segmentation labels, please specify a path for saving.\n"
                 "Alternatively, you can close the window and proceed without saving."
        )
        label_save_segmentation_question.place(x=170, y=80)

        label_enter_path = tkinter.Label(
            self.save_segmentation_window, font=("Helvetica", 16),
            text="Enter Path: "
        )
        label_enter_path.place(x=170, y=240)

        path_entry = tkinter.Entry(self.save_segmentation_window, width=58, font=("Helvetica", 16))
        path_entry.place(x=170, y=280)

        browse_button = tkinter.Button(self.save_segmentation_window,
                                       command=lambda: self.browse_path(path_entry),
                                       image=self.browse_img)
        browse_button.place(x=170, y=350)

        save_button = tkinter.Button(self.save_segmentation_window,
                                     command=lambda: self.save_path(path_entry),
                                     image=self.save_img)
        save_button.place(x=640, y=350)

        self.save_segmentation_window.mainloop()

    @staticmethod
    def browse_path(path_entry):
        path = filedialog.askdirectory()
        path_entry.delete(0, tkinter.END)
        path_entry.insert(0, path)

    def save_path(self, path_entry):
        self.params.path_to_save = path_entry.get()
        print(self.params.path_to_save)

    def close_and_process(self):
        self.save_segmentation_window.destroy()
        if not self.params.segmentation:
            waiting_window = WaitingWindow(self.params, self.is_dark_mode)
            waiting_window.open_and_process()

        NapariWindow(self.params)
