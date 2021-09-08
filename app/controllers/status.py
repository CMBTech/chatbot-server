import json
from flask import current_app
from flask_restful import Resource, request
from app.schemas.category import CategorySchema
from app.models.category import Category
from app.schemas.platform import PlatformSchema
from app.models.platform import Platform

class StatusView(Resource):
    def post(self):
        """
        """

        google_data = request.get_json()
        if(google_data):
            choice = google_data['queryResult']['parameters']['number']
        else:
            choice = 3 # mannually set the choice if not sent in request
        
        
        if choice == 1 or choice == 2:
            # check for platform one
            platform_schema = PlatformSchema()

            platforms = Platform.get_by_id(choice)
            platforms_data, errors = platform_schema.dumps(platforms)

            if errors:
                return dict(status='fail', message=errors), 500

            # construct response 
            response_list = []
            platform_list = json.loads(platforms_data)
            name = platform_list['name']
            if platform_list['status']:
                message = " is currently blocked"
            else:
                message = " is up and running"
            response_list.append( name  + message + " as of "+ platform_list['status_date'])

            final_list = []
            final_list.append(dict(text = dict(text=response_list)))


            return dict(fulfillmentMessages=final_list),200

        elif choice == 3 or choice == 4 or choice == 5 or choice == 6:
            platform_schema = PlatformSchema(many=True)
            
            category = Category.find_all(menu_value=choice)
            print("category is",category)

            if not category:
                response_list = []
                response_list.append("Sorry I didn't get that category. Try another on the menu. For Twitter say 1, For Facebook say 2, For all social platforms say 3, For all vpn checks say 4")

                final_list = []
                final_list.append(dict(text = dict(text=response_list)))

                return dict(fulfillmentMessages=final_list),200
            
            platforms = Platform.find_all(category_id=category.id)
        
            platforms_data, errors = platform_schema.dumps(platforms)
            
            if errors:
                print(errors)
                return dict(status='fail', message=errors), 500

            # construct response 
            response_list = []
            platforms_data_list = json.loads(platforms_data)
            if not platforms_data_list:
                response_list.append("No platforms yet in this category")
            
            if platforms_data_list:
                for platform in platforms_data_list:
                    if platform['status']:
                        message = " is currently blocked"
                    else:
                        message = " is up and running"
                    response_list.append( platform['name']  + message + " as of "+ platform['status_date'])

            final_list = []
            final_list.append(dict(text = dict(text=response_list)))

            return dict(
                fulfillmentMessages=final_list),200
        else:
            response_list = []
            response_list.append("Sorry I didn't get that choice. Try another on the menu. For Facebook press 1, For Twitter press 2, For all social platforms press 3, For all vpn checks press 4")

            final_list = []
            final_list.append(dict(text = dict(text=response_list)))

            return dict(fulfillmentMessages=final_list),200



