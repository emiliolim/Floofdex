import React, {useState, useEffect} from 'react';
import {get_animals, delete_animal, add_animal, update_animal, API_URL} from './api';
import Header from './components/Header';
// import AnimalItem from './components/AnimalItem';
import AnimalList from './components/AnimalList';
import AnimalForm from './components/AnimalForm';
function App() {
  const [animals, setAnimals] = useState([])
  const [newAnimal, setNewAnimal] = useState({
    name: '', type: '', description: '', image_url: ''
  })

  const fetchAnimals = async () => {
    try {
      const data = await get_animals();
      setAnimals(data);
    } catch (error) {
      console.error('Error fetching animals:', error);
    }
  };

  const handleAddAnimal = async (formData) => {
    try{
      await add_animal(formData); // API call on delete_animal
      fetchAnimals(); // refresh animal list
    } catch (error) {
      console.error('Error deleting animal:', error);
    }
  }

  const handleDeleteAnimal = async (id) => {
    try{
      await delete_animal(id); // API call on delete_animal
      fetchAnimals(); // refresh animal list
    } catch (error) {
      console.error('Error deleting animal:', error);
    }
  }

  const handleUpdateAnimal = async (id, formData) => {
    try{
      await update_animal(id, formData);
      fetchAnimals();
    } catch (error){
      console.error('Error updating animal', error);
    }
  }

    useEffect(() => {
    fetchAnimals();
  }, []);

  return (
      <div>
          <Header />
          {/* Display form to add animals */}
          <AnimalForm
              newAnimal={newAnimal}
              setNewAnimal={setNewAnimal}
              handleAddAnimal={handleAddAnimal}
              />
          {/* TODO: Here we can implement a search bar AnimalSearch*/}
          {/* Show list of all animals */}
          <AnimalList
              animals={animals}
              handleDeleteAnimal={handleDeleteAnimal}
              handleUpdateAnimal={handleUpdateAnimal}
          />
      </div>
  );

}
export default App;

