import React from "react";

// Functional component with props being straight referenced
const Ninjas = ({ ninjas }) => {
  console.log(ninjas);

  // const { ninjas } = props;

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
};

export default Ninjas;
