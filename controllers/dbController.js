//do stuff
function calcRoute() {
    var start = document.getElementById('start').value;
    var end = document.getElementById('end').value;
    var request = {
      origin: start,
      destination: end,
      travelMode: 'DRIVING'
    };
    directionsService.route(request, function(result, status) {
      if (status == 'OK') {
        directionsDisplay.setDirections(result);
      }
    });
  }
  
//routing
module.exports = function(serve){


//serve index page
serve.get("/", function(req, res){
    res.render("index2");
});

serve.get("/other", function(req, res){
    res.render("index2");
});

  
};