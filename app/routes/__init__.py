from flask_restful import Api
from app.controllers import (
    IndexView, CategoryView
    )

api = Api()

# Index route
api.add_resource(IndexView, '/')

# Category routes
api.add_resource(CategoryView, '/categories', endpoint='categories')