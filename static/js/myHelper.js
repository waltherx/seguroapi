function calcularEdadExacta(fechaNacimiento) {
  const partesFecha = fechaNacimiento.split("-");
  const diaNacimiento = parseInt(partesFecha[0]);
  const mesNacimiento = parseInt(partesFecha[1]) - 1; // Restamos 1 para obtener el mes correcto (0-11)
  const anioNacimiento = parseInt(partesFecha[2]);

  const fechaNac = new Date(anioNacimiento, mesNacimiento, diaNacimiento);
  const hoy = new Date();

  const diffTiempo = hoy.getTime() - fechaNac.getTime();

  const msPorDia = 1000 * 60 * 60 * 24;
  const diffDias = Math.floor(diffTiempo / msPorDia);

  const anios = hoy.getFullYear() - fechaNac.getFullYear();
  const meses = hoy.getMonth() - fechaNac.getMonth();
  const dias = hoy.getDate() - fechaNac.getDate();

  let edadAnios = anios;
  let edadMeses = meses;
  let edadDias = dias;

  if (meses < 0 || (meses === 0 && dias < 0)) {
    edadAnios--;
    edadMeses += 12;
  }

  if (dias < 0) {
    const ultimoDiaMesAnterior = new Date(
      hoy.getFullYear(),
      hoy.getMonth(),
      0
    ).getDate();
    edadMeses--;
    edadDias += ultimoDiaMesAnterior;
  }

  return {
    anios: edadAnios,
    meses: edadMeses,
    dias: edadDias,
    totalDias: diffDias,
  };
}

function genero_persona(genero) {
  const state = genero.toLowerCase();
  if (state === "h") {
    return "Hombre";
  } else if (state === "m") {
    return "Mujer";
  } else if (state === "nb") {
    return "No binario";
  } else if (state === "gf") {
    return "Género fluido";
  } else if (state === "tr") {
    return "Transgénero";
  } else if (state === "ci") {
    return "Cisgénero";
  } else if (state === "ag") {
    return "Agénero";
  } else if (state === "bi") {
    return "Bigénero";
  } else if (state === "pa") {
    return "Pangénero";
  }
  return "Otro/No especificado";
}

function estado_civil_persona(estado) {
  const state = estado.toLowerCase();
  if (state === "c") {
    return "Casado/a";
  } else if (state === "s") {
    return "Soltero/a";
  } else if (state === "d") {
    return "Divorciado/a";
  } else if (state === "v") {
    return "Viudo/a";
  } else if (state === "p") {
    return "Conviviendo en pareja";
  }
  return "Otro/No especificado";
}
