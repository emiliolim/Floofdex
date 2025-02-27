from flask import Blueprint, request, jsonify, current_app, send_from_directory
from app.models import StuffedAnimals
from sqlalchemy.exc import IntegrityError
from app import db
import os
from werkzeug.utils import secure_filename

# Define a blueprint for routes
routes = Blueprint('routes', __name__)


# Helper function to check allowed file extensions
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in current_app.config[
            'ALLOWED_EXTENSIONS']


@routes.route('/animals', methods=['GET'])
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


@routes.route('/animals/<int:id>', methods=['GET'])
def get_animal(animal_id):
    """
    :return: animal associated with id
    """
    animal = db.session.get(StuffedAnimals, animal_id)
    return jsonify({
        'id': animal.id,
        'name': animal.name,
        'type': animal.type,
        'description': animal.description,
        'image_url': animal.image_url
    })


@routes.route('/animals', methods=['POST'])
def add_animal():
    """
    :return: adds new animal to animal database
    """
    # form data
    name = request.form.get('name')
    type = request.form.get('type')
    description = request.form.get('description')
    image = request.files.get('image')

    # make sure required fields are present
    if not name or not type or not description:
        return jsonify({'error': 'Missing required fields'}), 400

    if image:
        # save uploaded image
        filename = secure_filename(image.filename)
        filepath = os.path.join('./app/uploads', filename)
        image.save(filepath)

        # store image url
        image_url = f"./uploads/{filename}"
    else:
        image_url = "none.jpg"

    try:
        new_animal = StuffedAnimals(
            name=name,
            type=type,
            description=description,
            image_url=image_url
        )
        db.session.add(new_animal)
        db.session.commit()
        return jsonify({'message': 'animal added!'}), 201

    except IntegrityError:  # catch duplicate entries
        db.session.rollback()  # restore data to last commit
        return jsonify({'error': 'animal already exists'}), 400
    except Exception:  # TODO: better error response
        db.session.rollback()
        return jsonify({'error': 'internal server error'}), 500


@routes.route('/animals/<int:id>', methods=['PUT'])
def update_animal(id):
    """:return: updates animal with given id"""
    # find animal by ID
    animal = StuffedAnimals.query.get_or_404(id)

    # get updated data from the request
    data = request.json

    # update animal fields
    if 'name' in data:
        animal.name = data['name']
    if 'type' in data:
        animal.type = data['type']
    if 'description' in data:
        animal.description = data['description']
    if 'image_url' in data:
        animal.image_url = data['image_url']

    # save changes to db
    db.session.commit()

    return jsonify({'message': 'animal updated!'}), 200


@routes.route('/animals/<int:id>', methods=['DELETE'])
def delete_animal(id):
    # find the animal
    # TODO: possibly catch 404 message gracefully
    animal = StuffedAnimals.query.get_or_404(id)

    # delete animal from database
    db.session.delete(animal)
    # save changes to db
    db.session.commit()

    # return successful message
    return jsonify({'message': 'animal deleted!'}), 200


@routes.route('/')
def home():  # put application's code here
    return 'Welcome to Floofdex!'


# Endpoint to serve uploaded images
@routes.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)
