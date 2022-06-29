import tkinter as tk
from tkinter import ttk

class  MainFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(self, container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

class InputFrame(ttk.Frame):
    def __init__(self, container, ):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        self.__create_widgets()



if __name__ == "__main__":
    app = App()
    app.mainloop()
