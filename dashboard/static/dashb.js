
function setupTopSubs(dict){
    dict = {
        'Sunday': dict.Sunday,
        'Monday': dict.Monday,
        'Tuesday': dict.Tuesday,
        'Wednesday': dict.Wednesday,
        'Thursday': dict.Thursday,
        'Friday': dict.Friday,
        'Saturday': dict.Saturday

    }
    const labels = Object.keys(dict)
    const data = {
    labels: labels,
    datasets: [{
      label: 'What days do I post the most?',
      backgroundColor: 'rgb(255, 99, 132)',
      borderColor: 'rgb(255, 99, 132)',
      data: Object.values(dict),
    }]
  };
  const config = {
    type: 'bar',
    data: data,
    options: {
      plugins: {
          // title: {
          //   display: true,
          //   text: 'Something'
          // }
      }
    }
  };
  const myChart = new Chart(
    document.getElementById('myChart'),
    config
  );
    
}
   //Pie chart config 
function setupSubPieChart(topSubs){
    const entries = Object.entries(topSubs)
    entries.sort(function(a, b){
        if(a[1] < b[1]) { return 1; }
        if(a[1] > b[1]) { return -1; }
        return 0;
      })
      subsArray = []
      countsArray = []
      for (let i = 0; i < 10; i++) {
      subsArray.push(entries[i][0]);
      countsArray.push(entries[i][1]);
      }
      const dataPie = {
      labels: subsArray,
      datasets: [{
      label: 'My First Dataset',
      data: countsArray,
      backgroundColor: [
      'rgb(255, 99, 132)',
      'rgb(54, 162, 235)',
      'rgb(255, 205, 86)'
      ],
      hoverOffset: 4
      }]
    };

      const configPie = {
      type: 'pie',
      data: dataPie,
      options: {
      plugins:{
        title: {
          display: true,
          text: 'Hover to see Subreddits'
        },
        legend:{
          display: false
            }
        }
      }
    };

    const pieChart1 = new Chart(
    document.getElementById('pieChart1'),
    configPie
    );
}
