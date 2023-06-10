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
   