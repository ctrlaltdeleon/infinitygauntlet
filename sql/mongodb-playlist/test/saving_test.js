// const mocha = require('mocha');
const assert = require("assert");
const MarioChar = require("../models/mariochar");

// describe tests
describe("saving records", function() {
  // create tests
  it("saves a record to the database", function() {
    var char = new MarioChar({
      name: "Bowser",
    });
    // asynchronous request
    char.save().then(function() {
      assert(char.isNew);
    });
  });
});
