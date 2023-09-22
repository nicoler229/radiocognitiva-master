// Obtener el elemento canvas donde se dibujará el gráfico
const chartCanvas = document.getElementById('myAreaChart').getContext('2d');

// Datos de ejemplo (eje X: meses, eje Y: valores)
const datos = {
  labels: ['100', '200', '300', '400', '500', '600'],
  datasets: [{
    label: 'Tx VS Rx',
    data: [10, 20, 15, 25, 30, 18],
    fill: false,
    borderColor: 'rgba(75, 192, 192, 1)',
    tension: 0.4
  }]
};

// Opciones de configuración del gráfico
const opciones = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true
    }
  }
};

// Crear el gráfico de línea
const chart = new Chart(chartCanvas, {
  type: 'line',
  data: datos,
  options: opciones
});
