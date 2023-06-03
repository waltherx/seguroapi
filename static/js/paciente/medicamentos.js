async function modalMedicamento(ci_person, id_paciente) {
  const { value: formValues } = await Swal.fire({
    title: "Agregar Medicamento",
    html: `<div class="form-floating">
            <input id="nombreTxt" type="text" class="form-control">
            <label for="nombreTxt" class="form-label">Nombre:</label>
          </div>
          <div class="form-floating">
            <input id="descripTxt" type="text" class="form-control">
            <label for="descripTxt" class="form-label">Descripcion:</label>
          </div>
          <div class="form-floating">
            <input id="cantidadTxt" type="number" class="form-control">
            <label for="cantidadTxt" class="form-label">Cantidad:</label>
          </div>
        <div class="form-floating">
          <input id="unidadTxt" type="text" class="form-control">
          <label for="unidadTxt" class="form-label">Unidad de Medida:</label>
        </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresMedicamento,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  if (formValues) {
    const data = {
      id_paciente: id_paciente,
      nombre: formValues[0],
      descripcion: formValues[1],
      cantidad: parseInt(formValues[2]),
      unidad: formValues[3],
    };
    console.log(data);
    add_medicamento_paciente(data)
      .then((result) => {
        notificacionSwal(result.data.message, "success");
        mostrarMedicamentos(ci_person);
      })
      .catch((error) => {
        notificacionSwal(result.data.message, "error");
      });
  }
}

function obtenerValoresMedicamento() {
  const input1 = document.getElementById("nombreTxt").value;
  const input2 = document.getElementById("descripTxt").value;
  const input3 = document.getElementById("cantidadTxt").value;
  const input4 = document.getElementById("unidadTxt").value;
  const regex = /^\d+$/;

  if (input1.trim() === "") {
    Swal.showValidationMessage(
      `Request failed: Por favor ingresa un Nombre de Medicamento.`
    );
  } else if (input3 !== "" && !regex.test(input3)) {
    Swal.showValidationMessage("Por favor ingresa solo números en dosis.");
  } else {
    console.log("Ambos campos tienen valores válidos.");
    return [input1, input2, input3, input4];
  }
}

function llenarTablaMedicamento(datos, ci_person) {
  const tablaBody = document.getElementById("tmedicamento");
  tablaBody.innerHTML = "";
  datos.forEach((medicamento) => {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td");
    const td2 = document.createElement("td");
    const td3 = document.createElement("td");
    const td4 = document.createElement("td");
    const td5 = document.createElement("td");

    td1.textContent = medicamento.nombre;
    td2.textContent = medicamento.descripcion;
    td3.textContent = medicamento.unidad;
    td4.textContent = medicamento.cantidad;

    const btnEliminar = crearBotonMedicamento(true, () =>
      eliminarMedicamento(medicamento.id, medicamento.nombre, ci_person)
    );
    const btnActualizar = crearBotonMedicamento(false, () =>
      actualizarMedicamento(medicamento.id, ci_person)
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

function crearBotonMedicamento(isDelete, onClick) {
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

function eliminarMedicamento(id, nombre, ci_persona) {
  Swal.fire({
    title: "Esta Seguro?",
    text: `Eliminar Medicamento de ${nombre}!`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#012970",
    cancelButtonColor: "#d33",
    confirmButtonText: "Eliminar!",
  }).then((result) => {
    if (result.isConfirmed) {
      delete_medicamento_paciente(id)
        .then((response) => {
          notificacionSwal(response.data.message, "success");
          mostrarMedicamentos(ci_persona);
        })
        .catch((error) => {
          notificacionSwal(error.response, "error");
        });
    }
  });
}

function actualizarMedicamento(id_medicamento, ci_persona) {
  try {
    console.log(id_medicamento);
    update_Medicamento(id_medicamento, ci_persona);
  } catch (error) {
    console.log(error);
  }
}

function mostrarMedicamentos(ci_persona) {
  get_medicamentos(ci_persona)
    .then((datos) => {
      llenarTablaMedicamento(datos, ci_persona);
    })
    .catch((error) => {
      console.log("Error al obtener y llenar los datos:", error);
    });
}

async function update_Medicamento(id_medicamento, ci_person) {
  const url_get = `${window.origin}/api/medicamento/view/${id_medicamento}`;
  const response = await axios.get(url_get);
  const medicamento = response.data;
  console.log(medicamento);
  const { value: formValues } = await Swal.fire({
    title: "Actualizar Medicamento",
    html: `<div class="form-floating">
            <input id="nombreTxt" type="text" value="${medicamento.nombre}" class="form-control">
            <label for="nombreTxt" class="form-label">Nombre:</label>
          </div>
          <div class="form-floating">
            <input id="descripTxt" type="text" value="${medicamento.descripcion}" class="form-control">
            <label for="descripTxt" class="form-label">Descripcion:</label>
          </div>
          <div class="form-floating">
            <input id="cantidadTxt" type="number" value="${medicamento.cantidad}" class="form-control">
            <label for="cantidadTxt" class="form-label">Cantidad:</label>
          </div>
        <div class="form-floating">
          <input id="unidadTxt" type="text" value="${medicamento.unidad}" class="form-control">
          <label for="unidadTxt" class="form-label">Unidad de Medida:</label>
        </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresMedicamento,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  if (formValues) {
    const data = {
      id: id_medicamento,
      nombre: formValues[0],
      descripcion: formValues[1],
      cantidad: parseInt(formValues[2]),
      unidad: formValues[3],
      id_paciente: medicamento.paciente_id,
    };

    update_medicamento_paciente(data)
      .then((result) => {
        notificacionSwal(result.data.message, "success");
        mostrarMedicamentos(ci_person);
      })
      .catch((error) => {
        notificacionSwal(result.data.message, "error");
      });
  }
}

async function get_medicamentos(ci_persona) {
  try {
    const url = `${window.origin}/api/medicamento/${ci_persona}`;
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

async function add_medicamento_paciente(datos) {
  try {
    const url = `${window.origin}/api/medicamento/add`;
    const response = await axios.post(url, datos);
    return response;
  } catch (error) {
    console.log(error);
  }
}

async function update_medicamento_paciente(datos) {
  try {
    const url_put = `${window.origin}/api/medicamento/update`;
    const response = await axios.put(url_put, datos);
    return response;
  } catch (error) {
    console.log(error);
  }
}

async function delete_medicamento_paciente(id) {
  try {
    const url = `${window.origin}/api/medicamento/delete/${id}`;
    const response = await axios.delete(url);
    return response;
  } catch (error) {
    console.error(error);
  }
}
