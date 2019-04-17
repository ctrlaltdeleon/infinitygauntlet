import React, { Component } from "react";

export default class Button extends Component {
  state = { counter: 0 };

  increment = () => {
    this.setState(state => ({ counter: state.counter + 1 }));
    console.log("increment()");
  };

  decrement = () => {
    this.setState(state => ({ counter: state.counter - 1 }));
    console.log("decrement()");
  };

  handleClick = () => {
    this.setState(state => ({ counter: 3.14159265359 }));
    console.log("handleClick()");
  };

  reset = () => {
    this.setState(state => ({ counter: 0 }));
    console.log("reset()");
  };

  render() {
    return (
      <div>
        <h1>hi</h1>
        <h1>{this.state.counter}</h1>
        <button onClick={this.increment}>Incrementor!</button>
        <button onClick={this.decrement}>Decrementor!</button>
        <button onClick={this.handleClick}>Pi!</button>
        <button onClick={this.reset}>Reset!</button>
      </div>
    );
  }
}
