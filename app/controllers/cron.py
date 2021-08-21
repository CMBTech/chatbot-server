import requests
import json
from app.schemas.platform import PlatformSchema
from app.models.platform import Platform
import datetime
from flask_restful import Resource

class CronView(Resource):
    def patch(self):
        get_data()

        return dict(
            status="success",
            message=f"Platform updated successfully"
            ), 200

def get_data():
    # Get facebook status
    r = requests.get('https://api.ooni.io/api/v1/measurements?report_id=20210407T180249Z_facebookmessenger_UG_20294_n1_x71fmhkRPLbIJLsA')
    
    # convert the response to a python object
    json_data = json.loads(r.text)

    # retrieve the status. If its true it means the platform is inaccessible 
    print("..............................start.....................")
    print(json_data['results'][0]['anomaly']) 
    print(r.status_code)
    fb_status = json_data['results'][0]['anomaly']
    save2db(2,fb_status)
    


    print("..............................end.....................")

    # Get Twitter status
    r2 = requests.get('https://api.ooni.io/api/v1/measurements?report_id=20210406T103932Z_webconnectivity_UG_36991_n1_B1JhJZjdOT2VihlG')
    
    # convert the response to a python object
    json_data2 = json.loads(r2.text)

    # retrieve the status. If its true it means the platform is inaccessible 
    print("..............................start.....................")
    print(json_data2['results'][0]['anomaly'])
    print(r2.status_code)
    twt_status = json_data2['results'][0]['anomaly']

    save2db(1,twt_status)
    print("..............................end.....................")

    return 0




def save2db(id, n_status):
    print("Am in .... yeysssss!!!")
    status_date = datetime.datetime.now().isoformat()
    # print(now)
    # status_date = now.strftime(" %d-%m-%Y %H:%M")
    # print("Here is the current date",status_date)
    print(status_date)
    data = dict(status=n_status, status_date=status_date)
    print(data)

    platform_schema = PlatformSchema()
    validated_platform_data, errors = platform_schema.load(data, partial=("name",))


    if errors:
        print(errors)
        
    platform = Platform.get_by_id(id)
    if not platform:
        print("platform doest exist")
    if 'status' in validated_platform_data:
        platform.status = validated_platform_data['status']

    if 'status_date' in validated_platform_data:
        platform.status_date = validated_platform_data['status_date']
    
    updated_platform = platform.save()
    print(updated_platform)

    if not updated_platform:
        print("Sarri failed to update")

    print("Status successfuly updated!!!")
    # return dict(
    #         status="success",
    #         message=f"Platform status updated successfully"
    #         ), 200

# get_data()