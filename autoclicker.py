import tkinter as tk
from tkinter import ttk


class Example():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("AutoClicker GUI")
        self.root.wm_geometry('950x400')
        #self.root.resizable(width=False, height=False)

        # click interval widget
        self.click_interval = tk.Frame(self.root, bg="red", height=75, padx=10, pady=10)
        self.click_interval_frame = tk.Frame(self.click_interval, bg="blue violet", height=75, padx=10, pady=10)
        hours_input = tk.Entry(self.click_interval_frame, width=5,)
        mins_input = tk.Entry(self.click_interval_frame, width=5)
        secs_input = tk.Entry(self.click_interval_frame, width=5)
        millisecs_input = tk.Entry(self.click_interval_frame, width=5)

        click_intervall_label = tk.Label(self.click_interval_frame, text='Click Intervall :')

        hours_label = tk.Label(self.click_interval_frame, text='hours', padx=30)
        mins_label = tk.Label(self.click_interval_frame, text='mins', padx=30)
        secs_label = tk.Label(self.click_interval_frame, text='secs', padx=30)
        millisecs_label = tk.Label(self.click_interval_frame, text='milliseconds', padx=30)

        click_intervall_label.pack()
        hours_input.pack(side='left', expand=True)
        hours_label.pack(side='left', expand=True)
        mins_input.pack(side='left', expand=True)
        mins_label.pack(side='left', expand=True)
        secs_input.pack(side='left', expand=True)
        secs_label.pack(side='left', expand=True)
        millisecs_input.pack(side='left', expand=True)
        millisecs_label.pack(side='left', expand=True)

        self.click_interval.pack(fill='both', expand=True)
        self.click_interval_frame.pack()



        # center click options
        self.center_click_options = tk.Frame(self.root, width=150, height=75, bg="lightblue", padx=10, pady=10)
        ## click options
        self.click_options = tk.Frame(self.center_click_options, width=150, height=75, bg='yellow', padx=10, pady=10)
        ## click repeat
        self.click_repeat = tk.Frame(self.center_click_options, width=150, bg='green', padx=10, pady=10)
        ### click options content (click_options & click_type)
        self.click_options_frame = tk.Frame(self.click_options, width=150, height=75, bg='cyan', padx=10, pady=10)
        click_options_header_label = tk.Label(self.click_options_frame, text='Click Options :')
        click_options_header_label.grid(row=0, column=0)

        mouse_button_label = tk.Label(self.click_options_frame, text='Mouse Button :')
        mouse_button_label.grid(row=1, column=0)

        mouse_button_combo_box = ttk.Combobox(self.click_options_frame, values=['Left',
                                                                          'Right',
                                                                          'Mousewheel'])
        mouse_button_combo_box.grid(row=1, column=1)
        mouse_button_combo_box.current(0)
# missing : comboExample.bind("<<ComboboxSelected>>", callbackFunc)
        click_type_header_label = tk.Label(self.click_options_frame, text='Click Type :')
        click_type_header_label.grid(row=2, column=0)

        click_type_combo_box = ttk.Combobox(self.click_options_frame, values=['Single',
                                                                        'Double'])
        click_type_combo_box.grid(row=2, column=1)
        click_type_combo_box.current(0)
