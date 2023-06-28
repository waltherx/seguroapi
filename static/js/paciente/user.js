"use strict";

const url = `${window.origin}/api/user/`;

console.log(url);

async function get_users() {
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

new gridjs.Grid({
  columns: ["CI", "id_user", "Nombre usuario", "nombre_completo", "rol"],
  pagination: true,
  server: {
    url: url,
    then: (data) =>
      data.map((user) => [
        user.ci_persona,
        user.id_user,
        user.name_user,
        user.nombre_completo,
        user.rol,
      ]),
  },
  resizable: true,
  sort: true,
  /*name: "Actions",
      formatter: (cell, row) => {
        return h(
          "button",
          {
            className:
              "py-2 mb-4 px-4 border rounded-md text-white bg-blue-600",
            onClick: () =>
              alert(`Editing "${row.cells[0].data}" "${row.cells[1].data}"`),
          },
          "Edit"
        );
      },*/
  language: {
    pagination: {
      previous: "Anterior",
      next: "Siguiente",
      /*navigate: (page, pages) => `Page ${page} of ${pages}`,
        page: (page) => `Page ${page}`,*/
      showing: "Mostrar",
      of: "de",
      to: "a",
      results: "resultados",
    },
    loading: "Cargando...",
  },
  style: {
    table: {
      border: "3px solid #ccc",
    },
    th: {
      "background-color": "rgba(0, 0, 0, 0.1)",
      color: "#000",
      "border-bottom": "3px solid #ccc",
      "text-align": "center",
    },
    td: {
      "text-align": "center",
    },
  },
}).render(document.getElementById("table"));
