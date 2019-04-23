import React from "react";

// If JavaScript is disabled

module.exports = class HTML extends React.Component {
  render() {
    return (
      <noscript>
        <h1>Please enable JavaScript!</h1>
        <p>something something something</p>
      </noscript>
    );
  }
};
