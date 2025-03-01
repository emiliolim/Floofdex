import React, {useState} from 'react';
import './css/animalItem.css'
const AnimalItem = ({animal, handleDeleteAnimal}) => {
    /*
    Component handling stuffed animal entries in the scrapbook

    animal: database entry for a stuffed animal
    handleDeleteAnimal: allows the option to delete the entry
    */
    const imageUrl = `http://localhost:5000/${animal.image_url}`;
    const [imgSrc, setImgSrc] = useState(imageUrl);

    return (
        <li id={animal.id}>
            <div className={"entry"}>
                {/* TODO: upon click, pull up a edit screen and upon
                    TODO: a 'save changes' button, API call to update_animals
                */}
                <img className={"entry_edit"}
                     src={"edit_button.png"}
                     alt={"edit button image"}
                     width={"40"}
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
                    {/* Send API call to delete animal entry */}
                    <button className={"entry_remove"}
                            onClick={() => handleDeleteAnimal(animal.id)}>
                        remove this entry
                    </button>
                </div>
            </div>
        </li>
    );
};

export default AnimalItem;