import PySimpleGUI as sg
import api

username = "therealjacob07"
key = "E8F5637E-9AA2-4E1E-8132-90106C5BDB92" 

def Match(api, table, results, code):
    sg.theme("Topanga")
    
    layout = [  [sg.Table(table, ['Event', 'Team 1', "Color", "Team 2", 'Color', "Team 3", "Color", "Team 4", "Color"], alternating_row_color= 'Purple',expand_y=True ), sg.Image('qr.png')],
                [sg.Table(results, ['Event', 'Red Final', 'Red Auto', 'Red Penalty', 'Blue Final', 'Blue Auto', 'Blue Penalty'], alternating_row_color= 'Purple', expand_y=True)],
                [sg.Button('Close'), sg.Button('Refresh'), sg.Button('Event Details'), sg.Button("Rankings")]]
    
    
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
        if event == 'Event Details':
            eventDetails(code)
        if event == 'Rankings':
            rank(code)
            
    window.close()
        
def eventCode():
    sg.theme("Topanga")
    
    layout = [  [sg.DropDown(api.detailed(str(2023), username, key, str(9161)))],
                [sg.Button("Submit"), sg.Button("Cancel")]]
    
    window = sg.Window('Event Code', layout, element_justification='c')
    
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

def eventDetails(code):
    sg.theme("Topanga")
    
    data = api.event_details(str(2023), username, key, 9161, code)
    
    layout = [  [sg.Text("Event Name")],
                [sg.Text("Meet Name: " + data['name'])],
                [sg.Text(data['address'])],
                [sg.Text(data['city'])],
                [sg.Text("Meet Date: " + data['dateStart'])],
                [sg.Text('')],
                [sg.Text('Event Code: ' + data['code'])],
                [sg.Text('Event Type: ' + data['typeName'])],
                [sg.Text()]]
    
    window = sg.Window('Event Details', layout, element_justification='c')
    
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
    window.close()

def rank(code):
    data = api.rankings(str(2023), code, username, key)
    
    sg.theme("Topanga")
    
    layout = [  [sg.Table(data, ["Rank", "Team Number" ,"W-L-T", "TB1", "TB2", "TB3", "TB4", "TB5"], alternating_row_color= 'Purple', expand_y = True)]]
    
    window = sg.Window('Rankings', layout, element_justification='c')
    
    while True:
        event, value = window.read()
        if event == sg.WINDOW_CLOSED:
            break
    window.close()