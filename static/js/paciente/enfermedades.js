async function obtenerEnfermedades(ci_persona) {
    try {
      const url = `${window.origin}/api/enfermedad/${ci_persona}`;
      const response = await axios.get(url);      
      return response.data;
    } catch (error) {
      console.log(error);
    }
  }
  
  function llenarTablaEnfermedades(datos) {
    const tablaBody = document.getElementById("tenfermedad");
    tablaBody.innerHTML = "";
    datos.forEach((enfermedad) => {
      const tr = document.createElement("tr");
      const td1 = document.createElement("td");
      const td2 = document.createElement("td");
      const td3 = document.createElement("td");
      const td4 = document.createElement("td");
      const td5 = document.createElement("td");
      td1.textContent = enfermedad.nombre;
      td2.textContent = enfermedad.descripcion;
      td3.textContent = enfermedad.causa;
      td4.textContent = enfermedad.sintoma;
      td5.textContent = enfermedad.diagnostico;
      tr.appendChild(td1);
      tr.appendChild(td2);
      tr.appendChild(td3);
      tr.appendChild(td4);
      tr.appendChild(td5);
      tablaBody.appendChild(tr);
    });
  }
  
  
  