import PySimpleGUI as sg

def Match(api, table, results):
    sg.theme("DarkPurple1")
    
    layout = [  [sg.Text(api[0]['description']), sg.Text(api[0]['teams'][0]["teamNumber"]), sg.Text(api[0]['teams'][1]["teamNumber"]), sg.Text(api[0]['teams'][2]["teamNumber"]), sg.Text(api[0]['teams'][3]["teamNumber"])],
                [sg.Table(table, ['Event', 'Team 1', "Color", "Team 2", 'Color', "Team 3", "Color", "Team 4", "Color"], alternating_row_color= 'Purple' )],
                [sg.Table(results, ['Event', 'Red Fianl', 'Red Auto', 'Red Penalty', 'Blue Final', 'Blue Auto', 'Blue Penalty'])]]
    
    
    window = sg.Window('Test', layout, )
    
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        