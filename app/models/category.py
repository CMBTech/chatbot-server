from app.models import db
from app.models.root_model import ModelMixin

class Category(ModelMixin):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=True)
    plaforms = db.relationship('Platform', backref='category', lazy=True)
