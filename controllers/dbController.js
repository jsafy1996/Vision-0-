//do stuff

//routing
module.exports = function(serve){

//serve index page
serve.get("/", function(req, res){
    res.render("index");
});

serve.get("/other", function(req, res){
    res.render("index");
});

  
};