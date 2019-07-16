# ABSTRACT FACTORY

## What is it?

- A factory of factories; a factory that groups the individual but related/dependent factories together without specifying their concrete classes.
- Instead of micromanaging which worker to which door, we would just need to access the correct factory and that will handle the door and the worker itself.

## When to use?

- When there are interrelated dependencies with not-that-simple creation logic involved.
- In this case, to reduce the amount of variables to work with and have the overall application be simpler.

```jsx
import React from "react";
import ReactDOM from "react-dom";

// Create different types of doors.
class Door {
  constructor() {
    this.getDescription = () => {};
  }
}

class IronDoor extends Door {
  constructor() {
    super();
    this.getDescription = () => "I am an iron door!";
  }
}

class WoodenDoor extends Door {
  constructor() {
    super();
    this.getDescription = () => "I am a wooden door!";
  }
}

// Create different types of experts according to the doors.
class DoorFittingExpert {
  constructor() {
    this.getDescription = () => {};
  }
}

class Welder extends DoorFittingExpert {
  constructor() {
    super();
    this.getDescription = () => "I can only fit iron doors.";
  }
}

class Carpenter extends DoorFittingExpert {
  constructor() {
    super();
    this.getDescription = () => "I can only fit wooden doors.";
  }
}

// Create a door factory which encapsulates the correct door to the correct expert.
class DoorFactory {
  constructor() {
    this.makeDoor = () => {};
    this.makeFittingExpert = () => {};
  }
}

class WoodenDoorFactory extends DoorFactory {
  constructor() {
    super();
    this.makeDoor = () => new WoodenDoor();
    this.makeFittingExpert = () => new Carpenter();
  }
}

class IronDoorFactory extends DoorFactory {
  constructor() {
    super();
    this.makeDoor = () => new IronDoor();
    this.makeFittingExpert = () => new Welder();
  }
}

const woodFactory = new WoodenDoorFactory();
const woodDoor = woodFactory.makeDoor().getDescription();
const woodExpert = woodFactory.makeFittingExpert().getDescription();

const ironFactory = new IronDoorFactory();
const ironDoor = ironFactory.makeDoor().getDescription();
const ironExpert = ironFactory.makeFittingExpert().getDescription();

function App() {
  return (
    <div className="App">
      <p>Door: {woodDoor}</p>
      <p>Expert: {woodExpert}</p>
      <p>Door: {ironDoor}</p>
      <p>Expert: {ironExpert}</p>
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
```

## Output

```
Door: I am a wooden door!
Expert: I can only fit wooden doors.
Door: I am an iron door!
Expert: I can only fit iron doors.
```
