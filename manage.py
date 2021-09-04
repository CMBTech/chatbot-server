from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import db
from server import app

# import models
from app.models.platform import Platform
from app.models.category import Category

#  import helpers
from app.helpers.create_categories import create_category
from app.helpers.create_platforms import create_platform

# register app and db with migration class
migrate = Migrate(app, db, compare_type=True)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

@manager.option('-n', '--name', dest='name')
@manager.option('-u', '--url', dest='url')
@manager.option('-c', '--category_id', dest='category_id')

@manager.command
def create_new_category():
    create_category()

@manager.command
def create_new_platform(name, url, category_id):
    create_platform(name, url, category_id)

if __name__ == '__main__':
    manager.run()