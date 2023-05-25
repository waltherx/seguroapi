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
    preConfirm: obtenerValores,
    confirmButtonText:'Aceptar',
    confirmButtonColor: '#012970',
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
      obtenerPhones(ci_person)
        .then((datos) => {
          llenarTabla(datos);
        })
        .catch((error) => {
          console.log("Error al obtener y llenar los datos:", error);
        });
    } catch (error) {
      Swal.fire(JSON.stringify(error, msg.data.message, "error"));
    }
  }
}

function obtenerValores() {
  const input1 = document.getElementById("numeroTxt").value;
  const input2 = document.getElementById("referenciaTxt").value;

  const numeroRegex = /^[0-9]+$/;
  const alfanumericoRegex = /^[a-zA-Z0-9]+$/;

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
    td1.textContent = phone.numero;
    td2.textContent = phone.referencia;
    tr.appendChild(td1);
    tr.appendChild(td2);
    tablaBody.appendChild(tr);
  });
}
