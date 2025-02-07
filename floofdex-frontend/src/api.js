import axios from 'axios';

const API_URL = 'http://localhost:3000' // Flask backend URL

export const get_animals = async () => {
    const response = await axios.get(`${API_URL}/animals`)
    return response.data
};

export const add_animal = async () => {
    const response = await axios.post(`${API_URL}/animals`)
    return response.data
};

export const update_animal = async (id) => {
    const response = await axios.put(`${API_URL}/animals/${id}`)
    return response.data
};

export const delete_animal = async (id) => {
    const response = await axios.delete(`${API_URL}/animals/${id}`)
    return response.data
};