import requests
import json

def get_data():
    # Get facebook status
    r = requests.get('https://api.ooni.io/api/v1/measurements?report_id=20210407T180249Z_facebookmessenger_UG_20294_n1_x71fmhkRPLbIJLsA')
    
    # convert the response to a python object
    json_data = json.loads(r.text)

    # retrieve the status. If its true it means the platform is inaccessible 
    print("..............................start.....................")
    print(json_data['results'][0]['anomaly']) 
    print(r.status_code)
    print("..............................end.....................")

    # Get Twitter status
    r2 = requests.get('https://api.ooni.io/api/v1/measurements?report_id=20210406T103932Z_webconnectivity_UG_36991_n1_B1JhJZjdOT2VihlG')
    
    # convert the response to a python object
    json_data2 = json.loads(r2.text)

    # retrieve the status. If its true it means the platform is inaccessible 
    print("..............................start.....................")
    print(json_data2['results'][0]['anomaly'])
    print(r2.status_code)
    print("..............................end.....................")

    return 0

# get_data()
