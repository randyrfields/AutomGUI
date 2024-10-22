from tkinter import *
from tkinter import ttk


class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        self.title('Rexair Automation Controller')
        self.minsize(1000,600)
        text1 = self.Label(self, text="Label 1")
        text2 = self.Label(self, text="Label 2")
        text3 = self.Label(self, text="Label 3")
        text4 = self.Label(self, text="Label 4")

        # Place widgets in the grid using tkinter's grid manager
        text1.grid(row=0, column=0)
        text2.grid(row=1, column=0, columnspan=2)
        text3.grid(row=0, column=1)


def main():
    root = Root()
    root.mainloop()


if __name__=="__main__":
    main()