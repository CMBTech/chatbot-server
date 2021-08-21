import json
from flask import current_app
from flask_restful import Resource, request
from app.schemas.category import CategorySchema
from app.models.category import Category

class CategoryView(Resource):
    def post(self):
        """
        """

        category_schema = CategorySchema()

        category_data = request.get_json()

        validated_category_data, errors = category_schema.load(category_data)

        category_name = validated_category_data.get('name', None)

        if errors:
            return dict(status="fail", message=errors), 400

        category_existant = Category.find_first(name=category_name)

        if category_existant:
            return dict(
                status="fail",
                message=f"category {validated_category_data['name']} Already Exists."
                ), 400

        category = Category(**validated_category_data)
        saved_category = category.save()

        if not saved_category:
            return dict(status='fail', message=f'Internal Server Error'), 500

        new_category_data, errors = category_schema.dumps(category)

        return dict(
            status='success',
            data=dict(category=json.loads(new_category_data))
            ), 201

    def get(self):
        """
        """
        category_schema = CategorySchema(many=True)

        categories = Category.find_all()
        print(categories)

        category_data, errors = category_schema.dumps(categories)

        if errors:
            return dict(status='fail', message=errors), 400

        return dict(
            status='success',
            data=dict(categories=json.loads(category_data))
        ), 200
