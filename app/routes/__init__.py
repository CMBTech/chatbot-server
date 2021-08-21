from flask_restful import Api
from app.controllers import (
    IndexView, CategoryView, PlatformView, CronView
    )

api = Api()

# Index route
api.add_resource(IndexView, '/')

# Category routes
api.add_resource(CategoryView, '/categories', endpoint='categories')

# Platform routes
api.add_resource(PlatformView, '/platforms', endpoint='platforms')

# 
api.add_resource(CronView, '/cron', endpoint='crons')