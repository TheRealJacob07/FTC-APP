import api
import window

#Register at https://ftc-events.firstinspires.org/services/API/register
username = "therealjacob07"
key = "E8F5637E-9AA2-4E1E-8132-90106C5BDB92"

def apiData():
    apicall = api.matchAPI(str(2023), window.eventCode(), username, key, '')
    
    filtered1, filtered2 = api.filterData(apicall)
    return apicall,filtered1,filtered2

def run():
    temp1, temp2, temp3 = apiData()

    window.Match(temp1, temp2, temp3)