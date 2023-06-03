async function modalAlergia(ci_person, id_paciente) {
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

  if (formValues) {
    const data = {
      id_paciente: id_paciente,
      nombre: formValues[0],
      descripcion: formValues[1],
      gravedad: formValues[2],
      reaccion: formValues[3],
    };

    add_alergia_paciente(data)
      .then((result) => {
        notificacionSwal(result.data.message, "success");
        mostrarAlergias(ci_person);
      })
      .catch((error) => {
        notificacionSwal(result.data.message, "error");
      });
  }
}

async function add_alergia_paciente(datos) {
  try {
    const url = `${window.origin}/api/alergia/add`;
    const response = await axios.post(url, datos);
    return response;
  } catch (error) {
    console.log(error);
  }
}

function mostrarAlergias(ci_persona) {
  obtenerAlergias(ci_persona)
    .then((datos) => {
      llenarTablaAlergia(datos, ci_persona);
    })
    .catch((error) => {
      console.log("Error al obtener y llenar los datos:", error);
    });
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

function llenarTablaAlergia(datos, ci_person) {
  const tablaBody = document.getElementById("talergia");
  tablaBody.innerHTML = "";
  datos.forEach((alergia) => {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td");
    const td2 = document.createElement("td");
    const td3 = document.createElement("td");
    const td4 = document.createElement("td");
    const td5 = document.createElement("td");
    td1.textContent = alergia.nombre;
    td2.textContent = alergia.descripcion;
    td3.textContent = alergia.gravedad;
    td4.textContent = alergia.reaccion;

    const btnEliminar = crearBotonAlergia(true, () =>
      eliminarAlergia(alergia.id, alergia.nombre, ci_person)
    );
    const btnActualizar = crearBotonAlergia(false, () =>
      actualizarAlergia(alergia.id, ci_person)
    );

    const contenedorBotones = document.createElement("div");
    contenedorBotones.classList.add("d-flex", "justify-content-end", "gap-2");
    contenedorBotones.appendChild(btnActualizar);
    contenedorBotones.appendChild(btnEliminar);
    td5.appendChild(contenedorBotones);

    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td5);
    tablaBody.appendChild(tr);
  });
}

function crearBotonAlergia(isDelete, onClick) {
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

function eliminarAlergia(id, nombre, ci_persona) {
  Swal.fire({
    title: "Esta Seguro?",
    text: `Eliminar Alergia de ${nombre}!`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#012970",
    cancelButtonColor: "#d33",
    confirmButtonText: "Eliminar!",
  }).then((result) => {
    if (result.isConfirmed) {
      delete_alergia_paciente(id)
        .then((result) => {
          notificacionSwal(result.data.message, "success");
          mostrarAlergias(ci_persona);
        })
        .catch((error) => {
          notificacionSwal(result.data.message, "error");
        });
    }
  });
}

async function delete_alergia_paciente(id) {
  try {
    const url = `${window.origin}/api/alergia/delete/${id}`;
    const response = await axios.delete(url);
    return response;
  } catch (error) {
    console.error(error);
  }
}

function actualizarAlergia(id_alergia, ci_persona) {
  try {
    console.log(id_alergia);
    update_Alergia(id_alergia, ci_persona);
  } catch (error) {
    console.log(error);
  }
}

async function update_Alergia(id_alergia, ci_person) {
  const url_get = `${window.origin}/api/alergia/view/${id_alergia}`;
  const response = await axios.get(url_get);
  const alergia = response.data;
  console.log(alergia);
  const { value: formValues } = await Swal.fire({
    title: "Actualizar Alergia",
    html: `<div class="form-floating">
              <input id="nombreTxt" type="text" value="${alergia.nombre}" class="form-control">
              <label for="nombreTxt" class="form-label">Nombre:</label>
            </div>
          <div class="form-floating">
            <input id="descrTxt" type="text" value="${alergia.descripcion}" class="form-control">
            <label for="descrTxt" class="form-label">Descripcion:</label>
          </div>
          <div class="form-floating">
            <input id="gravedadTxt" type="text" value="${alergia.gravedad}" class="form-control">
            <label for="gravedadTxt" class="form-label">Gravedad:</label>
          </div>
          <div class="form-floating">
            <input id="reaccionTxt" type="text" value="${alergia.reaccion}" class="form-control">
            <label for="reaccionTxt" class="form-label">Reaccion:</label>
          </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresAlergia,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  if (formValues) {
    const data = {
      id: id_alergia,
      nombre: formValues[0],
      descripcion: formValues[1],
      gravedad: formValues[2],
      reaccion: formValues[3],
      id_paciente: alergia.paciente_id,
    };

    update_alergia_paciente(data)
      .then((result) => {
        notificacionSwal(response.data.message, "success");
        mostrarAlergias(ci_person);
      })
      .catch((error) => {
        notificacionSwal(result.data.message, "error");
      });
  }
}

async function update_alergia_paciente(datos) {
  try {
    const url_put = `${window.origin}/api/alergia/update`;
    const response = await axios.put(url_put, datos);
    return response;
  } catch (error) {
    console.log(error);
  }
}
