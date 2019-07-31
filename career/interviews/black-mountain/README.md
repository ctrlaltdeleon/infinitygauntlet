# BLACK MOUNTAIN

## Round 1 (Online)

- No time limit with no person.
- Technical.
- Coding reasoning questions in `C#`.
- "How would you build a string in `C#` efficiently?"
  - Using the `StringBuilder` library for speed and less consuming of memory.
- "What is the difference between these two scenarios?"
  - `A` preserves all error information.
  - `B` resets the stack trace and shows core error information.

```cs
// A
try { ... }
catch (Exception ex)
{
    throw;
}
```

```cs
// B
try { ... }
catch (Exception ex)
{
    throw ex;
}
```

- "What is wrong with the code?"
  - The method `Name` and the `get` and `set` fields are the same, so this means when you call the method, it will keep calling itself therefore an infinite loop.

```cs
public string Name
{
    get { return Name; }
    set { Name = value ?? String.Empty; }
}
```

- "How do you fix this implementation of `DateTime`"?
  - `dt.AddDays(1)` works, but isn't assigned to a return value.
  - It works like this because it creates a new object, not update the previous one.

```cs
DateTime GetTomorrow()
{
    DateTime dt = DateTime.Now;
    dt.AddDays(1);
    return dt;
}
```

- "Can this method return true?"
  - Say for example `(T t) → (Int number), return typeof(int) != number.GetType();`, this will always return false.
  - But what if `(T t) → (Object obj), where obj = “hello”? typeof(object) → object, obj.GetType(); → string`!
  - Yes it can return true if an object is being passed as an object would be returned for `typeof(T)`, but for the `GetType()`, it could be anything that the object is assigned to.

```cs
static bool TT<T>(T t)
{
    return typeof(T) != t.GetType();
}
```

- "Implement `Fizzbuzz` but with `CheeseBurger`!"

```cs
function cheeseBurger() {
    var limit = 50;
    for (var i = 1; i <= limit; i++) {
    	soln = “”
        if (i % 3 == 0) soln += "Cheese";
        if (i % 5 == 0) soln += "Burger";
        console.log(soln || i);
    }
}
```

- "Return whether or not an array has duplicate integers. No libraries can be used."
  - This will return true if there are duplicates, otherwise false.
  - This compares the original length of the array to the new array within a set, a data structure that doesn’t allow duplicates.

```cs
function duplicateIntegersInArray(array) {
    return array.length != new Set(array).size;
}
```

- "Correct the code so that `countingFunctions` is correctly populated."
  - When the first function is called, it goes through the whole loop thus printing out `16` from start to end value times (In this case 15 times).
  - To fix this, we need to reserve a copy by enclosing `i` within the function as well.

```cs
// Broken.
var countingFunctions = [];

for (var i=1; i<=15; i++) {
	countingFunctions.push(function() {
	console.log(i);
	});
}

countingFunctions.forEach(function(f) {f();});
```

```cs
// Fixed.
var countingFunctions = [];

for (var i=1; i<=15; i++) {
	(function() {
		var copy = i;
		countFunctions.push(function() {
			console.log(copy);
		});
	})();
}

countingFunctions.forEach(function(f) {f();});
```

## Round 2 (Phone)

- 30 minutes with Senior Recruiter.
- Behavioral.
- Introduction to the company.

## Round 3 (Phone)

- 30 minutes with Software Engineer.
- Behavioral and technical.
- Questions based on `C#` and `JavaScript`.
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

- 4 hours with Senior Software Engineer.
- Behavioral, cultural, and technical.
- ER diagram.
  - Given a series of entities and relationships, how would they interact with each other?
- Coding solution.
  - Stock management.
- Culture fit.

## Round 5 (Offer)

- Did not make it.
