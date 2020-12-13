// Set new default font family and font color to mimic Bootstrap's default styling
// Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
// Chart.defaults.global.defaultFontColor = '#292b2c';
// Bar Chart Example
function generaGraficoBar() {
  const ctx2 = document.getElementById("graficoBar");
  const myBarChart = new Chart(ctx2, {
    type: 'bar',
    data: {
      labels: nomi,
      datasets: [{
        label: "Media",
        backgroundColor: colori,
        borderColor: colori,
        data: medie,
      }],
    },
    options: {
      scales: {
        xAxes: [{
          gridLines: {
            display: false,
            zeroLineColor: 'rgba(255,255,255,1)',
            zeroLineWitdh: 2,
          },
          ticks: {
            steps: 10,
            stepValue: 1,
            fontColor: "rgba(255,255,255,1)", //Colore voti
          },
        }],
        yAxes: [{
          ticks: {
            min: 0,
            max: 10,
            steps: 10,
            stepValue: 1,
            fontColor: "rgba(255,255,255,1)", //Colore voti
          },
          gridLines: {
            display: true,
            zeroLineColor: 'rgba(255,255,255,1)',
            color: '#505050',
            zeroLineWidth: 2,
          },
        }],
      },
      legend: {
        display: false,
      },
    },
  });
}

generaGraficoBar();