#Import required librarys
import requests
import json

def matchAPI(year, eventID, username, key, teamNum):
    #Get match data for specified year, event, team, and match number.

    # Create request for specified match data
    req = requests.get("http://ftc-api.firstinspires.org/v2.0/" + year + "/matches/" + eventID, auth=(username, key), params={'teamNumber' : teamNum})

    # Convert request data to JSON format
    data = req.json()

    # Dump JSON data to string, sort keys
    jsondump = json.dumps(data, sort_keys= True)

    # Load JSON data from string
    jsonloads = json.loads(jsondump)

    # Get the match data for the specified match number
    data_return = jsonloads['matches']

    # Return the match data
    return data_return
    