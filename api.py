#Import required librarys
import requests
import json

def matchAPI(year, eventID, username, key, teamNum):

    req = requests.get("http://ftc-api.firstinspires.org/v2.0/" + year + "/matches/" + eventID, auth=(username, key), params={'teamNumber' : teamNum})

    data = req.json()

    jsondump = json.dumps(data, sort_keys= True)

    jsonloads = json.loads(jsondump)

    data_return = jsonloads['matches']

    return data_return

def filterData(data_return):
    description = []
    teams = []
    colorsa = []
    colorsb = []
    redFinal = []
    redAuto = []
    redFoul = []
    blueFinal = []
    blueAuto = []
    blueFoul = []
    k = 0
    for i in data_return:
        description.append(i["description"])
        redFinal.append(i["scoreRedFinal"])
        redAuto.append(i["scoreRedAuto"])
        redFoul.append(i["scoreRedFoul"])
        blueFinal.append(i["scoreBlueFinal"])
        blueAuto.append(i["scoreBlueAuto"])
        blueFoul.append(i["scoreBlueFoul"])
        
        for j in i['teams']:
            teams.append(j["teamNumber"])
            colorsa.append(j["station"])
    for i in colorsa:
        if i[0] == 'R':
            colorsb.append('Red')
        else:
            colorsb.append('Blue')
    re = []
    cl = []
    for i in range(int(len(teams)/4)):
        re.append([teams[0+(4*i)],teams[1+(i*4)],teams[2+(i*4)],teams[3+(i*4)]])
        cl.append([colorsb[0+(4*i)], colorsb[1+(4*i)], colorsb[2+(4*i)], colorsb[3+(4*i)]])
    
        
    temp = []
    temp2 = []
    for i in range(len(description)):
        temp.append([description[i], str(re[i][0]), str(cl[i][0]), str(re[i][1]), str(cl[i][1]), str(re[i][2]), str(cl[i][2]), str(re[i][3]), str(cl[i][3])])
        temp2.append([description[i], str(redFinal[i]), str(redAuto[i]), str(redFoul[i]), str(blueFinal[i]), str(blueAuto[i]), str(blueFoul[i])])
    
    return temp, temp2

def detailed(year, username, key, match):

    req = requests.get("http://ftc-api.firstinspires.org/v2.0/"+year+"/events", auth=(username, key), params={'teamnumber' : match})

    data = req.json()
    
    jsondump = json.dumps(data, sort_keys= True)

    jsonloads = json.loads(jsondump)

    data_return = jsonloads['events']
    
    values = []
    for i in data_return:
        values.append(i['code'])

    return values