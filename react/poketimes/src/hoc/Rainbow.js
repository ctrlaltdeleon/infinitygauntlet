import React from "react";

const Rainbow = WrappedComponent => {
  const colours = ["red", "pink", "blue", "yellow", "green", "orange"];
  const randomColour = colours[Math.floor(Math.random() * 6)];
  const className = randomColour + "-text"; // For materialize

  return props => {
    return (
      <div className={className}>
        <WrappedComponent {...props} />
      </div>
    );
  };
};

export default Rainbow;
