import tkinter as tk
from tkinter import ttk
import sv_ttk
from PIL import Image, ImageTk

# root = tk.Tk()

# button = ttk.Button(root, text="Button")
# button.pack()

# sv_ttk.use_dark_theme()
# sv_ttk.use_light_theme()


def main():
    mainWindow = tk.Tk()
    mainWindow.title("Rexair Automation Controller")
    # mainWindow.attributes('-fullscreen', True)
    mainWindowWidth = mainWindow.winfo_screenwidth()
    mainWindowHeight = mainWindow.winfo_screenheight()
    mainWindow.geometry(f"{mainWindowWidth}x{mainWindowHeight}+0+0")
    image = Image.open("Rexair-LLC.png")
    image = image.resize((int(mainWindowWidth/2), int(mainWindowHeight/2)))
    image = ImageTk.PhotoImage(image)
    bg_label = tk.Label(mainWindow, image = image)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = image
    label = ttk.Label(mainWindow, text="Scan Results")
    label.pack(side='top')


    scanResultsPane = ttk.Frame(mainWindow, relief='raised', borderwidth=1, width=int(mainWindowWidth/4), height=int(mainWindowHeight))
    scanResultsPane.pack_propagate(False)
    scanResultsPane.pack(side='left')
    scanButton = ttk.Button(scanResultsPane, text='Scan')
    scanButton.pack(side="bottom")

    sv_ttk.set_theme("dark")
 
    mainWindow.mainloop()


if __name__=="__main__":
    main()