import React, { useContext, useState } from "react";

/**
 * A general template for using context within functional components.
 */

const ThemeContext = React.createContext();
const ThemeUpdateContext = React.createContext();

// Hook to access value.
export function useTheme() {
  return useContext(ThemeContext);
}

// Hook to access value.
export function useThemeUpdate() {
  return useContext(ThemeUpdateContext);
}

export function ThemeProvider({ children }) {
  // Create the state.
  const [darkTheme, setDarkTheme] = useState(true);

  // Update the state.
  function toggleTheme() {
    setDarkTheme((prevDarkTheme) => !prevDarkTheme);
  }

  // Persist the state down to the children.
  return (
    <ThemeContext.Provider value={darkTheme}>
      <ThemeUpdateContext.Provider value={toggleTheme}>
        {children}
      </ThemeUpdateContext.Provider>
    </ThemeContext.Provider>
  );
}
