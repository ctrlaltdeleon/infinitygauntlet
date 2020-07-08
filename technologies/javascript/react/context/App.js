import React from "react";
import ClassContextComponent from "./ClassContextComponent";
import FunctionContextComponent from "./FunctionContextComponent";
import { ThemeProvider } from "./ThemeContext";

export default function App() {
  return (
    <ThemeProvider>
      <ClassContextComponent />
      <FunctionContextComponent />
    </ThemeProvider>
  );
}
