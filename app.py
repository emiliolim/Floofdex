from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request

# create app
app = Flask(__name__)
# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stuffed_animals.db'
db = SQLAlchemy(app)


# test class
class StuffedAnimals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    description = db.Column(db.Text)
    image_url = db.Column(db.String(200))


# create database tables
with app.app_context():
    db.create_all()


@app.route('/animals', methods=['GET'])
def get_animals():
    """
    :return: list of stuffed animals
    """
    animals = StuffedAnimals.query.all()
    return jsonify([{
        'id': animal.id,
        'name': animal.name,
        'type': animal.type,
        'description': animal.description,
        'image_url': animal.image_url
    } for animal in animals])


@app.route('/animals', methods=['POST'])
def add_animal():
    """
    :return: adds new animal to animal database
    """
    data = request.json
    new_animal = StuffedAnimals(
        name=data['name'],
        type=data['type'],
        description=data['description'],
        image_url=data['image_url']
    )
    db.session.add(new_animal)
    db.session.commit()
    return jsonify({'message': 'animal added!'}), 201


@app.route('/')
def home():  # put application's code here
    return 'Welcome to Floofdex!'


if __name__ == '__main__':
    app.run()
