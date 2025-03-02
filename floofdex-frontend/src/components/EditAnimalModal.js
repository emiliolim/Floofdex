import React, {useState} from 'react';
import './css/editAnimalModal.css'
const EditAnimalModal = ({animal, onClose, handleUpdateAnimal, handleDeleteAnimal}) => {
    // States to manage form inputs
    const [name, setName] = useState(animal.name);
    const [type, setType] = useState(animal.type);
    const [description, setDescription] = useState(animal.description);
    // TODO: Make a use state for images/image file submissions

    const handleSubmit = async (e) => {
      e.preventDefault();

      const formData = new FormData();
      formData.append('name', name);
      formData.append('type', type);
      formData.append('description', description);
      formData.append('image_url', animal.image_url);

      await handleUpdateAnimal(animal.id, formData);
      onClose();
    };

    return (
        <div className={"modal_edit"}>
            <div className={"modal_content"}>
                {/* Close button */}
                <span className={"close_btn"} onClick={onClose}>
                    &times;
                </span>
                {/* Edit form content*/}
                <h2 align={"center"}> Edit Entry</h2>
                <form onSubmit={handleSubmit}>
                    {/* Edit Name form */}
                    <div>
                        <label><b>Name: </b></label>
                        <input type={"text"} value={name} className={"entry_update"}
                               onChange ={(e) => setName(e.target.value)}
                               />
                    </div>
                    {/* Edit Type form */}
                    <div>
                        <label><b>Type: </b></label>
                        <input type={"text"} value={type} className={"entry_update"}
                               onChange={(e) => setType(e.target.value)}
                               />
                    </div>
                    {/* Edit Description form */}
                    <div>
                        <label><b>Description: </b></label>
                        <input type={"text"} value={description} className={"entry_update"}
                               onChange={(e) => setDescription(e.target.value)}
                               />
                    </div>
                    <button type={"submit"} className={"save_changes"}>
                        save changes
                    </button>
                    {/* Send API call to delete animal entry */}
                    <button className={"entry_remove"}
                            onClick={() => handleDeleteAnimal(animal.id)}>
                        remove this entry
                    </button>
                </form>
            </div>
        </div>
    );
};

export default EditAnimalModal;