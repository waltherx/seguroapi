async function obtenerDocumentos(ci_persona) {
  try {
    const url = `${window.origin}/api/doc/${ci_persona}`;
    const response = await axios.get(url);
    return response.data.Documentos;
  } catch (error) {
    console.log(error);
  }
}

function llenarTablaDoc(datos) {
  const tablaBody = document.getElementById("tdocumento");
  tablaBody.innerHTML = "";
  datos.forEach((doc) => {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td");
    const td2 = document.createElement("td");
    td1.textContent = doc.tipo;
    const img = document.createElement("img");
    img.src = doc.url;
    img.alt = "Cinque Terre";
    img.height = 200;
    img.width = 200;
    img.classList.add("rounded-circle");
    td2.appendChild(img);
    tr.appendChild(td1);
    tr.appendChild(td2);
    tablaBody.appendChild(tr);
  });
}
