import json
from flask import current_app
from flask_restful import Resource, request
from app.schemas.category import CategorySchema
from app.models.category import Category

class CategoryView(Resource):
    def post(self):
        """
        add new categories
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
        Fetch categories
        """
        category_schema = CategorySchema(many=True)

        categories = Category.find_all()

        category_data, errors = category_schema.dumps(categories)

        if errors:
            return dict(status='fail', message=errors), 400

        return dict(
            status='success',
            data=dict(categories=json.loads(category_data))
        ), 200

    def patch(self, category_id):
        """
        update a category
        """
        category_schema = CategorySchema(partial=True)

        update_data = request.get_json()

        validated_update_data, errors = category_schema.load(update_data)

        if errors:
            return dict(status="fail", message=errors), 400

        category = Category.get_by_id(category_id)

        if not category:
            return dict(
                status="fail",
                message=f"Category with id {category_id} not found"
                ), 404


        updated_category = Category.update(category, **validated_update_data)

        if not updated_category:
            return dict(status='fail', message='Internal Server Error'), 500

        return dict(
            status="success",
            message=f"Category {category.name} updated successfully"
            ), 200



    def delete(self, category_id):
        """
        Delete a category
        """

        try:
            category = Category.get_by_id(category_id)

            if not category:
                return dict(
                    status='fail',
                    message=f'category {category_id} not found'
                    ), 404

            deleted = category.delete()

            if not deleted:
                return dict(status='fail', message='deletion failed'), 500

            return dict(
                status='success',
                message=f'category {category_id} deleted successfully'
                ), 200

        except Exception as e:
            return dict(status='fail', message=str(e)), 500