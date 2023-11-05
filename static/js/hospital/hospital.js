"use strict"

const url = `${window.origin}/api/hospital/`;

export const getHospitalCA = async () => {
    const response = await axios.get(`${url}/n/1`);
    return response.data;
}