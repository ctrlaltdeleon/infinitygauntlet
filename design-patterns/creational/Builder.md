# BUILDER

## What is it?

- Allows you to create different flavors of an object while avoiding constructor pollution.
- Useful when there could be several flavors of an object or when there are a lot of steps involved in creation of an object.
- Instead of the hiring manager interviewing all candidates, have specialized interviewers interview sections of candidates.

## When to use?

- Useful when there is some generic processing in a class but the required sub-class is dynamically decided at runtime.
- Or putting it in other words, when the client doesn't know what exact sub-class it might need.
- In this case, when the hiring manager doesn't know what exact managers needed to interview candidates.

```js
import React from "react";
import ReactDOM from "react-dom";

export class Burger {
  constructor(builder) {
    if (builder) {
      this.size = builder.size;
      this.cheese = builder.cheese;
      this.pepperoni = builder.pepperoni;
      this.lettuce = builder.lettuce;
      this.tomato = builder.tomato;
    } else {
      this.size = false;
      this.cheese = false;
      this.pepperoni = false;
      this.lettuce = false;
      this.tomato = false;
    }
  }
}

export class BurgerBuilder {
  constructor(size) {
    this.size = size;
    this.cheese = false;
    this.pepperoni = false;
    this.lettuce = false;
    this.tomato = false;
  }

  addPepperoni() {
    this.pepperoni = true;
    return this;
  }

  addLettuce() {
    this.lettuce = true;
    return this;
  }

  addCheese() {
    this.cheese = true;
    return this;
  }

  addTomato() {
    this.tomato = true;
    return this;
  }

  build() {
    return new Burger(this);
  }
}

const burger = new BurgerBuilder(14)
  .addPepperoni()
  .addLettuce()
  .addTomato()
  .build();

function App() {
  return (
    <div className="App">
      <div className="subtitle">Burger #{burger.size}</div>
      {!burger.cheese && <p>no cheese</p>}
      {burger.pepperoni && <p>add pepperoni</p>}
      {burger.lettuce && <p>add lettuce</p>}
      {burger.tomato && <p>add tomato</p>}
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
