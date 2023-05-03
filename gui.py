import PySimpleGUI as sg

import functions
import time_format_functions

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[[label], [input_box, add_button]]])
window.read()
window.close()