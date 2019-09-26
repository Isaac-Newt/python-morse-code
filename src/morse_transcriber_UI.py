"""
Credits: Isaac List
Updated: July 2019
License: MPL2

A basic GUI front-end to a Morse Code decoder project,
built using GTK (Python GObject).
"""

# This Source Code Form is subject to the terms of the
# Mozilla Public License, v. 2.0. If a copy of the MPL
# was not distributed with this file, You can obtain
# one at https://mozilla.org/MPL/2.0/.

# GTK
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# Morse
from resources.morse import Coder


class MainWindow(Gtk.Window):
    """Create an application window"""

    def __init__(self):
        """Initialize Application"""
        # Create morse code tree
        # Path is dependent on CWD, so works if in project root
        self.morse_coder = Coder("src/resources/morse.txt")

        # Window title
        Gtk.Window.__init__(self, title="Morse Code Transcriber")

        # Window padding
        self.set_border_width(15)
        self.set_default_size(600, 150)
        self.main_area = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(self.main_area)

        # Build window contents
        self.build_main_view()

    def build_main_view(self):
        """Build the Page"""
        self.letters_to_morse = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)

        # Input form
        self.text_input = Gtk.Entry()
        # self.text_input = Gtk.TextView()
        # self.text_input_buffer = self.text_input.get_buffer()
        input_box = self.build_text_box("Enter Text:", self.text_input)
        self.letters_to_morse.pack_start(input_box, True, True, 0)

        # Submit button
        self.submit_button = Gtk.Button(label="Convert")
        self.submit_button.connect("clicked", self.display_morse)
        self.letters_to_morse.pack_start(self.submit_button, True, True, 0)

        # Output area
        self.morse_output = Gtk.Entry()
        self.morse_output.set_editable(False)
        output_box = self.build_text_box("Morse Transcription:", self.morse_output)
        self.letters_to_morse.pack_start(output_box, True, True, 0)

        self.main_area.pack_start(self.letters_to_morse, True, True, 0)

    def build_text_box(self, label_text: str, box_function):
        """Create a Gtk.Entry() element (i.e. text box)"""
        horizontal_box = Gtk.Box(spacing=8)
        box_label = Gtk.Label(label_text)
        horizontal_box.pack_start(box_label, True, True, 0)
        horizontal_box.pack_start(box_function, True, True, 0)
        return horizontal_box

    def to_morse(self, input_text: str):
        """Convert text to Morse Code"""
        code_string = self.morse_coder.encode(input_text)
        return code_string

    def display_morse(self, input_text):
        """Display converted text in the output box"""
        input_text = str(self.text_input.get_text())
        # input_text = str(self.text_input_buffer.get_text(self.text_input_buffer.get_start_iter(), self.text_input_buffer.get_end_iter(), True))
        input_text = input_text.lower()
        print(input_text)
        morse_string = self.to_morse(input_text)
        self.morse_output.set_text(morse_string)


WINDOW = MainWindow()
WINDOW.connect("delete-event", Gtk.main_quit)
WINDOW.show_all()
Gtk.main()
