from flask import Blueprint, request, jsonify
from app.models import *


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


@app.route('/animals/<int:id>', methods=['PUT'])
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


@app.route('/animals/<int:id>', methods=['DELETE'])
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


@app.route('/')
def home():  # put application's code here
    return 'Welcome to Floofdex!'
