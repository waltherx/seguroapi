async function modalAlergia(ci_person,id_paciente) {
  const { value: formValues } = await Swal.fire({
    title: "Agregar Alergia",
    html: `<div class="form-floating">
            <input id="nombreTxt" type="text" class="form-control">
            <label for="nombreTxt" class="form-label">Nombre:</label>
          </div>
        <div class="form-floating">
          <input id="descrTxt" type="text" class="form-control">
          <label for="descrTxt" class="form-label">Descripcion:</label>
        </div>
        <div class="form-floating">
          <input id="gravedadTxt" type="text" class="form-control">
          <label for="gravedadTxt" class="form-label">Gravedad:</label>
        </div>
        <div class="form-floating">
          <input id="reaccionTxt" type="text" class="form-control">
          <label for="reaccionTxt" class="form-label">Reaccion:</label>
        </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresAlergia,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  const url = `${window.origin}/api/alergia/add`;
  if (formValues) {
    const data = {
      id_paciente: id_paciente,
      nombre: formValues[0],
      descripcion: formValues[1],
      gravedad: formValues[2],
      reaccion: formValues[3],
    };

    try {
      const response = await axios.post(url, data);
      const msg = response;
      Swal.fire("Correcto!", msg.data.message, "success");
      obtenerAlergias(ci_person)
        .then((datos) => {
          llenarTablaAlergia(datos);
        })
        .catch((error) => {
          console.log("Error al obtener y llenar los datos:", error);
        });
    } catch (error) {
      Swal.fire(JSON.stringify(error, msg.data.message, "error"));
    }
  }
}

function obtenerValoresAlergia() {
  const input1 = document.getElementById("nombreTxt").value;
  const input2 = document.getElementById("descrTxt").value;
  const input3 = document.getElementById("gravedadTxt").value;
  const input4 = document.getElementById("reaccionTxt").value;

  if (input1.trim() === "") {
    Swal.showValidationMessage(
      `Request failed: Por favor ingresa un Nombre de Alergia.`
    );
  } else {
    console.log("Ambos campos tienen valores válidos.");
    return [input1, input2, input3, input4];
  }
}

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
