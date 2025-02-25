import React, {useState} from 'react';
import "./css/animalForm.css"
import {add_animal} from "../api";
// This will handle the form for adding animals

const AnimalForm = ({newAnimal, setNewAnimal, handleAddAnimal}) => {
    const [imageFile, setImageFile] = useState(null);

    const handleFileChange = (e) => {
        setImageFile(e.target.files[0]); // store file
    };

    const handleSubmit = async (e) => {
        e.preventDefault(); // prevent default form submission so that we can implement
        // client side validation

        // create and pass formdata object
        const formData = new FormData();
        formData.append('name', newAnimal.name);
        formData.append('type', newAnimal.type);
        formData.append('description', newAnimal.description);
        formData.append('image', imageFile);

        await add_animal(formData);
        // reset inputs
        setNewAnimal({'name': '', type: '', description: '', image_url: '' });
        setImageFile(null);

    }

    return (
    <div className={"add-animal"}>
        <h2 className={"prompt-text"}> Add a new animal!</h2>
        <form onSubmit={handleSubmit}>
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
            type={"file"}
            accept={"image/*"} // images only!
            onChange={handleFileChange}
            />
            <button type={"submit"}>Add New Animal</button>
        </div>
        </form>
    </div>
);
};

export default AnimalForm;