import React, { Component } from "react";

class Ninjas extends Component {
  render() {
    console.log(this.props);

    const { ninjas } = this.props;

    // Output a specific list, useful if there's a bunch of ninjas and need to add more props
    const ninjaList = ninjas.map(ninja => {
      return (
        <div className="ninja" key={ninja.id}>
          <div>Name: {ninja.name}</div>
          <div>Age: {ninja.age}</div>
          <div>Belt: {ninja.belt}</div>
          <div>You are beautiful</div>
          <br />
        </div>
      );
    });

    return <div className="ninja-list">{ninjaList}</div>;
  }
}

export default Ninjas;
