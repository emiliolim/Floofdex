import React from 'react';
// This will handle the form for adding animals

const AnimalForm = ({newAnimal, setNewAnimal, handleNewAnimal}) => {
    return (
    <div>
        <h2> Add a new animal!</h2>
        <input
            type="text"
            placeholder="Name"
            value={newAnimal.name}
            onChange={(e) =>
            setNewAnimal({ ...newAnimal, name: e.target.value })
            }
        />
        <input
            type="text"
            placeholder="Type"
            value={newAnimal.type}
            onChange={(e) =>
                setNewAnimal({ ...newAnimal, type: e.target.value })
            }
        />
        <input
            type="text"
            placeholder="Description"
            value={newAnimal.description}
            onChange={(e) =>
                setNewAnimal({ ...newAnimal, description: e.target.value })
            }
            />
        <input
            type="text"
            placeholder="Image URL"
            value={newAnimal.image_url}
            onChange={(e) =>
                setNewAnimal({ ...newAnimal, image_url: e.target.value })
        }
            />
        <button onClick={handleNewAnimal}>Add New Animal</button>
    </div>
);
};

export default AnimalForm;