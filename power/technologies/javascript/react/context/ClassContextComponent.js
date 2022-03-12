import React, { Component } from "react";

export default class ClassContextComponent extends Component {
  themeStyles(dark) {
    return {
      backgroundColor: darkTheme ? "#333" : "#CCC",
      color: darkTheme ? "#CCC" : "#333",
      padding: "2rem",
      margin: "2rem",
    };
  }

  // Notice the differences of nesting between a class component and a functional component.
  render() {
    return (
      <ThemeContext.Consumer>
        {(darkTheme) => {
          return <div style={this.themeStyles(darkTheme)}>Class Theme</div>;
        }}
      </ThemeContext.Consumer>
    );
  }
}
