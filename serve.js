var express = require("express");
//var controller1 = require("");

var serve = express();

//set up ejs as template engine
//app.set("view engine", "ejs");

//serve static files (css styles)
serve.use(express.static("./assets"));

//fire controllers
controller1(serve);

//listen to port
app.listen(3000);

module.exports = serve;