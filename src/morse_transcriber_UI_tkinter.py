#!/usr/bin/python3

"""
TKInter version of morse code transcriber
"""

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL
# was not distributed with this file, You can obtain
# one at https://mozilla.org/MPL/2.0/.

import tkinter


class MainWindow:
    """Build the application window"""

    def __init__(self):
        """__init__"""
        self.window = tkinter.Tk()
        self.build_main_view()

    def build_main_view(self):
        """Build the main application view"""
        self.main_view = tkinter.Frame(self.window)
        self.main_view.pack()

        text_frame, morse_frame = self.build_inputs()
        text_frame.pack(side=tkinter.LEFT)
        morse_frame.pack(side=tkinter.RIGHT)

        button_frame = self.build_buttons()
        button_frame.pack(side=tkinter.LEFT)

    def build_inputs(self):
        """Build the text and morse in/out puts"""
        text_frame = tkinter.Frame(self.main_view)
        text_box_label = tkinter.Label(text_frame, text="Enter Text:", fg="blue")
        text_box_label.pack(side=tkinter.TOP)
        self.text_box = tkinter.Entry(text_frame)
        self.text_box.pack(side=tkinter.TOP)

        morse_frame = tkinter.Frame(self.main_view)
        morse_box_label = tkinter.Label(
            morse_frame, text="Morse Transcription", fg="red"
        )
        morse_box_label.pack(side=tkinter.TOP)
        self.morse_box = tkinter.Entry(morse_frame)
        self.morse_box.pack(side=tkinter.TOP)

        return text_frame, morse_frame

    def build_buttons(self):
        """Build the buttons in the UI"""
        button_frame = tkinter.Frame(self.main_view)

        self.transcribe_button = tkinter.Button(
            button_frame, text="Convert", command=self.display_morse
        )
        self.transcribe_button.pack(side=tkinter.TOP)

        self.change_input_button = tkinter.Button(
            button_frame, text="Change Input", command=self.change_input
        )
        self.change_input_button.pack(side=tkinter.BOTTOM)

        return button_frame

    def display_morse(self):
        """Display morse transcription of text input"""
        print("Display Morse")

    def change_input(self):
        """Change input source"""
        print("Change Input")


WINDOW = MainWindow()
WINDOW.window.mainloop()
