import pytest
from app import create_app, db
from app.models import StuffedAnimals
import warnings
from sqlalchemy import exc as sa_exc

BASE_URL = 'http://127.0.0.1:5000'


@pytest.fixture
def client():
    """Test client for floofdex"""
    # create sample database from local storage
    app = create_app('app.config.TestingConfig')
    app.config['TESTING'] = True
    app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:///:memory'

    # ignore legacy warnings
    warnings.simplefilter("default")
    warnings.simplefilter("ignore", category=sa_exc.LegacyAPIWarning)

    # Create a test client
    with app.test_client() as client:
        # Set up the database
        with app.app_context():
            db.create_all()  # Create all database tables
        yield client  # Provide the client to the test
        # Tear down the database
        with app.app_context():
            db.drop_all()  # Drop all database tables after the test


@pytest.fixture
def test_animal_data():
    """Fixture for test animal data"""
    return {
        "name": "meep",
        "type": "dino",
        "description": "a green horned dino",
        "image_url": "http://127.0.0.1:5000/static/images/meep.png"
    }


def test_animals_get(client):
    """Tests GET endpoint and return type"""
    # Add a test animal to the database
    with client.application.app_context():
        test_animal = StuffedAnimals(
            name="meep",
            type="dino",
            description="a green horned dino",
            image_url="https://example.com/meep.jpg"
        )
        db.session.add(test_animal)
        db.session.commit()

    # Make a GET request to the /animals endpoint
    response = client.get('/animals')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]['name'] == "meep"


def test_animals_post(client, test_animal_data):
    """tests POST endpoint"""
    # Make a POST request to the /animals endpoint
    response = client.post('/animals', json=test_animal_data)
    assert response.status_code == 201
    assert response.get_json() == {"message": "animal added!"}

    # Verify the animal was added to the database
    with client.application.app_context():
        animal = StuffedAnimals.query.first()
        assert animal.name == "meep"


def test_animals_put(client, test_animal_data):
    """tests PUT endpoint"""
    # Add a test animal to the database
    with client.application.app_context():
        test_animal = StuffedAnimals(
            name="meep",
            type="dino",
            description="a green horned dino",
            image_url="https://example.com/meep.jpg"
        )
        db.session.add(test_animal)
        db.session.commit()
        animal_id = test_animal.id

    # Updated animal data
    updated_data = {
        "name": "noop",
        "type": "chicken nugget dino",
        "description": "this guy is noop!",
        "image_url": "https://example.com/noop.jpg"
    }

    # sent put request
    response = client.put(f'/animals/{animal_id}', json=updated_data)

    # manage return
    assert response.status_code == 200
    assert response.get_json() == {"message": "animal updated!"}

    # verify updates
    with client.application.app_context():
        animal = db.session.get(StuffedAnimals, animal_id)
        assert animal.name == "noop"
        assert animal.type == "chicken nugget dino"
        assert animal.description == "this guy is noop!"
        assert animal.image_url == "https://example.com/noop.jpg"


def test_animals_delete(client, test_animal_data):
    """tests DELETE endpoint"""
    # Add a test animal to the database
    with client.application.app_context():
        test_animal = StuffedAnimals(
            name="meep",
            type="dino",
            description="a green horned dino",
            image_url="https://example.com/meep.jpg"
        )
        db.session.add(test_animal)
        db.session.commit()
        animal_id = test_animal.id

    # delete!
    response = client.delete(f'/animals/{animal_id}')
    assert response.status_code == 200
    assert response.get_json() == {"message": "animal deleted!"}

    # verify delete in db
    with client.application.app_context():
        animal = db.session.get(StuffedAnimals, animal_id)
        assert animal is None
