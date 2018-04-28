var express = require("express");
var dbController = require("./controllers/dbController");

var serve = express();

//set up ejs as template engine
serve.set("view engine", "ejs");

//serve static files (css styles)
//serve.use(express.static("./assets"));

//fire controllers
dbController(serve);

//listen to port
serve.listen(3000);

module.exports = serve;