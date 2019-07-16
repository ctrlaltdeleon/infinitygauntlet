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

// Different types of doors with the base of being a door.
class Door {
  constructor() {
    this.getDescription = () => {};
  }
}

// An iron door.
class IronDoor extends Door {
  constructor() {
    super();
    this.getDescription = () => "I am an iron door!";
  }
}

// A wooden door.
class WoodenDoor extends Door {
  constructor() {
    super();
    this.getDescription = () => "I am a wooden door!";
  }
}

// Experts according to the doors.
class DoorFittingExpert {
  constructor() {
    this.getDescription = () => {};
  }
}

// A welder is expected to fit iron doors.
class Welder extends DoorFittingExpert {
  constructor() {
    super();
    this.getDescription = () => "I can only fit iron doors.";
  }
}

// A carpenter is expected to fit wooden doors.
class Carpenter extends DoorFittingExpert {
  constructor() {
    super();
    this.getDescription = () => "I can only fit wooden doors.";
  }
}

// The door factory encapsulates the correct door to the correct expert.
class DoorFactory {
  constructor() {
    this.makeDoor = () => {};
    this.makeFittingExpert = () => {};
  }
}

// A wooden door factory creates wooden doors with carpenters.
class WoodenDoorFactory extends DoorFactory {
  constructor() {
    super();
    this.makeDoor = () => new WoodenDoor();
    this.makeFittingExpert = () => new Carpenter();
  }
}

// An iron door factory creates iron doors with welders.
class IronDoorFactory extends DoorFactory {
  constructor() {
    super();
    this.makeDoor = () => new IronDoor();
    this.makeFittingExpert = () => new Welder();
  }
}

// Create a wooden factory with the proper door, a wooden door, and proper expert, a carpenter.
const woodFactory = new WoodenDoorFactory();
const woodDoor = woodFactory.makeDoor().getDescription();
const woodExpert = woodFactory.makeFittingExpert().getDescription();

// Create an iron factory with the proper door, an iron door, and proper expert, a welder.
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
