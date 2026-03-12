function sendData(){

navigator.geolocation.getCurrentPosition(function(position){

fetch("http://127.0.0.1:5000/predict", {

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

description:document.getElementById("desc").value,
lat:position.coords.latitude,
lon:position.coords.longitude

})

})

.then(res=>res.json())
.then(data=>{

document.getElementById("result").innerHTML =

"Emergency Type: "+data.emergency_type+"<br>"+
"Nearest Service: "+data.nearest_service+"<br>"+
"Contact: "+data.contact

})

})

}
