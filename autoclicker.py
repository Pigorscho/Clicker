import tkinter as tk
from tkinter import ttk


class Example():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AutoClicker GUI")
        self.root.wm_geometry('950x500')
        self.root.resizable(width=False, height=False)

        # click interval widget
        self.click_interval = tk.Frame(self.root, bg="red", height=75)
        hours_input = tk.Entry(self.click_interval, width=5)
        mins_input = tk.Entry(self.click_interval, width=5)
        secs_input = tk.Entry(self.click_interval, width=5)
        millisecs_input = tk.Entry(self.click_interval, width=5)

        click_intervall_label = tk.Label(self.click_interval, text='Click Intervall :')

        hours_label = tk.Label(self.click_interval, text='hours')
        mins_label = tk.Label(self.click_interval, text='mins')
        secs_label = tk.Label(self.click_interval, text='secs')
        millisecs_label = tk.Label(self.click_interval, text='milliseconds')

        click_intervall_label.grid(row=1, column=1)
        hours_input.grid(row=2, column=1)
        hours_label.grid(row=2, column=2)
        mins_input.grid(row=2, column=3)
        mins_label.grid(row=2, column=4)
        secs_input.grid(row=2, column=5)
        secs_label.grid(row=2, column=6)
        millisecs_input.grid(row=2, column=7)
        millisecs_label.grid(row=2, column=8)

        self.click_interval.pack(fill='both', expand=True)



        # center click options
        self.center_click_options = tk.Frame(self.root, width=150, height=75, bg="cyan")
        ## click options
        self.click_options = tk.Frame(self.center_click_options, width=150, height=75, bg='yellow')
        ## click repeat
        self.click_repeat = tk.Frame(self.center_click_options, width=150, bg='green')
        ### click options content
        click_options_header_label = tk.Label(self.click_options, text='Click Options :')
        click_options_header_label.grid(row=0, column=1)

        mouse_button_label = tk.Label(self.click_options, text='Mouse Button :')
        mouse_button_label.grid(row=2, column=1)

        mouse_button_combo_box = ttk.Combobox(self.click_options, values=['Left',
                                                                          'Right',
                                                                          'Mousewheel'])
        mouse_button_combo_box.grid(row=2, column=2)
        mouse_button_combo_box.current(0)
# missing : comboExample.bind("<<ComboboxSelected>>", callbackFunc)
        click_type_header_label = tk.Label(self.click_options, text='Click Type :')
        click_type_header_label.grid(row=3, column=1)

        click_type_combo_box = ttk.Combobox(self.click_options, values=['Single',
                                                                        'Double'])
        click_type_combo_box.grid(row=4, column=2)
        click_type_combo_box.current(0)
# missing : comboExample.bind("<<ComboboxSelected>>", callbackFunc)

        click_type_label = tk.Label(self.click_options, text='Mouse Button :')
        click_type_label.grid(row=4, column=1)

        self.click_options.pack(side="left", fill="both", expand=True)
        self.click_repeat.pack(side="right", fill="both", expand=True)
        ## click repeat content
        click_repeat_header_label = tk.Label(self.click_repeat, text='Click Repeat :')
        click_repeat_header_label.grid(row=0, column=1)

        click_repeat_button = tk.Radiobutton(self.click_repeat, text='Repeat :', value=1)  # , variable=makro_button_on
        click_repeat_button.grid(row=1, column=1)

        click_repeat_combo_box = ttk.Combobox(self.click_repeat, values=['1', '2', '3', '4', '5'])
        click_repeat_combo_box.grid(row=1, column=2)
        click_repeat_combo_box.current(0)

        click_repeat_combo_box_label = tk.Label(self.click_repeat, text='times')
        click_repeat_combo_box_label.grid(row=2, column=2)

        repeat_until_stopped_button = tk.Radiobutton(self.click_repeat, text='Repeat until stopped', value=1)  # , variable=makro_button_on
        repeat_until_stopped_button.grid(row=3, column=1)



        # makro
        self.makro = tk.Frame(self.root, width=200, height=250)
        # makro frame 1
        self.makro_settings_frame = tk.Frame(self.makro, width=100, height=350, bg='blue')
        makro_radio_button = tk.Radiobutton(self.makro_settings_frame, text='Makro', value=1) # , variable=makro_button_on
        makro_radio_button.grid(row=0, column=0)
        # makro button aufnehmen
        record_makro = tk.Button(self.makro_settings_frame, text='REC')
        record_makro.grid(row=0, column=1)
        makro_combo_box = ttk.Combobox(self.makro_settings_frame, values=['Makro 1', 'Makro 2', 'Makro 3', 'Makro 4', 'Makro 5'])
        makro_combo_box.grid(row=1)
        makro_combo_box.current(0)
# missing : comboExample.bind("<<ComboboxSelected>>", callbackFunc)
        # makro frame 2
        self.makro_text_frame = tk.Frame(self.makro, width=100, height=350, bg='white')
        makro_rec_text_label = tk.Label(self.makro_text_frame, text='makros')
        makro_rec_text_label.pack()

        self.makro_settings_frame.pack(side="top", fill="both")
        self.makro_text_frame.pack(side="bottom", fill="both", expand=True)


        # special eff
        self.special_effects = tk.Frame(self.root, width=150, height=60, bg='orange')

        special_effect_button = tk.Radiobutton(self.special_effects, text='Cheatcode :', value=1)  # , variable=makro_button_on
        special_effect_button.grid(row=0, column=0)

        special_effect_combo_box = ttk.Combobox(self.special_effects,
                                       values=['Cheat 1', 'Cheat 2', 'Cheat 3', 'Cheat 4', 'Cheat 5'])
        special_effect_combo_box.grid(row=0, column=1)
        special_effect_combo_box.current(0)



        self.click_interval.grid(row=0, columnspan=2, rowspan=1, sticky='ew')
        self.center_click_options.grid(row=1, column=1, rowspan=2, sticky='nsew')
        self.makro.grid(row=0, column=2, rowspan=3, sticky='nsew')
        self.special_effects.grid(row=3, columnspan=3, rowspan=1, sticky='ew')



        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)


        self.root.mainloop()


Example()