async function get_persona_2(ci_persona) {
  try {
    const url_get = `${window.origin}/api/person/view/${ci_persona}`;
    const response = await axios.get(url_get);
    return response;
  } catch (error) {
    console.log(error);
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
