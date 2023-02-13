const data = {
    name: 'John Doe',
    age: 30
  };
  
  fetch('http://localhost:5000/api/data', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(error => console.error(error))