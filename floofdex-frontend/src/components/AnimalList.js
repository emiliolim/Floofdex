import React from 'react';
import AnimalItem from './AnimalItem';

const AnimalList = ({animals}) => {
    return (
        <div className={"scrapbook"}>
            <h2 className={"scrapbook_title"}>Animal List</h2>
            {/* Use grid container for scrapbook entries */}
            <ul className={"scrapbook_grid"}>
                {animals.map((animal) => (
                    <AnimalItem key={animal.id} animal={animal}/>
                ))}
            </ul>
        </div>
    );
};

export default AnimalList;