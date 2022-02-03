var chart    = document.getElementById('chart').getContext('2d'),
    gradient = chart.createLinearGradient(0, 0, 0, 450);

gradient.addColorStop(0, 'rgba(0, 199, 214, 0.32)');
gradient.addColorStop(0.3, 'rgba(0, 199, 214, 0.1)');
gradient.addColorStop(1, 'rgba(0, 199, 214, 0)');


var data  = {
    labels: [ '11', '12', '13', '14', '15', '16', '17','18','19','20', '21','22' ],
    datasets: [{
			label: 'Applications',
			backgroundColor: gradient,
			pointBackgroundColor: '#00c7d6',
			borderWidth: 1,
			borderColor: '#0e1a2f',
			data: [60, 45, 80, 30, 35, 55,25,80,40,50,80,50]
    }]
};


var options = {
	responsive: true,
	maintainAspectRatio: true,
	animation: {
		easing: 'easeInOutQuad',
		duration: 520
	},
	scales: {
		yAxes: [{
      ticks: {
        fontColor: '#5e6a81'
      },
			gridLines: {
				color: 'rgba(200, 200, 200, 0.08)',
				lineWidth: 1
			}
		}],
    xAxes:[{
      ticks: {
        fontColor: '#5e6a81'
      }
    }]
	},
	elements: {
		line: {
			tension: 0.4
		}
	},
	legend: {
		display: false
	},
	point: {
		backgroundColor: '#00c7d6'
	},
	tooltips: {
		titleFontFamily: 'Poppins',
		backgroundColor: 'rgba(0,0,0,0.4)',
		titleFontColor: 'white',
		caretSize: 5,
		cornerRadius: 2,
		xPadding: 10,
		yPadding: 10
	}
};

setInterval(() => {
		setInterval(() => {
		data["labels"].push(Math.floor(Math.random()*203));
		data["datasets"][0]["data"].push(Math.floor(Math.random()*100))
		
	}, 500);
	var chartInstance = new Chart(chart, {
		type: 'line',
		data: data,
			options: options
	});

	
},2500);

document.querySelector(".offer-button").addEventListener("click",function(){
	var randomvv=Math.random()*100
	// percentage
	var todaycount = new Date();
    var timecount = todaycount.getHours() + ":" + todaycount.getMinutes() ;
               
             
	document.querySelector(".percentageFuel").textContent = Math.floor(randomvv) + "%"
	document.querySelector(".circleFuel").attributes[1].nodeValue=randomvv + ", 100"

	if(timecount< 12){
		document.querySelector(".subtitle-count1").textContent=timecount + " am"
	}else{
		document.querySelector(".subtitle-count1").textContent=timecount + " pm"
	}
	
})

document.querySelector('.open-right-area').addEventListener('click', function () {
    document.querySelector('.app-right').classList.add('show');
});

document.querySelector('.close-right').addEventListener('click', function () {
    document.querySelector('.app-right').classList.remove('show');
});

document.querySelector('.menu-button').addEventListener('click', function () {
    document.querySelector('.app-left').classList.add('show');
});

document.querySelector('.close-menu').addEventListener('click', function () {
    document.querySelector('.app-left').classList.remove('show');
});