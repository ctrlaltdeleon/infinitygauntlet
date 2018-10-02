import React, { Component } from "react";
import Ninjas from "./ninjas";
class App extends Component {
  render() {
    return (
      <div className="App">
        <h1>Not my first React app!</h1>
        <p>Welcome :)</p>
        <Ninjas name="NARUTO" age="900" />
        <Ninjas name="SASUKE" age="90" />
      </div>
    );
  }
}

export default App;
