async function update_paciente(id_paciente) {
  const { value: formValues } = await Swal.fire({
    title: "Actualizar Informacion Personal",
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
            <input id="alturaTxt" type="number" class="form-control" />
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
            <input id="pesoTxt" type="number" class="form-control" />
            <label for="pesoTxt" class="form-label">Peso:</label>
          </div>
        </div>
      </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresPaciente,
    confirmButtonText: "Aceptar",
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
      const msg = response;
      Swal.fire("Correcto!", msg.data.message, "success");
      console.log(msg.statusText);
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
ñ;

function obtenerValoresPaciente() {
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
