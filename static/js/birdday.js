function calcularEdadExacta(fechaNacimiento) {
    const partesFecha = fechaNacimiento.split('-');
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
      const ultimoDiaMesAnterior = new Date(hoy.getFullYear(), hoy.getMonth(), 0).getDate();
      edadMeses--;
      edadDias += ultimoDiaMesAnterior;
    }
  
    return {
      anios: edadAnios,
      meses: edadMeses,
      dias: edadDias,
      totalDias: diffDias
    };
  }
  