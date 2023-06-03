async function modalVacuna(ci_person, id_paciente) {
  const { value: formValues } = await Swal.fire({
    title: "Agregar Vacuna",
    html: `<div class="form-floating">
            <input id="nombreTxt" type="text" class="form-control">
            <label for="nombreTxt" class="form-label">Nombre:</label>
          </div>
        <div class="form-floating">
          <input id="dosisTxt" type="number" class="form-control">
          <label for="dosisTxt" class="form-label">Dosis:</label>
        </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresVacuna,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  if (formValues) {
    const data = {
      id_paciente: id_paciente,
      nombre: formValues[0],
      dosis: formValues[1],
    };

    add_vacuna_paciente(data)
      .then((result) => {
        notificacionSwal(result.data.message, "success");
        mostrarVacunas(ci_person);
      })
      .catch((error) => {
        notificacionSwal(result.data.message, "error");
      });
  }
}

function obtenerValoresVacuna() {
  const input1 = document.getElementById("nombreTxt").value;
  const input2 = document.getElementById("dosisTxt").value;
  const regex = /^\d+$/;

  if (input1.trim() === "") {
    Swal.showValidationMessage(
      `Request failed: Por favor ingresa un Nombre de Vacuna.`
    );
  } else if (!regex.test(input2)) {
    Swal.showValidationMessage("Por favor ingresa solo números en dosis.");
    return;
  }else {
    console.log("Ambos campos tienen valores válidos.");
    return [input1, input2];
  }
}

function llenarTablaVacuna(datos, ci_person) {
  const tablaBody = document.getElementById("tvacuna");
  tablaBody.innerHTML = "";
  datos.forEach((vacuna) => {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td");
    const td2 = document.createElement("td");
    const td3 = document.createElement("td");
    
    td1.textContent = vacuna.nombre;
    td2.textContent = vacuna.dosis;    

    const btnEliminar = crearBotonVacuna(true, () =>
      eliminarVacuna(vacuna.id, vacuna.nombre, ci_person)
    );
    const btnActualizar = crearBotonVacuna(false, () =>
      actualizarVacuna(vacuna.id, ci_person)
    );

    const contenedorBotones = document.createElement("div");
    contenedorBotones.classList.add("d-flex", "justify-content-end", "gap-2");
    contenedorBotones.appendChild(btnActualizar);
    contenedorBotones.appendChild(btnEliminar);
    td3.appendChild(contenedorBotones);

    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tablaBody.appendChild(tr);
  });
}

function crearBotonVacuna(isDelete, onClick) {
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

function eliminarVacuna(id, nombre, ci_persona) {
  Swal.fire({
    title: "Esta Seguro?",
    text: `Eliminar Vacuna de ${nombre}!`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#012970",
    cancelButtonColor: "#d33",
    confirmButtonText: "Eliminar!",
  }).then((result) => {
    if (result.isConfirmed) {
      delete_vacuna_paciente(id)
        .then((response) => {
          notificacionSwal(response.data.message, "success");
          mostrarVacunas(ci_persona);
        })
        .catch((error) => {
          notificacionSwal(result.data.message, "error");
        });
    }
  });
}

function actualizarVacuna(id_vacuna, ci_persona) {
  try {
    console.log(id_vacuna);
    update_Vacuna(id_vacuna, ci_persona);
  } catch (error) {
    console.log(error);
  }
}

function mostrarVacunas(ci_persona) {
  get_vacunas(ci_persona)
    .then((datos) => {
      llenarTablaVacuna(datos, ci_persona);
    })
    .catch((error) => {
      console.log("Error al obtener y llenar los datos:", error);
    });
}

async function update_Vacuna(id_vacuna, ci_person) {
  const url_get = `${window.origin}/api/vacuna/view/${id_vacuna}`;
  const response = await axios.get(url_get);
  const vacuna = response.data;
  console.log(vacuna);
  const { value: formValues } = await Swal.fire({
    title: "Actualizar Vacuna",
    html: `<div class="form-floating">
              <input id="nombreTxt" type="text" value="${vacuna.nombre}" class="form-control">
              <label for="nombreTxt" class="form-label">Nombre:</label>
            </div>
          <div class="form-floating">
            <input id="dosisTxt" type="number" value="${vacuna.dosis}" class="form-control">
            <label for="dosisTxt" class="form-label">Descripcion:</label>
          </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresVacuna,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  if (formValues) {
    const data = {
      id: id_vacuna,
      nombre: formValues[0],
      dosis: formValues[1],
      id_paciente: vacuna.paciente_id,
    };

    update_vacuna_paciente(data)
      .then((result) => {
        notificacionSwal(result.data.message, "success");
        mostrarVacunas(ci_person);
      })
      .catch((error) => {
        notificacionSwal(result.data.message, "error");
      });
  }
}

async function get_vacunas(ci_persona) {
  try {
    const url = `${window.origin}/api/vacuna/${ci_persona}`;
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

async function add_vacuna_paciente(datos) {
  try {
    const url = `${window.origin}/api/vacuna/add`;
    const response = await axios.post(url, datos);
    return response;
  } catch (error) {
    console.log(error);
  }
}

async function update_vacuna_paciente(datos) {
  try {
    const url_put = `${window.origin}/api/vacuna/update`;
    const response = await axios.put(url_put, datos);
    return response;
  } catch (error) {
    console.log(error);
  }
}

async function delete_vacuna_paciente(id) {
  try {
    const url = `${window.origin}/api/vacuna/delete/${id}`;
    const response = await axios.delete(url);
    return response;
  } catch (error) {
    console.error(error);
  }
}
