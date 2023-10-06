async function generateQr(button) {
  console.log("desdeqr");
  const row = button.parentNode.parentNode;
  const cells = row.getElementsByTagName("td");
  const ci_paciente = cells[0].innerText;
  gen(ci_paciente)
    .then((result) => {
      const paciente = result.Paciente;
      const data = {
        ci_persona: paciente.ci,
        nombre_completo: `${paciente.nombres} ${paciente.apellidos}`,
        foto_url: paciente.foto_url,
        fecha_nacimiento: paciente.fecha_nacimiento,
      };
      console.log(JSON.stringify(data));      
      mostrarQR(JSON.stringify(data));
    })
    .catch((error) => {
      console.log(error);
    });
}

async function gen(ci_paciente) {
  try {
    const url = `${window.origin}/api/paciente/${ci_paciente}`;
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.log(error);
  }
}

function mostrarQR(texto) {
  const qr = new QRious({
    value: texto,
    size: 200,
    //foreground: "#012970",
  });

  const imagenQR = qr.toDataURL();

  Swal.fire({
    title: "Código QR de Paciente",
    imageUrl: imagenQR,
    imageWidth: 250,
    imageHeight: 250,
    imageAlt: "Código QR",
    confirmButtonText: 'Descargar',
    confirmButtonColor: "#012970",
    showCancelButton: true,
    cancelButtonText: 'Cerrar',
    showCloseButton: true,
    preConfirm: () => {
        let linkQr = document.createElement('a');
        linkQr.href = imagenQR;
        linkQr.download = 'Codigo_Qr_paciente.png';
        linkQr.click();
      }
  });
}
