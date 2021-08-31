var myMap = L.map('mapid').setView([35.78, -78.6382], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

d3.json('/fetch').then(data=>{
	console.log(data);
	for (var i=0; i<data.length; i++){
		ufo=data[i];
		L.marker([ufo['lat'], ufo['lon']])
		 .addTo(myMap);
	};
	// need to use data for at least 4X charts
});