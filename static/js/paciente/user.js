"use strict";

const url = `${window.origin}/api/user/`;






async function get_users() {
  try {
    const response = await axios.get(url);
    return response.data;
  } catch (error) {
    console.error(error);
  }
}

new gridjs.Grid({
  columns: [
    { name: "id_user" },
    { name: "Nombre usuario" },
    { name: "nombre_completo" },
    {
      name: "Actions",
      formatter: (cell, row) => {
        return gridjs.h(
          "button",
          {
            className: "btn btn-success",
            onClick: () =>
              alert(`Editing "${row.cells[0].data}" "${row.cells[1].data}"`),
          },
          "Edit"
        );
      },
    },
  ],
  search: true,
  pagination: true,
  server: {
    url: url,
    then: (data) =>
      data.map((user) => [
        user.id_user,
        user.name_user,
        user.nombre_completo,
        null,
      ]),
  },
  resizable: true,
  sort: true,
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
    search: "Buscar",
  },
  style: {
    table: {
      border: "3px solid #ccc",
      overflow: "hidden",
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
