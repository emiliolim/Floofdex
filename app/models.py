from app import db


# test class
class StuffedAnimals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(200))
