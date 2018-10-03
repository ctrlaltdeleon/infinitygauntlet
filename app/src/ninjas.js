import React from "react";
import "./Ninjas.css";

// Functional component with props being straight referenced
const Ninjas = ({ ninjas, deleteNinja }) => {
  console.log(ninjas);

  // const { ninjas } = props;

  // IF STATEMENT

  // Output a specific list, useful if there's a bunch of ninjas and need to add more props
  // const ninjaList = ninjas.map(ninja => {
  //   if (ninja.age > 20) {
  //     return (
  //       <div className="ninja" key={ninja.id}>
  //         <div>Name: {ninja.name}</div>
  //         <div>Age: {ninja.age}</div>
  //         <div>Belt: {ninja.belt}</div>
  //         <div>You are beautiful</div>
  //         <br />
  //       </div>
  //     );
  //   } else {
  //     return null;
  //   }
  // });

  // CONDITIONAL STATEMENT

  const ninjaList = ninjas.map(ninja => {
    return ninja.age > 20 ? (
      <div className="ninja" key={ninja.id}>
        <div>Name: {ninja.name}</div>
        <div>Age: {ninja.age}</div>
        <div>Belt: {ninja.belt}</div>
        {/* This is called an anonymous function in order to invoke props but not exe */}
        <button onClick={() => deleteNinja(ninja.id)}>Delete ninja!</button>
        <br />
      </div>
    ) : null;
  });

  // EMBEDDED LOGIC

  // return (
  //   <div className="ninja-list">
  //     {ninjas.map(ninja => {
  //       return ninja.age > 20 ? (
  //         <div className="ninja" key={ninja.id}>
  //           <div>Name: {ninja.name}</div>
  //           <div>Age: {ninja.age}</div>
  //           <div>Belt: {ninja.belt}</div>
  //           <div>You are beautiful</div>
  //           <br />
  //         </div>
  //       ) : null;
  //     })}
  //   </div>
  // );

  return <div className="ninja-list">{ninjaList}</div>;
};

export default Ninjas;
