import React, {useState} from 'react';
import './css/animalItem.css'
import EditAnimalModal from "./EditAnimalModal";
const AnimalItem = ({animal, handleDeleteAnimal, handleUpdateAnimal}) => {
    /*
    Component handling stuffed animal entries in the scrapbook

    animal: database entry for a stuffed animal
    handleDeleteAnimal: allows the option to delete the entry
    */

    // state for default image entries
    const imageUrl = `http://localhost:5000/${animal.image_url}`;
    const [imgSrc, setImgSrc] = useState(imageUrl);

    // state for controlling edit entry box visibility
    const [isModalOpen, setIsModalOpen] = useState(false);

    const openModal = () => {
        setIsModalOpen(true);
    };

    const closeModal = () => {
        setIsModalOpen(false);
    };

    return (
        <li id={animal.id}>
            <div className={"entry"}>
                <input type={"image"}
                       className={"entry_edit"}
                     src={"edit_button.png"}
                     alt={"edit button image"}
                     width={"40"}
                       onClick = {openModal}
                />
                <div className={"entry_content"}>
                    <h3 className={"entry_name"}>{animal.name}
                    </h3>
                    {/*If the image is not found in the db, then a
                        default image scrapEntry.png is shown.*/}
                    <img
                        src={imgSrc}
                        alt={animal.name}
                        width="100"
                        className={"entry_img"}
                        onError={() => setImgSrc("scrapEntry.PNG")}/>
                    <div className={"entry_about"}>
                        <p className={"entry_type"}>Type: {animal.type}</p>
                        <p className={"entry_description"}>{animal.description}</p>
                    </div>
                </div>
            </div>
            {/* Render Modal when edit button is clicked */}
            {isModalOpen && (
                <EditAnimalModal animal={animal}
                                 onClose={closeModal}
                                 handleUpdateAnimal={handleUpdateAnimal}
                                 handleDeleteAnimal={handleDeleteAnimal}
                />
            )}
        </li>
    );
};

export default AnimalItem;