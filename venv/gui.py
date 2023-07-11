import functions
import PySimpleGUI as psg

input = psg.InputText(tooltip='Enter todo')
label = psg.Text('Type in a to-do')
add_button = psg.Button('Add')
win = psg.Window('My To-Do App', layout = [[label],[input,add_button]])
win.read()
win.close()
