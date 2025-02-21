import React from 'react';
import AnimalItem from './AnimalItem';

const AnimalList = ({animals}) => {
    return (
        <div>
            <h2>Animal List</h2>
            <ul>
                {animals.map((animal) => (
                    <AnimalItem key={animal.id} animal={animal} />
                ))}
            </ul>
        </div>
    );
};

export default AnimalList;