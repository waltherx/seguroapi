"use strict";

import axios from "https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js";

async function uploadPhoto(data) {
  try {
    const response = await axios.post("/", data);
    return response.data;
  } catch (error) {
    throw error.response;
  }
}

export default uploadPhoto;
