const mongoose = require("mongoose");

// connect to mongodb
mongoose.connect("mongodb://localhost/testaroo");

// to use:
// node connection.js
mongoose.connection
  .once("open", function() {
    console.log("Connection to database successful.");
  })
  .on("error", function(error) {
    console.log("Connection error!", error);
  });
