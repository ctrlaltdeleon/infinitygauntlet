const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// create Schema and Model

const MarioCharSchema = new Schema({
  name: String,
  weight: Number,
});

// every time a new MarioChar is made, use the model 'mariochar' based on the MarioCharSchema

const MarioChar = mongoose.model("mariochar", MarioCharSchema);

module.exports = MarioChar;

var myChar = new MarioChar({});
