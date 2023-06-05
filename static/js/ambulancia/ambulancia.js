async function modalAmbulancia() {
  const { value: formValues } = await Swal.fire({
    title: "Agregar Ambulancia",
    html: `<div class="form-floating">
              <input id="modeloTxt" type="text" class="form-control">
              <label for="modeloTxt" class="form-label">Modelo:</label>
            </div>
            <div class="form-floating">
              <input id="marcaTxt" type="text" class="form-control">
              <label for="marcaTxt" class="form-label">Marca:</label>
            </div>
          <div class="form-floating">
            <input id="placaTxt" type="text" class="form-control">
            <label for="placaTxt" class="form-label">Placa:</label>
          </div>
          <div class="row">
          <div class="col">
            <div class="form-floating">
              <input id="anioTxt" type="number" class="form-control">
              <label for="anioTxt" class="form-label">Año:</label>
            </div>
          </div>
          <div class="col">
            <div class="form-floating">
              <input id="capacidadTxt" type="number" class="form-control">
              <label for="capacidadTxt" class="form-label">Capacidad:</label>
            </div>
          </div>
        </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresAmbulancia,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
    customClass: {
      title: "my-swal-title",
      htmlContainer: "my-swal-container",
      content: "my-swal-modal",
    },
  });

  if (formValues) {
    const data = {
      modelo: formValues[0],
      marca: formValues[1],
      anio: parseInt(formValues[2]),
      placa: formValues[3],
      capacidad: parseInt(formValues[4]),
    };
    console.log(formValues);
    console.log(data);
    add_ambulancia(data)
      .then((result) => {
        notificacionSwal(result.data.message, "success");
        //mostrarAmbulancias();
        location.href = "/ambulancia";
      })
      .catch((error) => {
        notificacionSwal(result.data.message, "error");
      });
  }
}

function obtenerValoresAmbulancia() {
  const input1 = document.getElementById("modeloTxt").value;
  const input2 = document.getElementById("marcaTxt").value;
  const input3 = document.getElementById("anioTxt").value;
  const input4 = document.getElementById("placaTxt").value;
  const input5 = document.getElementById("capacidadTxt").value;
  const regex = /^\d+$/;

  if (input1.trim() === "") {
    Swal.showValidationMessage(
      `Request failed: Por favor ingresa un Nombre de Ambulancia.`
    );
  } else {
    return [input1, input2, input3, input4, input5];
  }
}

function llenarTablaAmbulancia(datos) {
  const tablaBody = document.getElementById("tambulancias");
  tablaBody.innerHTML = "";
  let count = 1;
  datos.forEach((ambulancia) => {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td");
    const td2 = document.createElement("td");
    const td3 = document.createElement("td");
    const td4 = document.createElement("td");
    const td5 = document.createElement("td");
    const td6 = document.createElement("td");
    const td7 = document.createElement("td");

    td1.textContent = count;
    td2.textContent = ambulancia.modelo;
    td3.textContent = ambulancia.marca;
    td4.textContent = ambulancia.anio;
    td5.textContent = ambulancia.placa;
    td6.textContent = ambulancia.capacidad;
    count++;

    const btnEliminar = crearBotonAmbulancia(true, () =>
      eliminarAmbulancia(ambulancia.id, ambulancia.nombre)
    );
    const btnActualizar = crearBotonAmbulancia(false, () =>
      actualizarAmbulancia(ambulancia.id)
    );

    const contenedorBotones = document.createElement("div");
    contenedorBotones.classList.add("d-flex", "justify-content-end", "gap-2");
    contenedorBotones.appendChild(btnActualizar);
    contenedorBotones.appendChild(btnEliminar);
    td7.appendChild(contenedorBotones);

    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    tr.appendChild(td4);
    tr.appendChild(td5);
    tr.appendChild(td6);
    tr.appendChild(td7);
    tablaBody.appendChild(tr);
  });
}

function crearBotonAmbulancia(isDelete, onClick) {
  const boton = document.createElement("button");
  boton.textContent = "";
  if (isDelete) {
    boton.innerHTML = `<i class=" bi bi-trash"></i>`;
    boton.classList.add("hidden", "btn", "btn-danger", "btn-sm");
  } else {
    boton.innerHTML = `<i class="bi bi-gear-fill"></i>`;
    boton.classList.add("btn", "btn-success", "btn-sm");
  }
  //boton.classList.add("btn", "btn-success", "btn-sm");
  boton.addEventListener("click", onClick);
  return boton;
}

function eliminarAmbulancia(id, nombre) {
  Swal.fire({
    title: "Esta Seguro?",
    text: `Eliminar Ambulancia de ${nombre}!`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#012970",
    cancelButtonColor: "#d33",
    confirmButtonText: "Eliminar!",
  }).then((result) => {
    if (result.isConfirmed) {
      delete_ambulancia(id)
        .then((response) => {
          notificacionSwal(response.data.message, "success");
          mostrarAmbulancias();
        })
        .catch((error) => {
          notificacionSwal(error.response, "error");
        });
    }
  });
}

function actualizarAmbulancia(id_ambulancia) {
  try {
    console.log(id_ambulancia);
    update_Ambulancia(id_ambulancia);
  } catch (error) {
    console.log(error);
  }
}

function mostrarAmbulancias() {
  get_ambulancias()
    .then((datos) => {
      llenarTablaAmbulancia(datos);
    })
    .catch((error) => {
      console.log("Error al obtener y llenar los datos:", error);
    });
}

async function update_Ambulancia(id_ambulancia) {
  const url_get = `${window.origin}/api/ambulancia/view/${id_ambulancia}`;
  const response = await axios.get(url_get);
  const ambulancia = response.data;
  console.log(ambulancia);
  const { value: formValues } = await Swal.fire({
    title: "Actualizar Ambulancia",
    html: `<div class="form-floating">
              <input id="modeloTxt" type="text" value="${ambulancia.modelo}" class="form-control">
              <label for="modeloTxt" class="form-label">Modelo:</label>
            </div>
            <div class="form-floating">
              <input id="marcaTxt" type="text" value="${ambulancia.marca}" class="form-control">
              <label for="marcaTxt" class="form-label">Marca:</label>
            </div>
            <div class="form-floating">
              <input id="placaTxt" type="number" value="${ambulancia.anio}" class="form-control">
              <label for="placaTxt" class="form-label">Año:</label>
            </div>
          <div class="form-floating">
            <input id="anioTxt" type="text" value="${ambulancia.placa}" class="form-control">
            <label for="anioTxt" class="form-label">Placa:</label>
          </div>
          <div class="form-floating">
            <input id="capacidadTxt" type="number" value="${ambulancia.capacidad}" class="form-control">
            <label for="capacidadTxt" class="form-label">Capacidad:</label>
          </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresAmbulancia,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  if (formValues) {
    const data = {
      id: id_ambulancia,
      modelo: formValues[0],
      marca: formValues[1],
      anio: parseInt(formValues[2]),
      placa: formValues[3],
      capacidad: parseInt(formValues[4]),
    };
    update_ambulancia(data)
      .then((result) => {
        notificacionSwal(result.data.message, "success");
        mostrarAmbulancias();
      })
      .catch((error) => {
        notificacionSwal(result.data.message, "error");
      });
  }
}

async function get_ambulancias() {
  try {
    const url = `${window.origin}/api/ambulancia`;
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

async function add_ambulancia(datos) {
  try {
    const url = `${window.origin}/api/ambulancia/add`;
    const response = await axios.post(url, datos);
    return response;
  } catch (error) {
    console.log(error);
  }
}

async function update_ambulancia(datos) {
  try {
    const url_put = `${window.origin}/api/ambulancia/update`;
    const response = await axios.put(url_put, datos);
    return response;
  } catch (error) {
    console.log(error);
  }
}

async function delete_ambulancia(id) {
  try {
    const url = `${window.origin}/api/ambulancia/delete/${id}`;
    const response = await axios.delete(url);
    return response;
  } catch (error) {
    console.error(error);
  }
}
