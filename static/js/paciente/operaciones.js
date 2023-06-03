async function modalOperacion(ci_person, id_paciente) {
  const { value: formValues } = await Swal.fire({
    title: "Agregar Operacion",
    html: `<div class="form-floating">
            <input id="tipoTxt" type="text" class="form-control">
            <label for="tipoTxt" class="form-label">Tipo de Operacion:</label>
          </div>
          <div class="form-floating">
            <input id="fechaTxt" type="date" class="form-control">
            <label for="fechaTxt" class="form-label">Fecha:</label>
          </div>
          <div class="form-floating">
            <input id="descripTxt" type="text" class="form-control">
            <label for="descripTxt" class="form-label">Descripcion:</label>
          </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresOperacion,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });
  console.log(formValues);
  if (formValues) {
    const data = {
      id_paciente: id_paciente,
      tipo: formValues[0],
      fecha: formValues[1],
      descripcion: formValues[2],
    };
    console.log(data);
    add_operacion_paciente(data)
      .then((result) => {
        notificacionSwal(result.data.message, "success");
        mostrarOperacions(ci_person);
      })
      .catch((error) => {
        notificacionSwal(result.data.message, "error");
      });
  }
}

function obtenerValoresOperacion() {
  const input1 = document.getElementById("tipoTxt").value;
  const input2 = document.getElementById("fechaTxt").value;
  const input3 = document.getElementById("descripTxt").value;

  if (input1.trim() === "") {
    Swal.showValidationMessage(
      `Request failed: Por favor ingresa un Nombre de Operacion.`
    );
  } else if (input2 === "") {
    Swal.showValidationMessage("Por favor ingresa una Fecha.");
    return;
  } else {
    console.log("Ambos campos tienen valores válidos.");
    return [input1, input2, input3];
  }
}

function llenarTablaOperacion(datos, ci_person) {
  const tablaBody = document.getElementById("toperacion");
  tablaBody.innerHTML = "";
  datos.forEach((operacion) => {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td");
    const td2 = document.createElement("td");
    const td3 = document.createElement("td");
    const td4 = document.createElement("td");

    td1.textContent = operacion.tipo;
    td2.textContent = operacion.fecha;
    td3.textContent = operacion.descripcion;

    const btnEliminar = crearBotonOperacion(true, () =>
      eliminarOperacion(operacion.id, operacion.tipo, ci_person)
    );
    const btnActualizar = crearBotonOperacion(false, () =>
      actualizarOperacion(operacion.id, ci_person)
    );

    const contenedorBotones = document.createElement("div");
    contenedorBotones.classList.add("d-flex", "justify-content-end", "gap-2");
    contenedorBotones.appendChild(btnActualizar);
    contenedorBotones.appendChild(btnEliminar);
    td4.appendChild(contenedorBotones);

    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);

    tablaBody.appendChild(tr);
  });
}

function crearBotonOperacion(isDelete, onClick) {
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

function eliminarOperacion(id, nombre, ci_persona) {
  Swal.fire({
    title: "Esta Seguro?",
    text: `Eliminar Operacion de ${nombre}!`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#012970",
    cancelButtonColor: "#d33",
    confirmButtonText: "Eliminar!",
  }).then((result) => {
    if (result.isConfirmed) {
      delete_operacion_paciente(id)
        .then((response) => {
          notificacionSwal(response.data.message, "success");
          mostrarOperacions(ci_persona);
        })
        .catch((error) => {
          notificacionSwal(result.data.message, "error");
        });
    }
  });
}

function actualizarOperacion(id_operacion, ci_persona) {
  try {
    console.log(id_operacion);
    update_Operacion(id_operacion, ci_persona);
  } catch (error) {
    console.log(error);
  }
}

function mostrarOperacions(ci_persona) {
  get_operacions(ci_persona)
    .then((datos) => {
      llenarTablaOperacion(datos, ci_persona);
    })
    .catch((error) => {
      console.log("Error al obtener y llenar los datos:", error);
    });
}

async function update_Operacion(id_operacion, ci_person) {
  const url_get = `${window.origin}/api/operacion/view/${id_operacion}`;
  const response = await axios.get(url_get);
  const operacion = response.data;
  console.log(operacion);
  const { value: formValues } = await Swal.fire({
    title: "Actualizar Operacion",
    html: `<div class="form-floating">
            <input id="tipoTxt" type="text" value="${operacion.tipo}" class="form-control">
            <label for="tipoTxt" class="form-label">Tipo de Operacion:</label>
          </div>
          <div class="form-floating">
            <input id="fechaTxt" type="date" value="${operacion.fecha}" class="form-control">
            <label for="fechaTxt" class="form-label">Fecha:</label>
          </div>
          <div class="form-floating">
            <input id="descripTxt" type="text" value="${operacion.descripcion}" class="form-control">
            <label for="descripTxt" class="form-label">Descripcion:</label>
          </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresOperacion,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  if (formValues) {
    const data = {
      id: id_operacion,
      tipo: formValues[0],
      fecha: formValues[1],
      descripcion: formValues[2],
      id_paciente: operacion.paciente_id,
    };
    console.log(data);
    update_operacion_paciente(data)
      .then((result) => {
        notificacionSwal(result.data.message, "success");
        mostrarOperacions(ci_person);
      })
      .catch((error) => {
        notificacionSwal(result.data.message, "error");
      });
  }
}

async function get_operacions(ci_persona) {
  try {
    const url = `${window.origin}/api/operacion/${ci_persona}`;
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

async function add_operacion_paciente(datos) {
  try {
    const url = `${window.origin}/api/operacion/add`;
    const response = await axios.post(url, datos);
    return response;
  } catch (error) {
    console.log(error);
  }
}

async function update_operacion_paciente(datos) {
  try {
    const url_put = `${window.origin}/api/operacion/update`;
    const response = await axios.put(url_put, datos);
    return response;
  } catch (error) {
    console.log(error);
  }
}

async function delete_operacion_paciente(id) {
  try {
    const url = `${window.origin}/api/operacion/delete/${id}`;
    const response = await axios.delete(url);
    return response;
  } catch (error) {
    console.error(error);
  }
}
