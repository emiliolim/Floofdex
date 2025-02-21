import React from 'react';

const AnimalItem = ({animal}) => {
    return (
        <li>
            <h3>{animal.name}</h3>
            <img src={animal.image} alt={animal.name} width="100"/>
            <p>Type: {animal.type}</p>
            <p>{animal.description}</p>
        </li>
    );
};

export default AnimalItem;