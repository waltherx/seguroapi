function handleBlur() {
  const ci_person = document.getElementById("ciTxt").value;
  console.log(ci_person);
  get_persona_2(ci_person)
    .then((response) => {
      if (response.status === 200) {
        const persona = response.data;
        console.log(persona.nombres);
        console.log(persona.apellidos);
        console.log(persona.direccion);
      }
    })
    .catch((error) => console.log(error));
}

async function add_medico_2() {
  const steps = ["1", "2", "3"];
  const swalQueueStep = Swal.mixin({
    progressSteps: steps,
    //cancelButtonText: 'Atras',
    confirmButtonText: "Siguiente",
    reverseButtons: true,
    showCloseButton: true,

    showClass: { backdrop: "swal2-noanimation" },
    hideClass: { backdrop: "swal2-noanimation" },
  });

  const { value: result1 } = await swalQueueStep.fire({
    title: "Datos Personales",
    currentProgressStep: 0,
    allowOutsideClick: true,
    html: `<div class="row">
          <div class="col">
            <div class="form-floating">
              <input
                type="number"
                class="form-control"
                id="ciTxt"
                name="ciTxt"
                required
              />
              <label for="ciTxt">CI:</label>
            </div>
          </div>
          <div class="col">
            <div class="form-floating">
              
              <input
                type="date"
                class="form-control"
                id="fechaTxt"
                name="fechaTxt"
                required
              />
              <label for="fechaTxt">Fecha de Nacimiento:</label>
            </div>
          </div>
        </div>
  
        <div class="form-floating">
          
          <input
            type="text"
            class="form-control"
            id="nombreTxt"
            name="nombreTxt"
            required
          />
          <label for="nombreTxt">Nombres:</label>
        </div>
        <div class="form-floating">
          
          <input
            type="text"
            class="form-control"
            id="apellidoTxt"
            name="apellidoTxt"
            required
          />
          <label for="apellidoTxt">Apellidos:</label>
        </div>
  
        <div class="form-floating">
          
          <input
            type="text"
            class="form-control"
            id="direccionTxt"
            name="direccionTxt"
          />
          <label for="direccionTxt">Direccion:</label>
        </div>
  
        <div class="row">
          <div class="col">
            <div class="form-floating">
              
              <select
                class="form-select"
                id="generoTxt"
                name="generoTxt"
                required
              >
                <option value="h">Hombre</option>
                <option value="m">Mujer</option>
                <option value="nb">No binario</option>
                <option value="gf">Género fluido</option>
                <option value="tr">Transgénero</option>
                <option value="ci">Cisgénero</option>
                <option value="ag">Agénero</option>
                <option value="bi">Bigénero</option>
                <option value="pa">Pangénero</option>
                <option value="otro">Otro/No especificado</option>
              </select>
              <label for="generoTxt">Genero:</label>
            </div>
          </div>
          <div class="col">
            <div class="form-floating">
              
              <select
                class="form-select"
                id="estadocTxt"
                name="estadocTxt"
                required
              >
                <option value="s">Soltero/a</option>
                <option value="c">Casado/a</option>
                <option value="d">Divorciado/a</option>
                <option value="v">Viudo/a</option>
                <option value="p">Conviviendo en pareja</option>
                <option value="o">Otro/No especificado</option>
              </select>
              <label for="estadocTxt">Estado Civil:</label>
            </div>
          </div>
        </div>`,
    didOpen: () => {
      //const ciTxt = document.getElementById("ciTxt");
      //ciTxt.addEventListener("blur", handleBlur);
    },
    customClass: {
      title: "my-swal-title",
      htmlContainer: "my-swal-container",
      content: "my-swal-modal",
    },
    preConfirm: obtenerValoresPersona,
    confirmButtonColor: "#012970",
  });

  if (result1) {
    console.log(JSON.stringify(result1));
    const { value: result2 } = await swalQueueStep.fire({
      title: "Datos Medico",
      allowOutsideClick: true,
      currentProgressStep: 1,
      showCancelButton: true,
      html: `
      <div class="row">
            <div class="form-floating">
              <input
                type="Text"
                class="form-control"
                id="especialidadtxt"
                required
              />
              <label for="especialidadtxt">Especialidad</label>
            </div>
        </div>
        <div class="row">
            <div class="form-floating">
              <select
                class="form-select"
                id="hospitalTxt"
                placeholder="Cargando..."
                required
              >
              <option value="x" selected>Cargando...</option>
              </select>
              <label for="hospitalTxt">Hospital</label>
          </div>
          `,
      didOpen: () => {
        const hospitalTxt = document.getElementById("hospitalTxt");
        let optionToRemove = hospitalTxt.querySelector('option[value="x"]');
        get_all_hospitals()
          .then((hospitals) => {
            hospitals.forEach((hospital) => {
              optionToRemove.remove();
              let option = document.createElement("option");
              option.value = hospital.id;
              option.text = hospital.nombre;
              hospitalTxt.appendChild(option);
            });
          })
          .catch((error) => {
            console.log(error);
          });
      },
      preConfirm: obtenerValoresMedico,
      confirmButtonColor: "#012970",
    });
    if (result2) {
      console.log(JSON.stringify(result2));
      const { value: result3 } = await swalQueueStep.fire({
        title: "Datos Usuario",
        currentProgressStep: 2,
        allowOutsideClick: true,
        confirmButtonText: "OK",
        showCancelButton: true,
        html: `
      <div class="form-floating">
        <input
          type="text"
          class="form-control"
          id="nameuserTxt"
          name="nameuserTxt"
          required
        />
        <label for="nameuserTxt">Nombre de Usuario:</label>
      </div>
      <div class="form-floating">
        <input
          type="email"
          class="form-control"
          id="emailTxt"
          name="emailTxt"
          required
        />
        <label for="emailTxt">Email:</label>
      </div>
      <div class="form-floating">
        <input
          type="password"
          class="form-control"
          id="passwordTxt"
          name="passwordTxt"
          required
        />
        <label for="passwordTxt">Contraseña:</label>
      </div>
      <div class="form-floating">
        <input
          type="password"
          class="form-control"
          id="passwordConfTxt"
          name="passwordConfTxt"
          required
        />
        <label for="passwordConfTxt">Confirmar Contraseña:</label>
      </div>
      `,
        preConfirm: obtenerValoresUsuario,
        confirmButtonColor: "#012970",
      });
      if (result3) {
        console.log(JSON.stringify(result3));
        const data = {
          ci_persona: result1[0],
          nombres: result1[1],
          apellidos: result1[2],
          fecha_nacimiento: result1[3],
          direccion: result1[4],
          genero: result1[5],
          estado_civil: result1[6],
          nameuser: result3[0],
          email: result3[1],
          password: result3[2],
          especialidad: result2[0],
          hospital_id: result2[1],
        };

        guardarMedicoAxios(data)
          .then((response) => {
            console.log(response.data);
            msg = response.data.message;
            if (response.status === 200) {
              notificacionSwal(msg, "success");
              location.href = "/medico";
            } else {
              notificacionSwal(msg, "error");
            }
          })
          .catch((error) => {
            console.log("Error al obtener y llenar los datos:", error);
          });
      } else {
        Swal.fire("algo salio mal..", "Datos incorrectos!", "warning");
      }
    }
  }
}

