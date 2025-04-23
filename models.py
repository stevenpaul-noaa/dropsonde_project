from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dropsonde(db.Model):
    __tablename__ = 'dropsonde_data'  # <-- Update the table name here
    id = db.Column(db.Integer, primary_key=True)
    tail = db.Column(db.String(10), nullable=False)
    operator = db.Column(db.String(50), nullable=False)
    droptime = db.Column(db.DateTime, nullable=False)
    lat = db.Column(db.Float, nullable=False)
    lon = db.Column(db.Float, nullable=False)
    serial = db.Column(db.String(10), nullable=True)
