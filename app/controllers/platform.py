import json
from flask import current_app
from flask_restful import Resource, request
from app.schemas.platform import PlatformSchema
from app.models.platform import Platform

class PlatformView(Resource):
    def post(self):
        """
        """

        platform_schema = PlatformSchema()

        platform_data = request.get_json()
        print(platform_data)

        validated_platform_data, errors = platform_schema.load(platform_data)

        platform_name = validated_platform_data.get('name', None)
        print(platform_name)

        if errors:
            return dict(status="fail", message=errors), 400

        platform_existant = Platform.find_first(name=platform_name)

        if platform_existant:
            return dict(
                status="fail",
                message=f"platform {validated_platform_data['name']} Already Exists."
                ), 400

        platform = Platform(**validated_platform_data)
        saved_platform = platform.save()

        if not saved_platform:
            return dict(status='fail', message=f'Internal Server Error'), 500

        new_platform_data, errors = platform_schema.dumps(platform)

        return dict(
            status='success',
            data=dict(platform=json.loads(new_platform_data))
            ), 201

    def get(self):
        """
        """
        platform_schema = PlatformSchema(many=True)

        platforms = Platform.find_all()
        print(platforms)

        platform_data, errors = platform_schema.dumps(platforms)

        if errors:
            return dict(status='fail', message=errors), 400

        return dict(
            status='success',
            data=dict(platforms=json.loads(platform_data))
        ), 200


    def patch(self, platform_id):
        platform_schema = PlatformSchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = platform_schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        platform = Platform.get_by_id(platform_id)

        if not platform:
            return dict(
                status="fail",
                message=f"Platform with id {platform_id} not found"
                ), 404


        updated_platform = Platform.update(platform, **validated_update_data)

        if not updated_platform:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(
            status="success",
            message=f"Platform {platform.name} updated successfully"
            ), 200



    def delete(self, platform_id):
        """
        """

        try:
            platform = Platform.get_by_id(platform_id)

            if not platform:
                return dict(
                    status='fail',
                    message=f'platform {platform_id} not found'
                    ), 404

            deleted = platform.delete()

            if not deleted:
                return dict(status='fail', message='deletion failed'), 500

            return dict(
                status='success',
                message=f'platform {platform_id} deleted successfully'
                ), 200

        except Exception as e:
            return dict(status='fail', message=str(e)), 500