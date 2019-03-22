const mongoose = require("mongoose");
const Schema = mongoose.Schema;

// Create Schema and Model

const MarioCharSchema = new Schema({
  name: String,
  weight: Number,
});

// Everytime a new MarioChar is made, use the model 'mariochar' based on the MarioCharSchema

const MarioChar = mongoose.model("mariochar", MarioCharSchema);

module.exports = MarioChar;

var myChar = new MarioChar({});
