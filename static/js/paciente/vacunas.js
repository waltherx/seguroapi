async function obtenerVacunas(ci_persona) {
    try {
      const url = `${window.origin}/api/vacuna/${ci_persona}`;
      const response = await axios.get(url);      
      return response.data;
    } catch (error) {
      console.log(error);
    }
  }
  
  function llenarTablaVacuna(datos) {
    const tablaBody = document.getElementById("tvacuna");
    tablaBody.innerHTML = "";
    datos.forEach((vacuna) => {
      const tr = document.createElement("tr");
      const td1 = document.createElement("td");
      const td2 = document.createElement("td");      
      td1.textContent = vacuna.nombre;
      td2.textContent = vacuna.dosis;      
      tr.appendChild(td1);
      tr.appendChild(td2);      
      tablaBody.appendChild(tr);
    });
  }
  
  
  