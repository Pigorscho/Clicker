import tkinter as tk


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)




if __name__ == "__main__":
    app = SampleApp()
    window_width = 1500
    window_height = 800
    width = app.winfo_screenwidth()
    height = app.winfo_screenheight()
    app.geometry('%dx%d+%d+%d' % (window_width, window_height, width*0.5-(window_width/2), height*0.5-(window_height/2)))
    app.mainloop()