//do stuff

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