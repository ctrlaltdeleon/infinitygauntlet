// const mocha = require('mocha');
const assert = require("assert");
const MarioChar = require("../models/mariochar");

// describe tests
describe("describe: saving records...", function() {
  // create tests
  it("saves a record to the database", function(done) {
    // note that this will keep creating unique ids every "npm run test"
    var char = new MarioChar({
      name: "Bowser",
    });
    // asynchronous request
    char.save().then(function() {
      assert(char.isNew === false);
      // reference function to the "it" parameter
      done();
    });
  });
});
