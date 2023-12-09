import PySimpleGUI as sg
import api

username = "therealjacob07"
key = "E8F5637E-9AA2-4E1E-8132-90106C5BDB92" 

def Match(api, table, results, code):
    sg.theme("Topanga")
    
    layout = [  [sg.Table(table, ['Event', 'Team 1', "Color", "Team 2", 'Color', "Team 3", "Color", "Team 4", "Color"], alternating_row_color= 'Purple',expand_y=True ), sg.Image('qr.png')],
                [sg.Table(results, ['Event', 'Red Final', 'Red Auto', 'Red Penalty', 'Blue Final', 'Blue Auto', 'Blue Penalty'], alternating_row_color= 'Purple', expand_y=True)],
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
            temp1, temp2, temp3, code = apiData(code)
            Match(temp1, temp2, temp3, code)
            
    window.close()
        
def eventCode():
    sg.theme("Topanga")
    
    layout = [  [sg.DropDown(api.detailed(str(2023), username, key, str(9161)))],
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
    
def apiData(code):
    apicall = api.matchAPI(str(2023), code, username, key, '')
    filtered1, filtered2 = api.filterData(apicall)
    return apicall,filtered1,filtered2, code
        