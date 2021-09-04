import requests
import json
from app.schemas.platform import PlatformSchema
from app.models.platform import Platform
import datetime
from flask_restful import Resource

class CronView(Resource):
    def patch(self):

        platform_schema = PlatformSchema(many=True)
        platforms = Platform.find_all()

        platform_data, errors = platform_schema.dumps(platforms)

        if errors:
            return dict(status='fail', message=errors), 500

        platform_data_list = json.loads(platform_data)
        for platform in platform_data_list:
            print(platform['report_id'])
            get_data(platform['id'],platform['report_id'])

        return dict(
            status="success",
            message=f" All Platforms updated successfully"
            ), 200

def get_data(id,report_id):  
    print("..............................start retrieving status.....................")
    # Get platform status
    url = f'https://api.ooni.io/api/v1/measurements?report_id={report_id}'
    r2 = requests.get(url)
    
    # convert the response to a python object
    json_data2 = json.loads(r2.text)

    # retrieve the status. If its true it means the platform is inaccessible 
    
    platform_status = json_data2['results'][0]['anomaly']

    save2db(id,platform_status)
    print("..............................end status update duty.....................")

    return 0




def save2db(id, n_status):
    # Get current time
    now = datetime.datetime.now()
    status_date = now.strftime("%A %d %B %Y at %H:%M")
    data = dict(status=n_status, status_date=status_date)

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

    if not updated_platform:
        print("Sarri failed to update")

    if updated_platform:
        print("Status successfuly updated!!!")
