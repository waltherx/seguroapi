async function modalDocumento(ci_person, id_paciente) {
  const { value: formValues } = await Swal.fire({
    title: "Agregar Documento",
    html: `<div class="form-floating">      
          <input id="tipoTxt" type="text" class="form-control">
          <label for="tipoTxt" class="form-label">Tipo:</label>
        </div>
        <div class="form-floating">
          <input id="docTxt" type="file" class="form-control">
          <label for="docTxt" class="form-label">Documento:</label>
        </div>`,
    focusConfirm: false,
    preConfirm: obtenerValoresDoc,
    confirmButtonText: "Aceptar",
    confirmButtonColor: "#012970",
  });

  if (formValues) {
    const data = {
      id: id_paciente,
      tipo: formValues[0],
      photo: formValues[1],
    };
    try {
      const url = `${window.origin}/api/doc/add?tipo=${data.tipo}&id=${data.id}`;
      console.log(url);
      const formData = new FormData();
      formData.append("photo", data.photo);
      console.log(formData);

      const response = await axios.post(url, formData);
      console.log(response.data.message);
      Swal.fire("Correcto!", response.data.message, "success");
      //mostarDocs(ci_person);
    } catch (error) {
      Swal.fire(JSON.stringify(error, response.data.message, "error"));
    }
  }
}

async function obtenerDocumentos(ci_persona) {
  try {
    const url = `${window.origin}/api/doc/${ci_persona}`;
    const response = await axios.get(url);
    return response.data.Documentos;
  } catch (error) {
    console.log(error);
  }
}

function llenarTablaDoc(datos) {
  const tablaBody = document.getElementById("tdocumento");
  tablaBody.innerHTML = "";
  datos.forEach((doc) => {
    const tr = document.createElement("tr");
    const td1 = document.createElement("td");
    const td2 = document.createElement("td");
    td1.textContent = doc.tipo;

     // Crear un elemento de enlace <a>
     const link = document.createElement("a");
     link.href = "#"; // Puedes establecer aquí el enlace real+

    const img = document.createElement("img");
    img.src = doc.url;
    img.alt = "Documento de paciente";
    img.height = 100;
    img.width = 100;
    img.classList.add("rounded-circle");


    link.appendChild(img);

    link.addEventListener("click", function(event) {
      event.preventDefault(); // Evitar el comportamiento predeterminado del enlace
      // Llamar a la función deseada al hacer clic en la imagen
      verImg(doc.tipo, doc.url);
    });


    /*img.addEventListener("click", function() {
      verImg(doc.tipo, doc.url);
    });*/
    td2.appendChild(link);
    //td2.appendChild(img);
    tr.appendChild(td1);
    tr.appendChild(td2);
    tablaBody.appendChild(tr);
  });
}

function verImg(tipo_doc, url_doc) {
  console.log("Haz hecho clic en la imagen del documento:", url_doc);
  Swal.fire({
    title: tipo_doc,
    imageUrl: url_doc,
    imageAlt: 'Documento Paciente',
    showCloseButton: true
  })
}

function obtenerValoresDoc() {
  const input1 = document.getElementById("tipoTxt").value;
  const input2 = document.getElementById("docTxt").files[0];

  console.log(input2);

  if (input1.trim() === "") {
    Swal.showValidationMessage(
      `Request failed: Por favor ingresa un Tipo de Documento.`
    );
  } else if (!input2) {
    Swal.showValidationMessage(
      `Request failed: Por favor selecciona un archivo.`
    );
  } else {
    console.log("Ambos campos tienen valores válidos documento.");
    return [input1, input2];
  }
}

async function mostarDocs(ci_person) {}
