from blaise_mi_extract_api.extensions import db
from flask_login import UserMixin


class ApiKey(db.Model, UserMixin):
    # uncomment the tables args for SQL Server schemas
    # __table_args__ = {"schema": "dbo"}
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(255))
    api_key = db.Column(db.String(255))