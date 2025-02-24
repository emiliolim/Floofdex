import React, {useState} from 'react';
import './css/animalItem.css'

const AnimalItem = ({animal, handleDeleteAnimal}) => {
    const [imgSrc, setImgSrc] = useState("scrapEntry.PNG");

    return (
        <li id={animal.id} className={"entry"}>
            <div className={"entry_content"}>
                    <h3 className={"entry_name"}>{animal.name}</h3>
                    <img
                        src={imgSrc}
                        alt={animal.name}
                        width="100"
                        className={"entry_img"}
                    onError={() => setImgSrc(animal.image)}/>
                    <p className={"entry_type"}>Type: {animal.type}</p>
                    <p className={"entry_description"}>{animal.description}</p>
                    <button className={"entry_remove"}
                            onClick={() => handleDeleteAnimal(animal.id)}>
                        remove this entry
                    </button>
            </div>
        </li>
    );
};

export default AnimalItem;