# missing : comboExample.bind("<<ComboboxSelected>>", callbackFunc)



        self.click_options.pack(side="left", fill="both", expand=True)
        self.click_repeat.pack(side="right", fill="both", expand=True)
        self.click_options_frame.pack()
        ## click repeat window
        self.click_repeat_frame_all = tk.Frame(self.click_repeat, width=150, height=75, bg='gold', padx=10, pady=10)
        ## click repeat content

        self.click_repeat_frame = tk.Frame(self.click_repeat_frame_all, width=150, height=75, bg='purple', padx=10, pady=10)
        click_repeat_header_label = tk.Label(self.click_repeat_frame, text='Click Repeat :')
        click_repeat_header_label.grid(row=0, column=0)

        click_repeat_button = tk.Radiobutton(self.click_repeat_frame, text='Repeat :', value=1)  # , variable=makro_button_on
        click_repeat_button.grid(row=1, column=0)

        click_repeat_combo_box = ttk.Combobox(self.click_repeat_frame, values=['1', '2', '3', '4', '5'], width=5)
        click_repeat_combo_box.grid(row=1, column=1)
        click_repeat_combo_box.current(0)

        click_repeat_combo_box_label = tk.Label(self.click_repeat_frame, text='times')
        click_repeat_combo_box_label.grid(row=1, column=2)

        # repeat_until_stopped_frame
        self.repeat_until_stopped_frame = tk.Frame(self.click_repeat_frame_all, width=250, height=75, bg='limegreen', padx=10, pady=10)
        repeat_until_stopped_button = tk.Radiobutton(self.repeat_until_stopped_frame, text='Repeat until stopped', value=1)  # , variable=makro_button_on
        repeat_until_stopped_button.grid(row=0, column=0)

        self.click_repeat_frame_all.pack()
        self.click_repeat_frame.pack()
        self.repeat_until_stopped_frame.pack()



        # makro
        self.makro = tk.Frame(self.root, width=200, height=250, bg='brown', padx=10, pady=10)
        # makro frame 1
        self.makro_settings_frame = tk.Frame(self.makro, width=100, height=350, bg='blue', padx=10, pady=10)
        makro_radio_button = tk.Radiobutton(self.makro_settings_frame, text='Makro', value=1) # , variable=makro_button_on
        makro_radio_button.grid(row=0, column=0)
        # makro button aufnehmen
        record_makro = tk.Button(self.makro_settings_frame, text='REC')
        record_makro.grid(row=0, column=1)
        makro_combo_box = ttk.Combobox(self.makro_settings_frame, values=['Makro 1', 'Makro 2', 'Makro 3', 'Makro 4', 'Makro 5'])
        makro_combo_box.grid(row=1, columnspan=2)
        makro_combo_box.current(0)
# missing : comboExample.bind("<<ComboboxSelected>>", callbackFunc)
        # makro frame 2
        self.makro_text_frame = tk.Frame(self.makro, width=100, height=350, bg='white', padx=10, pady=10)
        makro_rec_text_label = tk.Label(self.makro_text_frame, text='makros')
        makro_rec_text_label.pack()

        self.makro_settings_frame.pack(side="top", fill="both")
        self.makro_text_frame.pack(side="bottom", fill="both", expand=True)


        # special eff
        self.special_effects = tk.Frame(self.root, width=150, height=60, bg='orange', padx=10, pady=10)
        self.special_effects_frame = tk.Frame(self.special_effects, width=150, height=60, bg='white', padx=10, pady=10)

        special_effect_button = tk.Radiobutton(self.special_effects_frame, text='Cheatcode :', value=1)  # , variable=makro_button_on
        special_effect_button.grid(column=0, row=0)

        special_effect_combo_box = ttk.Combobox(self.special_effects_frame,
                                       values=['Cheat 1', 'Cheat 2', 'Cheat 3', 'Cheat 4', 'Cheat 5'])
        special_effect_combo_box.grid(column=1, row=0)
        special_effect_combo_box.current(0)

        self.special_effects_frame.pack()

        # handle button frame
        self.handle_button = tk.Frame(self.root, width=150, height=200, bg='lightgray', padx=10, pady=10)
        self.handle_button_frame = tk.Frame(self.handle_button, width=150, height=200, bg='black', padx=10, pady=10)

        start_button = tk.Button(self.handle_button_frame, text='START')
        stop_button = tk.Button(self.handle_button_frame, text='STOP')
        hotkey_settings_button = tk.Button(self.handle_button_frame, text='Hotkey Setting')

        start_button.grid(column=1, row=0)
        stop_button.grid(column=2, row=0)
        hotkey_settings_button.grid(column=3, row=0)

        self.handle_button_frame



        self.handle_button_frame.pack()



        self.click_interval.grid(row=0, columnspan=2, rowspan=1, sticky='ew')
        self.center_click_options.grid(row=1, column=1, rowspan=2, sticky='nsew')
        self.makro.grid(row=0, column=2, rowspan=3, sticky='nsew')
        self.special_effects.grid(row=3, columnspan=3, rowspan=1, sticky='ew')
        self.handle_button.grid(row=4, columnspan=3, rowspan=1, sticky='nsew')



        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(1, weight=1)


        self.root.mainloop()


Example()