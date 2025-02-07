from flask import Blueprint, jsonify

"""
this module deals with error handling for CRUD operations
"""

# Define a blueprint for errors
errors = Blueprint('errors', __name__)

@errors.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Resource (stuffed animal) not found'}), 404


@errors.errorhandler(400)
def bad_request(error):
    return jsonify({'error': 'Bad Request'}), 400


@errors.errorhandler(500)
def internal_server_error(error):
    return jsonify({'error', 'Internal server error'}), 500
