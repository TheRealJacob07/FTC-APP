import PySimpleGUI as sg

def Match(api):
    layout = [  [sg.Text(api[0]['description']), sg.Text(api[0]['teams'][0]["teamNumber"]), sg.Text(api[0]['teams'][1]["teamNumber"]), sg.Text(api[0]['teams'][2]["teamNumber"]), sg.Text(api[0]['teams'][3]["teamNumber"])],
                [sg.Table((), api[0]['teams'][0]['teamNumber'])]]
    window = sg.Window('Test', layout)
    
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        