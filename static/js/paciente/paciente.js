async function update_paciente(id_paciente) {
  const url_get = `${window.origin}/api/paciente/view/${id_paciente}`;
  const response = await axios.get(url_get);
  const pacient = response.data;
  const { value: formValues } = await Swal.fire({
    title: "Actualizar Informacion Paciente.",
    html: `<div class="row row-padding mx-auto w-70">
            <div class="col">
            <div class="form-floating">
            <select class="form-select"
                      id="sangreTxt"
                      required>
                      <option value="A+">A positivo (A+)</option>
                      <option value="O+">O positivo (O+)</option>
                      <option value="B+">B positivo (B+)</option>
                      <option value="A-">A negativo (A-)</option>
                      <option value="O-">O negativo (O-)</option>
                      <option value="AB+">AB positivo (AB+)</option>
                      <option value="B-">B negativo (B-)</option>
                      <option value="AB-">AB negativo (AB-)</option>
                      <option value="Rh+">Rh positivo (Rh+)</option>
                      <option value="Rh-">Rh negativo (Rh-)</option>
                    </select>
            <label for="sangreTxt" class="form-label">Tipo de Sangre:</label>
          </div>
        </div>
        <div class="col">
          <div class="form-floating">
            <input id="alturaTxt" type="number" value="${pacient.altura}" class="form-control" />
            <label for="alturaTxt" class="form-label">Altura:</label>
          </div>
        </div>
      </div>
      <div class="row row-padding mx-auto w-70">
        <div class="col">
          <div class="form-floating">
            <select id="hipertencionTxt" class="form-select" required>
              <option value="Si">Si</option>
              <option value="No" selected>No</option>
            </select>
            <label for="hipertencionTxt" class="form-label">Hipertencion:</label>
          </div>
        </div>
        <div class="col">
          <div class="form-floating">
            <input id="pesoTxt" type="number" value="${pacient.peso}" class="form-control" />
            <label for="pesoTxt" class="form-label">Peso:</label>
          </div>
        </div>
      </div>`,
    didOpen: () => {
      const input1 = document.getElementById("sangreTxt");
      const input2 = document.getElementById("hipertencionTxt");
      input1.value = pacient.tipo_sangre;
      input2.value = pacient.hipertencion;
    },
    focusConfirm: false,
    preConfirm: obtenerValoresPaciente_update, //ojo
    confirmButtonText: "Actualizar",
    confirmButtonColor: "#012970",
  });

  const url = `${window.origin}/api/paciente/v1/update`;
  if (formValues) {
    const data = {
      id: id_paciente,
      tiposangre: formValues[0],
      hipertencion: formValues[1],
      altura: formValues[2],
      peso: formValues[3],
    };
    console.log(data);
    try {
      const response = await axios.put(url, data);
      notificacionSwal(response.data.message, "success");
      mostrarPaciente(
        data.tiposangre,
        data.hipertencion,
        data.altura,
        data.peso
      );
    } catch (error) {
      console.log(error);
    }
  }
}

function obtenerValoresPaciente_update() {
  const input1 = document.getElementById("sangreTxt").value;
  const input2 = document.getElementById("hipertencionTxt").value;
  const input3 = document.getElementById("alturaTxt").value;
  const input4 = document.getElementById("pesoTxt").value;

  if (
    input1.trim() === "" ||
    input2.trim() === "" ||
    input3.trim() === "" ||
    input4.trim() === ""
  ) {
    Swal.showValidationMessage("Por favor, completa todos los campos.");
  } else {
    console.log("Ambos campos tienen valores válidos.");
    return [input1, input2, input3, input4];
  }
}

