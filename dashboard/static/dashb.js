
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
      count = entries.length
      if(count > 10){count = 10}
      for (let i = 0; i < count; i++) {
      subsArray.push(entries[i][0]);
      countsArray.push(entries[i][1]);
      }
      const dataPie = {
      labels: subsArray,
      datasets: [{
      label: 'My First Dataset',
      data: countsArray,
      backgroundColor: [
        'rgb(197,184,252)',
        'rgb(98,92,126)',
        'rgb(243,240,254)'
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
          display: false,
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
// this is some jquery. It only loads after the elements on the page loads I think. 
$(document).ready(function()
{
	$("#wordCloud").jQWCloud({
		words: data,
		//cloud_color: 'yellow',		
		minFont: 10,
		maxFont: 50,
		//fontOffset: 5,
		//cloud_font_family: 'Owned',
		verticalEnabled: true,
		padding_left: 1,
		//showSpaceDIV: true,
		//spaceDIVColor: 'white',
		word_common_classes: 'WordClass',		
		word_mouseEnter :function(){
			$(this).css("text-decoration","underline");
		},
		word_mouseOut :function(){
			$(this).css("text-decoration","none");	
		},
		word_click: function(){ 			
			alert("You have selected:" +$(this).text());
		},		              
		beforeCloudRender: function(){
		       date1=new Date();
	 	},
	 	afterCloudRender: function(){
				var date2=new Date();
				console.log("Cloud Completed in "+(date2.getTime()-date1.getTime()) +" milliseconds");
			}
	});
	
});