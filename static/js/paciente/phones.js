async function obtenerPhones(ci_persona) {
  try {
    const url = `${window.origin}/api/phone/${ci_persona}`;
    const response = await fetch(url);
    const result = await response.json();
    return result.telefonos;
  } catch (error) {
    console.log(error);
  }
}

function llenarTabla(datos) {
  const tablaBody = document.getElementById("tphones");
  tablaBody.innerHTML = "";
  datos.forEach((phone) => {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td");
    const td2 = document.createElement("td");
    td1.textContent = phone.numero;
    td2.textContent = phone.referencia;
    tr.appendChild(td1);
    tr.appendChild(td2);
    tablaBody.appendChild(tr);
  });
}