async function add_paciente_2() {
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
      title: "Datos Paciente",
      allowOutsideClick: true,
      currentProgressStep: 1,
      showCancelButton: true,
      html: `
      <div class="row">
        <div class="col">
          <div class="form-floating">
            <select
              class="form-select"
              id="txtSangre"
              name="txtSangre"
              onchange=""
              required
            >
              <option value="A+">A positivo (A+)</option>
              <option value="O+">O positivo (O+)</option>
              <option value="B+">B positivo (B+)</option>
              <option value="A-">A negativo (A-)</option>
              <option value="O-">O negativo (O-)</option>
              <option value="AB+">AB positivo (AB+)</option>
              <option value="B-">B negativo (B-)</option>
              <option value="AB-">AB negativo (AB-)</option>
              <option value="Rh+">Rh positivo (Rh+)</option>
              <option value="Rh-">Rh negativo (Rh-)</option>
            </select>
            <label for="txtSangre">Sangre</label>
          </div>
        </div>
        <div class="col">
          <div class="form-floating">
            
            <input
              type="number"
              step="any"
              class="form-control"
              id="txtAltura"
              name="txtAltura"
              required
            />
            <label for="txtAltura">Altura</label>
          </div>
      </div>
  </div>
      <div class="row">
        <div class="col">
          <div class="form-floating">
            <select
              id="txtHipertencion"
              name="txtHipertencion"
              class="form-select"
              required
            >
              <option>Si</option>
              <option selected>No</option>
            </select>
            <label for="txtHipertencion">Hipertencion</label>
          </div>
        </div>
        <div class="col">
          <div class="form-floating">
            <input
              type="number"
              step="any"
              class="form-control"
              id="txtPeso"
              name="txtPeso"
              required
            />
            <label for="txtPeso">Peso</label>
          </div>
        </div>
      </div>
    `,
      preConfirm: obtenerValoresPaciente,
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
          tipo_sangre: result2[0],
          hipertencion: result2[1],
          altura: result2[2],
          peso: result2[3],
        };

        guardarPacienteAxios(data)
          .then((response) => {
            console.log(response.data);
            msg = response.data.message;
            const Toast = Swal.mixin({
              toast: true,
              position: "bottom-end",
              showConfirmButton: false,
              timer: 2000,
              timerProgressBar: true,
              didOpen: (toast) => {
                toast.addEventListener("mouseenter", Swal.stopTimer);
                toast.addEventListener("mouseleave", Swal.resumeTimer);
              },
            });

            if (response.status === 200) {
              Toast.fire({
                icon: "success",
                title: msg,
              });
            } else {
              Toast.fire({
                icon: "error",
                title: msg,
              });
            }

            Toast.fire({
              icon: "success",
              title: response.data,
            });
            location.href = "/paciente";
            //Swal.fire("Datos Ingresados!", response.data, "success");
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

function validarNameUser(name) {
  const nombreRegex = /^[a-zA-Z]+$/;
  return nombreRegex.test(name);
}

function validarEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function obtenerValoresUsuario() {
  const name_user = document.getElementById("nameuserTxt").value;
  const email_user = document.getElementById("emailTxt").value;
  const password_user = document.getElementById("passwordTxt").value;
  const password_confir = document.getElementById("passwordConfTxt").value;

  if (
    name_user === "" ||
    email_user === "" ||
    password_user === "" ||
    password_confir === ""
  ) {
    Swal.showValidationMessage("Por favor, completa todos los campos");
  } else if (!validarNameUser(name_user)) {
    Swal.showValidationMessage(
      "El nombre de usuario no puede contener espacios ni caracteres especiales"
    );
  } else if (!validarEmail(email_user)) {
    Swal.showValidationMessage("El email ingresado no es válido");
  } else if (password_user !== password_confir) {
    Swal.showValidationMessage("Las contraseñas no coinciden");
  } else {
    return [name_user, email_user, password_user];
  }
}

function obtenerValoresPaciente() {
  const tipo_sangre = document.getElementById("txtSangre").value;
  const hipertencion = document.getElementById("txtHipertencion").value;
  const altura = document.getElementById("txtAltura").value;
  const peso = document.getElementById("txtPeso").value;

  const decimalRegex = /^\d+(\.\d+)?$/;
  if (
    tipo_sangre === "" ||
    hipertencion === "" ||
    altura === "" ||
    peso === ""
  ) {
    Swal.showValidationMessage(
      `Request failed: Por favor, completa todos los campos.`
    );
  } else if (!decimalRegex.test(altura) || !decimalRegex.test(peso)) {
    Swal.showValidationMessage(
      `Request failed: Por favor, ingrese solo numeros en peso o altura.`
    );
  } else {
    return [tipo_sangre, hipertencion, altura, peso];
  }
}

function obtenerValoresPersona() {
  const ci = document.getElementById("ciTxt").value;
  const nombre = document.getElementById("nombreTxt").value;
  const apellido = document.getElementById("apellidoTxt").value;
  const fecha = document.getElementById("fechaTxt").value;
  const direccion = document.getElementById("direccionTxt").value;
  const genero = document.getElementById("generoTxt").value;
  const estado = document.getElementById("estadocTxt").value;

  const numeroRegex = /^[0-9]+$/;
  const alfanumericoRegex = /^[\w\s]+$/;

  if (
    ci.trim() === "" ||
    nombre.trim() === "" ||
    apellido.trim() === "" ||
    direccion.trim() === ""
  ) {
    Swal.showValidationMessage(
      `Request failed: Por favor ingresa un valor en ambos campos.`
    );
  } else if (!numeroRegex.test(ci)) {
    Swal.showValidationMessage(
      `Request failed: El campo CI debe contener solo números.`
    );
  } else if (
    !alfanumericoRegex.test(nombre) &&
    !alfanumericoRegex.test(apellido)
  ) {
    Swal.showValidationMessage(
      `Request failed: El campo Nombres o Apellidos debe contener solo letras.`
    );
  } else {
    console.log("Ambos campos tienen valores válidos.");
    return [ci, nombre, apellido, fecha, direccion, genero, estado];
  }
}

async function guardarPacienteAxios(datos) {
  try {
    const url = `${window.origin}/api/paciente/add`;
    const response = await axios.post(url, datos);
    return response;
  } catch (error) {
    console.log(error.response);
  }
}

async function update_persona_paciente(ci_persona) {
  const url_get = `${window.origin}/api/person/view/${ci_persona}`;
  const response = await axios.get(url_get);
  console.log(JSON.stringify(response.data));
  const persona = response.data;
  const { value: formValues } = await Swal.fire({
    title: "Actualizar Informacion Personal.",
    html: `<div class="row">
          <div class="col">
            <div class="form-floating">
              <input
                type="number"
                class="form-control"
                id="ciTxt"
                value="${persona.ci}"
                disabled
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
                value="${persona.fecha_nacimiento}"
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
            value="${persona.nombres}"
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
            value="${persona.apellidos}"
            required
          />
          <label for="apellidoTxt">Apellidos:</label>
        </div>

        <div class="form-floating">
          
          <input
            type="text"
            class="form-control"
            id="direccionTxt"
            value="${persona.direccion}"
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
      const input1 = document.getElementById("generoTxt");
      const input2 = document.getElementById("estadocTxt");
      input1.value = persona.genero;
      input2.value = persona.estado_civil;
    },
    focusConfirm: false,
    preConfirm: obtenerValoresPersona,
    confirmButtonText: "Actualizar",
    confirmButtonColor: "#012970",
    customClass: {
      /*title: "my-swal-title",*/
      htmlContainer: "my-swal-container",
      content: "my-swal-modal",
    },
  });

  const url_put = `${window.origin}/api/person/update`;
  if (formValues) {
    console.log(formValues);
    const data = {
      ci: formValues[0],
      nombres: formValues[1],
      apellidos: formValues[2],
      fecha_nacimiento: formValues[3],
      direccion: formValues[4],
      genero: formValues[5],
      estado_civil: formValues[6],
    };
    try {
      const response = await axios.put(url_put, data);
      const result = response.data;
      notificacionSwal("Datos Actualizados Correctamente!", "success");
      mostrar_paciente_persona(result);
    } catch (error) {
      notificacionSwal(response.data.message, "error");
    }
  }
}

async function actualizar_Persona_Panciente(datos) {
  try {
    const url = `${window.origin}/api/person/update`;
    const response = await axios.put(url, datos);
    return response;
  } catch (error) {
    console.log(error.response);
  }
}

function mostrarPaciente(tiposangre, hiper, altura, peso) {
  let sangreLbl = document.getElementById("sangreLbl");
  let hiperLbl = document.getElementById("hiperLbl");
  let alturaLbl = document.getElementById("alturaLbl");
  let pesoLbl = document.getElementById("pesoLbl");
  sangreLbl.innerHTML = `<b>Tipo Sangre : </b>${tiposangre}`;
  hiperLbl.innerHTML = `<b>Hipertencion : </b>${hiper}`;
  alturaLbl.innerHTML = `<b>Altura : </b>${altura}`;
  pesoLbl.innerHTML = `<b>Peso : </b>${peso}`;
}

function mostrar_paciente_persona(persona) {
  try {
    const nombreLbl = document.getElementById("nombreLbl");
    const apellidoLbl = document.getElementById("apellidoLbl");
    const fechaLbl = document.getElementById("fechaLbl");
    const dirLbl = document.getElementById("dirLbl");
    const estadoLbl = document.getElementById("estadoLbl");
    const generoLbl = document.getElementById("generoLbl");
    const edadLbl = document.getElementById("edadLbl");

    const fecha = persona.fecha_nacimiento;
    nombreLbl.innerHTML = `<p><b>Nombre : </b>${persona.nombres}</p>`;
    apellidoLbl.innerHTML = `<p><b>Apellido : </b>${persona.apellidos}</p>`;
    fechaLbl.innerHTML = `<p><b>Fecha Nacimiento : </b>${fecha}</p>`;
    dirLbl.innerHTML = `<p><b>Direccion : </b>${persona.direccion}</p>`;
    estadoLbl.innerHTML = `<p><b>Estado Civil : </b>${estado_civil_persona(
      persona.estado_civil
    )}</p>`;
    generoLbl.innerHTML = `<p><b>Genero : </b>${genero_persona(
      persona.genero
    )}</p>`;
    const edad = calcularEdadExacta(fecha);
    edadLbl.innerHTML = `<p><b>Edad : </b>${edad.anios} Años ${edad.meses} Meses ${edad.dias} Dias.</p>`;
  } catch (error) {
    console.log(error);
  }
}
