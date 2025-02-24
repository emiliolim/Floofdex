import React from 'react';
import "./css/animalForm.css"
// This will handle the form for adding animals

const AnimalForm = ({newAnimal, setNewAnimal, handleNewAnimal}) => {
    return (
    <div className={"add-animal"}>
        <h2 className={"prompt-text"}> Add a new animal!</h2>
        <div className={"prompts"}>
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
    </div>
);
};

export default AnimalForm;