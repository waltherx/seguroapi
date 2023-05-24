async function obtenerOperaciones(ci_persona) {
    try {
      const url = `${window.origin}/api/operacion/${ci_persona}`;
      const response = await axios.get(url);      
      return response.data;
    } catch (error) {
      console.log(error);
    }
  }
  
  function llenarTablaOperaciones(datos) {
    const tablaBody = document.getElementById("toperacion");
    tablaBody.innerHTML = "";
    datos.forEach((operacion) => {
      const tr = document.createElement("tr");
      const td1 = document.createElement("td");
      const td2 = document.createElement("td");
      const td3 = document.createElement("td");
      td1.textContent = operacion.tipo;
      td2.textContent = operacion.fecha;
      td3.textContent = operacion.descripcion;
      tr.appendChild(td1);
      tr.appendChild(td2);
      tr.appendChild(td3);
      tablaBody.appendChild(tr);
    });
  }
  
  
  