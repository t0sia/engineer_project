import tkinter
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile

segments = [
    {"name": "LIVER", "color": "blue"},
    {"name": "BRAIN", "color": "red"},
    {"name": "LUNGS", "color": "yellow"},
    {"name": "BLADDER", "color": "green"},
    {"name": "KIDNEY", "color": "white"}
]

is_dark_mode = True
mode_button_text = 'Switch to light mode'


def dark_mode():
    global is_dark_mode
    ModeButton.config(text='Switch to dark mode' if is_dark_mode else 'Switch to light mode')
    is_dark_mode = not is_dark_mode


def color():
    new_color = askcolor()
    return new_color


def open_file_dialog():
    filename = askopenfile()
    print(filename)


root = tkinter.Tk()
root.geometry("2000x1220")


bg= tkinter.PhotoImage("bg_dark.png")
img= tkinter.Label(root, image=bg)
img.pack()

bgexit = tkinter.PhotoImage("exit.png")

ModeButton = tkinter.Button(root, text='Switch to light mode', command=dark_mode)
ModeButton.place(x=30, y=30)

UploadDialogButton = tkinter.Button(root, command=open_file_dialog, image=bgexit)
# UploadDialogButton.place(x=30, y=70)

tkinter.Label(root, text='Selected file: ').place(x=30, y=100)


for (i, segment) in enumerate(segments):
    print(segment['name'], segment['color'])
    tkinter.Label(root, text=segment['name']).place(x=30, y=130+i*100)
    tkinter.Canvas(root, bg=segment['color'], width=50, height=50).place(x=30, y=160+i*100 + 30)
    tkinter.Button(root, text="Change Color", command=color).place(x=30, y=190+i*100 + 60)

root.mainloop()
