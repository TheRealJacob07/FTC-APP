import PySimpleGUI as sg

def Match(api):
    layout = [ [sg.Text(api['description'])]]
    window = sg.Window('Test', layout)
    
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        