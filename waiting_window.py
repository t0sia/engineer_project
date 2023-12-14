import tkinter
from model_inferer import infer_with_model


class WaitingWindow:
    def __init__(self, params, is_dark_mode):
        self.params = params
        self.is_dark_mode = is_dark_mode

        self.waiting_window = tkinter.Toplevel()
        self.waiting_window.geometry("1200x675")

        self.bg = (
            tkinter.PhotoImage(file="backgrounds/dark.png")
            if self.is_dark_mode
            else tkinter.PhotoImage(file="backgrounds/light.png")
        )

        self.waiting_window.title("Waiting")
        img_bg = tkinter.Label(self.waiting_window, image=self.bg)
        img_bg.pack()

    def open_and_process(self):
        label_wait = tkinter.Label(
            self.waiting_window, font=("Helvetica", 16),
            text="Please wait\n"
                 "Thank you for making a little script happy :)"
        )
        label_wait.place(x=280, y=80)

        self.waiting_window.update()

        try:
            self.process()
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            self.destroy()

    def process(self):
        _result, self.params.segmentation = infer_with_model(
            self.params.original_image, self.params.path_to_save
        )

    def destroy(self):
        self.waiting_window.destroy()
