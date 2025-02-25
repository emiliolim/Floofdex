import axios from 'axios';

export const API_URL = 'http://localhost:5000'; // Flask backend URL

export const get_animals = async () => {
    const response = await axios.get(`${API_URL}/animals`);
    return response.data;
};

export const add_animal = async (formData) => {
    const response = await axios.post(`${API_URL}/animals`, formData, {
        headers: {
            'Content-Type': 'multipart/form-data',
        },
    });
    return response.data;
};

export const update_animal = async (id, animal) => {
    const response = await axios.put(`${API_URL}/animals/${id}`, animal)
    return response.data
};

export const delete_animal = async (id) => {
    try {
        const response = await axios.delete(`${API_URL}/animals/${id}`)
        return response.data
    } catch(error){
        console.error('Error deleting animal during API Call:', error);
        throw error;
    }
};