fetch('https://jsonplaceholder.typicode.com/users')
  .then(response => response.json())
  .then(data => {
    const table = document.querySelector('#myTable tbody');
    data.forEach(user => {
      const newRow = table.insertRow();
      newRow.insertCell().innerHTML = user.id;
      newRow.insertCell().innerHTML = user.name;
      newRow.insertCell().innerHTML = user.email;
    });
  });