async function get_all_hospitals() {
  try {
    const url = `${window.origin}/api/hospital`;
    const response = await axios.get(url);
    if (response.status === 200) return response.data;
    else throw `Error al cargar datos de hospital...`;
  } catch (error) {
    console.log(error);
  }
}

function obtenerValoresMedico() {
  const hospital = document.getElementById("hospitalTxt").value;
  const especialidad = document.getElementById("especialidadtxt").value;
  if (hospital === "" || especialidad === "") {
    Swal.showValidationMessage("Por favor, completa todos los campos");
  } else {
    return [especialidad, hospital];
  }
}

async function guardarMedicoAxios(datos) {
  try {
    const url = `${window.origin}/api/medico/add`;
    const response = await axios.post(url, datos);
    return response;
  } catch (error) {
    console.log(error.response);
  }
}

function handleSubmit() {
  const ci = document.getElementById("ciTxt").value;
  const nombre = document.getElementById("nombreTxt").value;
  const apellido = document.getElementById("apellidoTxt").value;
  const fecha = document.getElementById("fechaTxt").value;
  const direccion = document.getElementById("direccionTxt").value;
  const genero = document.getElementById("generoTxt").value;
  const estado = document.getElementById("estadocTxt").value;

  const especialidad = document.getElementById("especialidadTxt").value;
  const hospital = document.getElementById("hospitalTxt").value;

  const name_user = document.getElementById("nameuserTxt").value;
  const password_user = document.getElementById("passwordTxt").value;
  const email_user = document.getElementById("emailTxt").value;

  const data = {
    ci_persona: ci,
    nombres: nombre,
    apellidos: apellido,
    fecha_nacimiento: fecha,
    direccion: direccion,
    genero: genero,
    estado_civil: estado,
    nameuser: name_user,
    password: password_user,
    email: email_user,
    especialidad: especialidad,
    hospital_id: hospital,
  };

  console.log(data);

  fetch(`${window.origin}/api/medico/add`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => {
      if (!response.ok) throw Error("Error en fetch ", response.statusText);
      return response.json();
    })
    .then((result) => {
      myModal.hide();
      Swal.fire("Medico Agreado");
    })
    .catch((error) => {
      Swal.fire("ah ocurrido un error", error);
    });
}

function viewRow(button) {
  const row = button.parentNode.parentNode;
  const cells = row.getElementsByTagName("td");
  const id_medico = cells[1].innerText;
  viewMedico(id_medico)
    .then((result) => {
      console.log(result.medico.apellidos);

      Swal.fire({
        title: "<strong>Informacion Medico</strong>",
        imageUrl: `${result.medico.foto_url}`,
        imageWidth: 100,
        imageHeight: 100,
        html: `<div class="row">
            <div class="col"><p><b class='fw-semibold'>ID: </b>${result.medico.id_medico}</p></div>
            <div class="col"><p><b clcass='fw-semibold'>CI: </b>${result.medico.ci_persona}</p></div>
          </div>
          <div class="row">
          <div class="col"><p><b class='fw-semibold'>Nombres: </b>${result.medico.nombres}</p></div>
            <div class="col"><p><b class='fw-semibold'>Apellidos: </b>${result.medico.apellidos}</p></div>
          </div>
          <div class="row">
            <div class="col"><p><b class='fw-semibold'>Especialidad: </b>${result.medico.especialidad}</p></div>
            <div class="col"><p><b class='fw-semibold'>Hospital: </b>${result.medico.hospital_name}</p></div>
          </div>`,
        confirmButtonColor: "#012970",
        confirmButtonText: "Aceptar",
        customClass: {
          title: "my-swal-title",
          htmlContainer: "my-swal-container",
          content: "my-swal-modal",
        },
      });
    })
    .catch((error) => {
      console.log(error);
    });
}

async function viewMedico(id_medico) {
  if (typeof id_medico !== "string" || id_medico.trim() === "") {
    console.log("El parámetro 'id_medico' es inválido o está vacío");
    return;
  }
  try {
    const url = `${window.origin}/api/medico/view/${id_medico}`;
    console.log(url);
    const response = await axios.get(url);
    console.log(response);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}
