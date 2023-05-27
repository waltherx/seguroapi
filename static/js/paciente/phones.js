async function modalPhone(ci_person) {
  const { value: formValues } = await Swal.fire({
    title: "Agregar Numero",
    html: `<div class="form-floating">      
      <input id="numeroTxt" type="number" class="form-control">
      <label for="numeroTxt" class="form-label">Numero:</label>
      </div><div class="form-floating">
      <input id="referenciaTxt" type="text" class="form-control">
      <label for="referenciaTxt" class="form-label">Referencia:</label> </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresPhone,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  const url = `${window.origin}/api/phone/add`;
  if (formValues) {
    const data = {
      ci_persona: ci_person,
      numero: formValues[0],
      referencia: formValues[1],
    };
    try {
      const response = await axios.post(url, data);
      const msg = response;
      Swal.fire("Correcto!", msg.data.message, "success");
      mostarPhones(ci_person);
    } catch (error) {
      Swal.fire(JSON.stringify(error, msg.data.message, "error"));
    }
  }
}

function mostarPhones(ci_persona) {
  try {
    obtenerPhones(ci_persona)
      .then((datos) => {
        llenarTabla(datos);
      })
      .catch((error) => {
        console.log("Error al obtener y llenar los datos:", error);
      });
  } catch (error) {
    console.log(error);
  }
}

function obtenerValoresPhone() {
  const input1 = document.getElementById("numeroTxt").value;
  const input2 = document.getElementById("referenciaTxt").value;
  console.log(input2);
  const numeroRegex = /^[0-9]+$/;
  const alfanumericoRegex = /^[\w\s]+$/;

  if (input1.trim() === "" && input2.trim() === "") {
    Swal.showValidationMessage(
      `Request failed: Por favor ingresa un valor en ambos campos.`
    );
  } else if (!numeroRegex.test(input1)) {
    Swal.showValidationMessage(
      `Request failed: El campo número debe contener solo números.`
    );
  } else if (!alfanumericoRegex.test(input2)) {
    Swal.showValidationMessage(
      `Request failed: El campo referencia debe contener solo letras.`
    );
  } else {
    console.log("Ambos campos tienen valores válidos.");
    return [input1, input2];
  }
}

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
    const td3 = document.createElement("td");
    const td4 = document.createElement("td");
    td1.textContent = phone.numero;
    td2.textContent = phone.referencia;

    const btnEliminar = crearBoton(true, () =>
      eliminarTelefono(phone.id, phone.referencia, phone.ci_persona)
    );
    const btnActualizar = crearBoton(false, () =>
      actualizarTelefono(phone.id, phone.ci_persona)
    );

    const contenedorBotones = document.createElement("div");
    contenedorBotones.classList.add("d-flex", "justify-content-end", "gap-2");
    contenedorBotones.appendChild(btnActualizar);
    contenedorBotones.appendChild(btnEliminar);
    td3.appendChild(contenedorBotones);
    tr.appendChild(td1);
    tr.appendChild(td2);
    tr.appendChild(td3);
    //tr.appendChild(td4);
    tablaBody.appendChild(tr);
  });
}

function crearBoton(isDelete, onClick) {
  const boton = document.createElement("button");
  boton.textContent = "";
  if (isDelete) {
    boton.innerHTML = `<i class="bi bi-trash"></i>`;
    boton.classList.add("btn", "btn-danger", "btn-sm");
  } else {
    boton.innerHTML = `<i class="bi bi-gear-fill"></i>`;
    boton.classList.add("btn", "btn-success", "btn-sm");
  }
  boton.classList.add("btn", "btn-success", "btn-sm");
  boton.addEventListener("click", onClick);
  return boton;
}

function eliminarTelefono(id, referencia, ci_persona) {
  Swal.fire({
    title: "Esta Seguro?",
    text: `Eliminar Telefono de ${referencia}!`,
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#012970",
    cancelButtonColor: "#d33",
    confirmButtonText: "Eliminar!",
  }).then((result) => {
    if (result.isConfirmed) {
      deletePhone(id)
        .then((result) => {
          console.log(result);
          Swal.fire("Eliminado!", "Telefono fue Eliminado!", "success");
          mostarPhones(ci_persona);
        })
        .catch((error) => {
          console.log("error", error);
        });
    }
  });
  console.log("Eliminar teléfono con ID:", id);
}

async function deletePhone(id, ci_persona) {
  try {
    const url = `${window.origin}/api/phone/delete/${id}`;
    const response = await axios.delete(url);
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

function actualizarTelefono(id, ci_persona) {
  try {
    console.log("Actualizar teléfono con ID:", id);
    update_phone(id, ci_persona);
  } catch (error) {
    console.log(error);
  }
}

async function update_phone(id_telefono, ci_person) {
  const url_get = `${window.origin}/api/phone/${ci_person}/${id_telefono}`;
  const response = await axios.get(url_get);
  phone = response.data;
  const { value: formValues } = await Swal.fire({
    title: "Agregar Numero",
    html: `<div class="form-floating">      
      <input id="numeroTxt" type="number" value="${phone.numero}" class="form-control">
      <label for="numeroTxt" class="form-label">Numero:</label>
      </div><div class="form-floating">
      <input id="referenciaTxt" type="text" value="${phone.referencia}" class="form-control">
      <label for="referenciaTxt" class="form-label">Referencia:</label> </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresPhone,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  if (formValues) {
    const data = {
      id_telefono: id_telefono,
      numero: formValues[0],
      referencia: formValues[1],
    };
    try {
      const url_put = `${window.origin}/api/phone/update`;
      const response = await axios.put(url_put, data);
      Swal.fire("Correcto!", "Acualizado", "success");
      mostarPhones(ci_person);
    } catch (error) {
      Swal.fire(JSON.stringify("error", response.data, "error"));
    }
  }
}

async function view_phone(id_telefono, ci_persona) {
  try {
    const url_get = `${window.origin}/api/phone/${ci_persona}/${id_telefono}`;
    const response = await axios.get(url_get);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}
