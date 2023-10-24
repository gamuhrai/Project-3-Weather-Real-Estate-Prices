function fetchData() {
    fetch('http://127.0.0.1:5000/')
        .then(response => response.json())
        .then(data => {
            document.getElementById('data-container').innerText = JSON.stringify(data, null, 2);
        })
        .catch(error => console.error('Error fetching data:', error));
}
// in your .js file

Plotly.newPlot('graph-container', [{
    x: [/* x data */],
    y: [/* y data */],
    type: 'scatter'
  }]);

  async function fetchtempData(city) {
    try {
      const response = await fetch(`/api/data/temp/${city}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Failed to fetch data:', error);
    }
  }
  
  const city = "boston"; // Replace with the actual city name you want to query
  fetchData(city).then(data => {
    if (data) {
      console.log('Dates:', data.dates);
      console.log('Temperature:', data.temperature);
    }
  });

  async function fetchData(city) {
    try {
      const response = await fetch(`/api/data/home/${city}`);
      if (!response.ok) {
        throw new Error(`HTTP error! Status: ${response.status}`);
      }
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Failed to fetch data:', error);
    }
  }
  
  const city = "boston"; // Replace with the actual city name you want to query
  fetchData(city).then(data => {
    if (data) {
      console.log('Dates:', data.dates);
      console.log('Home Values:', data.home_values);
    }
  });
  

//   const city = "boston"; // Replace with the actual city name you want to query

// const myArray = [1, 2, 3, 4, 5];
// javascript

// fetch('/api/data') .then(response => response.json()) .then(data => { const x_values = data.data.map(row => row[0]); 

// document.addEventListener('DOMContentLoaded', (event) => {
//     fetchData('New York'); // Replace 'New York' with the desired city
// });

// function fetchTemperatureData(city) {
//     const url = `http://127.0.0.1:5000/api/data/temp/${city}`;

//     fetch(url)
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok ' + response.statusText);
//             }
//             return response.json();
//         })
//         .then(data => {
//             console.log('Fetched temperature data:', data);

//             const yValues = data.temperatures;
//             const xValues = data.dates;

//             const trace = {
//                 x: xValues,
//                 y: yValues,
//                 type: 'line',
//                 name: 'Temperature'
//             };

//             const layout = {
//                 title: `Temperature in ${city}`
//             };

//             Plotly.newPlot('graph-container-temp', [trace], layout);
//         })
//         .catch(error => console.error('Error fetching temperature data:', error));
// }

// function fetchHomeData(city) {
//     const url = `http://127.0.0.1:5000/api/data/home/${city}`;

//     fetch(url)
//         .then(response => {
//             if (!response.ok) {
//                 throw new Error('Network response was not ok ' + response.statusText);
//             }
//             return response.json();
//         })
//         .then(data => {
//             console.log('Fetched home data:', data);

//             const yValues = data.home_values;
//             const xValues = data.dates;

//             const trace = {
//                 x: xValues,
//                 y: yValues,
//                 type: 'line',
//                 name: 'Home Value'
//             };

//             const layout = {
//                 title: `Home Value in ${city}`
//             };

//             Plotly.newPlot('graph-container-home', [trace], layout);
//         })
//         .catch(error => console.error('Error fetching home data:', error));
// }
