async function obtenerMedicamentos(ci_persona) {
    try {
      const url = `${window.origin}/api/medicamento/${ci_persona}`;
      const response = await axios.get(url);      
      return response.data;
    } catch (error) {
      console.log(error);
    }
  }
  
  function llenarTablaMedicamentos(datos) {
    const tablaBody = document.getElementById("tmedicamento");
    tablaBody.innerHTML = "";
    datos.forEach((medicamento) => {
      const tr = document.createElement("tr");
      const td1 = document.createElement("td");
      const td2 = document.createElement("td");
      const td3 = document.createElement("td");
      const td4 = document.createElement("td");
      td1.textContent = medicamento.nombre;
      td2.textContent = medicamento.descripcion;
      td3.textContent = medicamento.unidad;
      td4.textContent = medicamento.cantidad;
      tr.appendChild(td1);
      tr.appendChild(td2);
      tr.appendChild(td3);
      tr.appendChild(td4);
      tablaBody.appendChild(tr);
    });
  }
  
  
  