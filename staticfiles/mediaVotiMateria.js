// Set new default font family and font color to mimic Bootstrap's default styling
Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

function generaGraficoLinee() {
  try {
    const labels = [];
    const votiValidi=[];
    for(let i=0; i<voti[indice].length; i++)
      if(voti[indice][i][2]==1) {
        votiValidi.push(voti[indice][i][0]);
        labels.push(voti[indice][i][3]);
      }
    // Area Chart Example
    const ctx1 = document.getElementById("graficoLinee");
    const myLineChart = new Chart(ctx1, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [{
          label: ["Prova 1", "Prova 2", "Prova 3"],
          lineTension: 0.3,
          backgroundColor: "rgba(2,117,216,0.2)",
          borderColor: "rgba(2,117,216,1)",
          pointRadius: 5,
          pointBackgroundColor: "rgba(2,117,216,1)",
          pointBorderColor: "rgba(255,255,255,0.8)",
          pointHoverRadius: 5,
          pointHoverBackgroundColor: "rgba(2,117,216,1)",
          pointHitRadius: 50,
          pointBorderWidth: 2,
          data: votiValidi,
        }],
      },
      options: {
        scales: {
          xAxes: [{
            time: {
              unit: 'date',
            },
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
  } catch(e) {
    console.log(e);
  }
}

generaGraficoLinee();

function resetCanvasLinee() {
  $('#graficoLinee').remove(); // Tolgo la canvas
  $('#perGraficoLinee').append('<canvas id="graficoLinee"><canvas>'); //Creo di nuovo la canvas
}