const mongoose = require("mongoose");

// es6 promises to be used for the promise library
mongoose.Promise = global.Promise;

// connect to the database before npm run test
before(function(done) {
  // connect to mongodb
  mongoose.connect("mongodb://localhost/testaroo", { useNewUrlParser: true });

  // to use:
  // node connection.js
  mongoose.connection
    .once("open", function() {
      console.log("Connection to database successful.");
      done();
    })
    .on("error", function(error) {
      console.log("Connection error!", error);
    });
});
