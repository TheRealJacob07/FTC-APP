import PySimpleGUI as sg
import main
def Match(api, table, results):
    sg.theme("Topanga")
    
    layout = [  [sg.Table(table, ['Event', 'Team 1', "Color", "Team 2", 'Color', "Team 3", "Color", "Team 4", "Color"], alternating_row_color= 'Purple' )],
                [sg.Table(results, ['Event', 'Red Final', 'Red Auto', 'Red Penalty', 'Blue Final', 'Blue Auto', 'Blue Penalty'])],
                [sg.Button('Close'), sg.Button('Refresh')]]
    
    
    window = sg.Window('First App', layout, finalize=True, element_justification='c')
    window.Maximize()
    
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == 'Close':
            break
        if event == 'Refresh':
            window.close()
            main.run()
            
    window.close()
        
def eventCode():
    sg.theme("Topanga")
    
    layout = [  [sg.Input("Enter the Event Code: ")],
                [sg.Button("Submit"), sg.Button("Cancel")]]
    
    window = sg.Window('Event Code', layout)
    
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        if event == "Cancel":
            break
        if event == 'Submit':
            window.close()
            return value[0]
    window.close()
        