// Utilize different components from react plugin

import React, { Component } from "react";

class react extends Component {
  render() {
    return (
      <div>
        <h1>Standard component class</h1>
      </div>
    );
  }
}

export default react;

import React from 'react';

const react = () => {
  return (
    <div>
      <h1>Standard function class</h1>
    </div>
  );
};

export default react;
