async function modalEnfermedad(ci_person, id_paciente) {
  const { value: formValues } = await Swal.fire({
    title: "Agregar Enfermedad",
    html: `<div class="form-floating">
            <input id="nombreTxt" type="text" class="form-control">
            <label for="nombreTxt" class="form-label">Nombre:</label>
          </div>
          <div class="form-floating">
            <input id="descripcionTxt" type="text" class="form-control">
            <label for="descripcionTxt" class="form-label">Descripcion:</label>
          </div>
          <div class="form-floating">
            <input id="causaTxt" type="text" class="form-control">
            <label for="causaTxt" class="form-label">Causa:</label>
          </div>
          <div class="form-floating">
            <input id="sintomaTxt" type="text" class="form-control">
            <label for="sintomaTxt" class="form-label">Sintoma:</label>
          </div>
          <div class="form-floating">
            <input id="diagnosticoTxt" type="text" class="form-control">
            <label for="diagnosticoTxt" class="form-label">Diagnostico:</label>
          </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresEnfermedad,
    confirmButtonText: "Aceptar",
    showCloseButton: true,
    confirmButtonColor: "#012970",
  });

  const url = `${window.origin}/api/enfermedad/add`;
  if (formValues) {
    const data = {
      nombre: formValues[0],
      descripcion: formValues[1],
      causa: formValues[2],
      sintoma: formValues[3],
      diagnostico: formValues[4],
      paciente_id: id_paciente,
    };
    try {
      const response = await axios.post(url, data);
      const msg = response;
      Swal.fire("Correcto!", msg.data.message, "success");
      mostarEnfermedades(ci_person);
    } catch (error) {
      Swal.fire(JSON.stringify(error, msg.data.message, "error"));
    }
  }
}

function obtenerValoresEnfermedad() {
  const input1 = document.getElementById("nombreTxt").value;
  const input2 = document.getElementById("descripcionTxt").value;
  const input3 = document.getElementById("causaTxt").value;
  const input4 = document.getElementById("sintomaTxt").value;
  const input5 = document.getElementById("diagnosticoTxt").value;

  if (input1.trim() === "") {
    Swal.showValidationMessage(
      `Por favor ingresa un valor en el campo nombre.`
    );
  } else {
    return [input1, input2, input3, input4, input5];
  }
}

function mostrarEnfermedades(ci_persona) {
  obtenerEnfermedades(ci_persona)
    .then((datos) => {
      llenarTablaEnfermedades(datos, ci_persona);
    })
    .catch((error) => {
      console.log("Error al obtener y llenar los datos:", error);
    });
}

function llenarTablaEnfermedades(datos, ci_person) {
  const tablaBody = document.getElementById("tenfermedad");
  tablaBody.innerHTML = "";
  datos.forEach((enfermedad) => {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td");
    const td2 = document.createElement("td");
    const td3 = document.createElement("td");
    const td4 = document.createElement("td");
    const td5 = document.createElement("td");
    const td6 = document.createElement("td");
    td1.textContent = enfermedad.nombre;
    td2.textContent = enfermedad.descripcion;
    td3.textContent = enfermedad.causa;
    td4.textContent = enfermedad.sintoma;
    td5.textContent = enfermedad.diagnostico;

    const btnEliminar = crearBotonEnfermedad(true, () =>
      eliminarEnfermedad(enfermedad.id, enfermedad.nombre, ci_person)
    );
    const btnActualizar = crearBotonEnfermedad(false, () =>
      actualizarEnfermedad(enfermedad.id, ci_person)
    );

    const contenedorBotones = document.createElement("div");
    contenedorBotones.classList.add("d-flex", "justify-content-end", "gap-2");
    contenedorBotones.appendChild(btnActualizar);
    contenedorBotones.appendChild(btnEliminar);
    td6.appendChild(contenedorBotones);

    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td5);
    tr.appendChild(td6);
    tablaBody.appendChild(tr);
  });
}

function crearBotonEnfermedad(isDelete, onClick) {
  const boton = document.createElement("button");
  boton.textContent = "";
  if (isDelete) {
    boton.innerHTML = `<i class="bi bi-trash"></i>`;
    boton.classList.add("btn", "btn-danger", "btn-sm");
  } else {
    boton.innerHTML = `<i class="bi bi-gear-fill"></i>`;
    boton.classList.add("btn", "btn-success", "btn-sm");
  }
  //boton.classList.add("btn", "btn-success", "btn-sm");
  boton.addEventListener("click", onClick);
  return boton;
}

function eliminarEnfermedad(id, nombre, ci_persona) {
  Swal.fire({
    title: "Esta Seguro?",
    text: `Eliminar Enfermedad de ${nombre}!`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#012970",
    cancelButtonColor: "#d33",
    confirmButtonText: "Eliminar!",
  }).then((result) => {
    if (result.isConfirmed) {
      deleteEnfermedad(id)
        .then((result) => {
          Swal.fire("Eliminado!", "Enfermedad fue Eliminado!", "success");
          mostrarEnfermedades(ci_persona);
        })
        .catch((error) => {
          console.log("error", error);
        });
    }
  });
}

async function deleteEnfermedad(id) {
  try {
    const url = `${window.origin}/api/enfermedad/delete/${id}`;
    const response = await axios.delete(url);
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

function actualizarEnfermedad(id, ci_persona) {
  try {
    update_Enfermedad(id, ci_persona);
  } catch (error) {
    console.log(error);
  }
}

async function update_Enfermedad(id_enfermedad, ci_person) {
  const url_get = `${window.origin}/api/enfermedad/view/${id_enfermedad}`;
  const response = await axios.get(url_get);
  const enferm = response.data;
  console.log(enferm);
  const { value: formValues } = await Swal.fire({
    title: "Actualizar Enfermedad",
    html: `<div class="form-floating">      
            <input id="nombreTxt" type="text" value="${enferm.nombre}" class="form-control">
            <label for="nombreTxt" class="form-label">Nombre:</label>
          </div>
          <div class="form-floating">
            <input id="descripcionTxt" type="text" value="${enferm.descripcion}" class="form-control">
            <label for="descripcionTxt" class="form-label">Descripcion:</label>
          </div>
          <div class="form-floating">
            <input id="causaTxt" type="text" value="${enferm.causa}" class="form-control">
            <label for="causaTxt" class="form-label">Causa:</label>
          </div>
          <div class="form-floating">
            <input id="sintomaTxt" type="text" value="${enferm.sintoma}" class="form-control">
            <label for="sintomaTxt" class="form-label">Sintoma:</label>
          </div>
          <div class="form-floating">
            <input id="diagnosticoTxt" type="text" value="${enferm.diagnostico}" class="form-control">
            <label for="diagnosticoTxt" class="form-label">Diagnostico:</label>
          </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresEnfermedad,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  if (formValues) {
    const data = {
      id: id_enfermedad,
      nombre: formValues[0],
      descripcion: formValues[1],
      causa: formValues[2],
      sintoma: formValues[3],
      diagnostico: formValues[4],
      paciente_id: enferm.paciente_id,
    };

    try {
      const url_put = `${window.origin}/api/enfermedad/update`;
      const response = await axios.put(url_put, data);
      Swal.fire("Correcto!", "Acualizado", "success");
      mostrarEnfermedades(ci_person);
    } catch (error) {
      Swal.fire(JSON.stringify("error", response.data, "error"));
    }
  }
}

async function view_Enfermedad(id_enfermedad) {
  try {
    const url_get = `${window.origin}/api/enfermedad/view/${id_enfermedad}`;
    const response = await axios.get(url_get);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

async function obtenerEnfermedades(ci_persona) {
  try {
    const url = `${window.origin}/api/enfermedad/${ci_persona}`;
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}
