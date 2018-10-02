import React, { Component } from "react";
import Ninjas from "./Ninjas";
import AddNinja from "./AddNinja";

class App extends Component {
  state = {
    ninjas: [
      { name: "Ryu", age: 30, belt: "black", id: 1 },
      { name: "Yoshi", age: 20, belt: "green", id: 2 },
      { name: "Crystal", age: 25, belt: "pink", id: 3 }
    ]
  };

  // Passed down this function as a prop for dynamic reloading
  addNinja = ninja => {
    // What happens if you add and remove ninjas though?
    ninja.id = Date.now();
    // Can not do this due to it reforming the data structure instead of making a new one
    // ninjas: this.state.ninjas.push(ninja);
    // Creates a new array with the previous ninjas adding the new ninja
    let ninjas = [...this.state.ninjas, ninja];
    this.setState({
      ninjas: ninjas
    });
  };

  render() {
    return (
      <div className="App">
        <h1>Not my first React app!</h1>
        <p>Welcome :)</p>
        <Ninjas ninjas={this.state.ninjas} />
        <AddNinja addNinja={this.addNinja} />
      </div>
    );
  }
}

export default App;
