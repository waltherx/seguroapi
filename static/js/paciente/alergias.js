async function obtenerAlergias(ci_persona) {
    try {
      const url = `${window.origin}/api/alergia/${ci_persona}`;
      const response = await axios.get(url);      
      return response.data;
    } catch (error) {
      console.log(error);
    }
  }
  
  function llenarTablaAlergia(datos) {
    const tablaBody = document.getElementById("talergia");
    tablaBody.innerHTML = "";
    datos.forEach((alergia) => {
      const tr = document.createElement("tr");
      const td1 = document.createElement("td");
      const td2 = document.createElement("td");
      const td3 = document.createElement("td");
      const td4 = document.createElement("td");
      td1.textContent = alergia.nombre;
      td2.textContent = alergia.descripcion;
      td3.textContent = alergia.gravedad;
      td4.textContent = alergia.reaccion;
      tr.appendChild(td1);
      tr.appendChild(td2);
      tr.appendChild(td3);
      tr.appendChild(td4);
      tablaBody.appendChild(tr);
    });
  }
  
  
  