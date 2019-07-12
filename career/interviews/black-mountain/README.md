# BLACK MOUNTAIN

## Round 1 (Online)

- Coding reasoning questions.

## Round 2 (Phone)

- Behavioral.
- Introduction to the company.

## Round 3 (Phone)

- Behavioral and technical.
- Questions based on C# and JavaScript.
- "Name me some design patterns!"
  - Creational.
    - Singleton.
  - Structural.
    - Adapter.
    - Bridge.
  - Behavioral.
    - State.
- "All classes derive from?"
  - Objects.
- "What is the `using` statement for?"
  - To ensure that the object is disposed as soon as it goes out of scope, and it doesn't require explicit code to ensure that this happens.
- "What is the difference between Interface and Abstract Class?"
  - Interface provides a template of functions, but not implemented, provides multiple inheritance.
  - Abstract class may provide state (data members) and/or implementation (methods).

```cs
using (var conn = new SqlConnection("connection string"))
{
   conn.Open();
    // Execute SQL statement here on the connection you created.
}
```

- "What is the difference between dynamic type variables and object type variables?"
  - Dynamic type variables takes place at run time. (Skips boxing/unboxing, unsafe fast).
  - Object type variables takes place at compile time. (Strong-typed, safe alright).
- "What kind of language is JavaScript?"
  - An interpreted, scripted, non-compiled language.
- "How to create a new object?"
  - Define and create a single object, using an object literal.
    - `var person = {name: "AC"};`
  - Define and create a single object, with the keyword new.
    - `var person = new Person();`
  - Define an object constructor, and then create objects of the constructed type.

```js
function Person(name) {
  this.name = name;
}

var person = new Person("AC");
```

- "What is the difference between `==` and `===`?"
  - `==` checks value while `===` checks value and type.
  - For example `"24" == 24` would be true, but `"24" === 24` would be false because it is comparing a string and an integer.
- "What is a `promise`?"
  - A `promise` is saying you will do something and depending on the result affects the outcome.

```js
var makePromiseWithSon = function() {
  SonService.getWeather().then(
    function(data) {
      // Promise fulfilled.
      if (data.forecast === "good") {
        prepareFishingTrip();
      } else {
        prepareSundayRoastDinner();
      }
    },
    function(error) {
      // Promise rejected.
      // Could log the error with: console.log('error', error);
      prepareSundayRoastDinner();
    },
  );
};
```

- "What is a closure?"
  - A closure is where an inner function has access to the outer (enclosing) function’s variables — a scope chain.

```js
function init() {
  var name = "Mozilla"; // `name` is a local variable created by init.
  function displayName() {
    // `displayName()` is the inner function, a closure.
    alert(name); // Use variable declared in the parent function.
  }
  displayName();
}
init();
```

## Round 4 (On-Site)

- ER diagram.
- Coding solution.
- Culture fit.

## Round 5 (Offer)

- Did not make it.
