from sqlalchemy.sql.expression import null
from app.models import db
from app.models.root_model import ModelMixin

class Platform(ModelMixin):
    __tablename__ = 'platform'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True)
    url = db.Column(db.String(256), nullable=True)
    status_date = db.Column(db.String, default=db.func.current_timestamp())
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    status = db.Column(db.Boolean, nullable=True)
    report_id = db.Column(db.String(256), nullable=False)
    menu_value = db.Column(db.Integer, nullable=False)