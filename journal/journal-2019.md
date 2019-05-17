# May 17, 2019

- N/A

# May 16, 2019

- Remember to fix the `PATH` when using `Visual Studio Code` to reference compilers!
- What are advantages of `React`?
  - Increase application performance.
  - Easily integrated with other frameworks.
- What are disadvantages of `React`?
  - Just a library, not a full framework.
  - Library is large and takes time to understand.
  - Difficult for novice programmers to understand.
  - Code gets complex through inline templating and `JSX`.
- What is `JSX`?
  - `JavaScript XML`.
  - A `React` extension that allows to write `JavaScript` that looks like `HTML`.

```js
render() {
  return(
    <div>
      <h1>This is JSX!</h1>
    </div>
  )
}
```

- Difference between `componentWillReceiveProps` and `componentWillUpdate`?
  - `componentWillReceiveProps` is called before `componentWillUpdate`.
  - `componentWillReceiveProps` allows to `setState`.
  - `componentWillUpdate` allows a response to the `setState` change.
- What is business logic in terms of computer software?
  - Part of the program that encodes the real-world business rules that determines how data can be create, displayed, stored, and changed.
  - Usually falls into these 3 categories:
    - Verification. (Identifying the user accessing what.)
    - Transformation. (Augmenting what the user can do.)
    - Processing. (How the data gets transferred securely.)
- When is it appropriate to use component state vs `Redux` store?
  - If a component just needs to display data and can receive data from a parent, use `Redux` store.
  - Otherwise if it needs the state, use component state.

# May 15, 2019

- What is `React`?
  - React is a front-end JavaScript library developed by Facebook in 2011.
  - It follows component based approach which helps in reusable UI components.
- What are the features of `React`?
  - Virtual DOM.
  - Server-side rendering.
  - Uni-directional data flow.
- What's a `DOM`?
  - Document Object Model.
  - Gives characteristics to specific parts of an application.
  - It's a tree.

```txt
      html
    /      \
  head    body
   |     /    \
  title h1    div
```

- Gym!
  - Back and biceps.

# May 14, 2019

- **Avengers: Endgame!** Round Three?
- Worked on Mindera interview.

# May 13, 2019

- What is `jQuery`?
  - A library of JavaScript functions that make it easier to do common tasks such as:
    - Manipulating webpage.
    - Responding to user events.
    - Getting data from servers.
    - Building effects and animation.

```js
// javascript

var images = document.getElementsByTagName("img");
for (var i = 0; i < images.length; i++) {
  images[i].style.width = "50px";
}

// jquery

$("img").width(50);
```

- How do you do a `fetch` call in `JavaScript`?

```js
// enclosed in a script tag

var apiUrl = "%WHERE_THE_FILE_IS%";
fetch(apiUrl)
  .then(response => {
    return response.json();
  })
  .then(data => {
    console.log("Work with the JSON data here: ", data);
  })
  .catch(err => {
    console.log("Work with the errors here:", err);
  });
```

- How should someone load a `.json` onto `HTML` ?
  - By using fragments so that when a large data set comes, it'll be pieced together rather than waiting for the whole load.
- Difference between `margin` and `padding`?
  - `Margin` takes place outside the `border`.
  - `Padding` takes place inside the `border`.
- How does `padding` work in terms of placement?
  - Think like the top of a clock.
  - `padding: top right bottom left;`
- Gym!
  - Freedom workout.

# May 12, 2019

- `<div class="">` vs `<div id="">`?
  - `class` is applied to many things (`.someClass`).
  - `id` is specific for one area (`#someID`).
- What is best practice for `<div class="">` vs `<div id="">`?
  - Usually want to `id` things such as `header`, `footer`, `sidebar` because there's only 1 `header` as such.
  - For something like `card`, a `class` would be wonderful because there is usually more than one `card` on a webpage.
- What happens if you use both `<div class="">` and `<div id="">`?
  - `id` will take precedence over the `class` selectors.
  - In the below code, `Hello!` would be red.

```html
<!-- index.html -->

<p id="intro" class="foo">Hello!</p>
```

```css
/* style.css */

#intro {
  color: red;
}
.foo {
  color: blue;
}
```

# May 11, 2019

- What does `HTML` mean?
  - HyperText Markup Language.
- `HTML5` vs `HTML`?
  - `HTML5` offers more such as new tags `<canvas>`. `<video>`, `<audio>`, and more bring much more.
  - `HTML` does not, but still is supported on all browsers as opposed to the updated `HTML5` which doesn't.

# May 10, 2019

- Made a `python` file which makes several strings and stops running when a specific string is found.
  - Had a lot of fun with this, formatted the output to be digestible.

```py
Current time: 0.0000 seconds | Current score: 0.25 | Input string found: yyaa
Current time: 0.0040 seconds | Current score: 0.50 | Input string found: rnss
Current time: 0.0317 seconds | Current score: 0.75 | Input string found: tess
It took 0.22 seconds to find: yess
```

- What is overloading?
  - When you have the same function taking in different parameters.
- Why would you use overloading?

```java
void println_emptyLine()
void println_boolean(boolean x)
void println_character(char x)

// with overloading...

void println()
void println(boolean x)
void println(char x)

// MOTIVATES CLEAN CODE!
```

- Does Python support overloading?
  - No, it's because you don't need to, it's flexible with default values.
- What is overriding?
  - When you have an inherited function, but would like to have it do something else.
- Why would you use overriding?

```java
class Thought {
    public void message() {
        System.out.println("I feel like I am diagonally parked in a parallel universe.");
    }
}

public class Advice extends Thought {
    @Override  // @Override annotation in Java 5 is optional but helpful.
    public void message() {
        System.out.println("Warning: Dates in calendar are closer than they appear.");
    }
}
```

- What is polymorphism?
  - Poly === Many, Morphism === Forms.
  - Many forms of one thing to achieve a result.
- Why use polymorphism?

```py
class Bird:
	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):
	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):
	def flight(self):
		print("Ostriches cannot fly.")

obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

"""
Output:

There are many types of birds.
Most of the birds can fly but some cannot.
There are many types of birds.
Sparrows can fly.
There are many types of birds.
Ostriches cannot fly.
"""

# MOTIVATES IMPLEMENTING INHERITANCE!
```

- What is boxing and unboxing?
  - Boxing is to convert a data type to an object.
  - Unboxing is the opposite, to convert an object to a data type.
- What's the difference between libraries and frameworks?
  - A library performs specific defined functions, like getting a piece of furniture that completes your home.
  - A framework provides a foundation where you input where you can, like selecting a house, but there's little options you can augment, but at the end of the day, it's up to the framework.
- What is a web service?
  - Another name for remote APIs.

# May 9, 2019

- What's object oriented programming?
  - A way to describe what a thing is and what i can do.
  - I made a button and what it does is log out the user.
- What's an API?
  - Application program interface.
- What are interfaces?
  - A class with no implementation, just prototyping.
  - They provide no variables, but specific functions to be expected in an implementing class.
- Why use interfaces?
  - Because it means that you know two pieces will fit together wherever it's needed.
  - Don't have to worry about if a car or truck works on a road, because they both implement the interface of vehicle.
- Design patterns are solutions to recurring problems.
- Types of design patterns!
  - Creational!
    - Focused on instantiating an object or group of related objects.
  - Structural!
    - Concerned with object composition (how entities can use each other).
    - "How to create a software component?"
  - Behavioral!
    - Concerned with assignment of responsibilities between objects.
    - Difference between this and structural is that not only do they specify the structure, but also outline patterns for communication between them.
    - "How to run a behavior in software component?"
- Examples of creational design patterns.
  - Singleton!
    - There can only be one president at a time. The same president has to be brought to action when needed. The president is a singleton with.
    - Strictly create a global instance of only 1 object with all methods.
- Examples of structural design patterns.
  - Bridge!
    - To have different themes for different pages, instead of creating multiple themed pages, this would apply a theme to the page.
    - This pushes implementation details from a hierarchy to another object with a separate hierarchy.
    - One interface would dictate webpages and getting a theme while the other would dictate the theme.
- Examples of behavioral design patterns.
  - State!
    - Think `React`.
    - If the user is logged in, update the UI to show relevant information to the user.

# May 8, 2019

- Is it possible to break JavaScript code into several lines?
  - Yes through utilizing the backslash `\`.
- Which company developed JavaScript?
  - Netscape is the software company who developed JavaScript.
  - Brendan Eich in 1995 was the one who spearheaded the language.
- Differences between undeclared and undefined variables?
  - Undeclared variables are variables that don't exist yet.
  - Undefined variables are variables that don't have meaning yet.
- Write the code for adding new elements dynamically in JavaScript?
  - Inside the `.html` file, put a `<script src="/index.js" type="text/javascript" charset="UTF-8">` with the code within.
  - `src` takes the source code and redistributes it into the `.html`.
  - Old browsers take in the type of `text/javascript` while newer ones also take in both the previous and `application/javascript`.
  - `charset` tells the browser how to interpret the characters (needed for foreign languages).
- The difference between `==` and `===`?
  - `==` checks value while `===` checks value and type.
  - For example `"24" == 24` would be true, but `"24" === 24` would be false because it is comparing a string and an integer.
- What's the use of lambda functions?
  - They are used as small anonymous functions.
  - They can take any parameters, but can only have one expression.
  - `lambda a : a + 10` takes in parameter `a` and adds 10 to it.

# May 7, 2019

- **Code Geass: Lelouch of the Re;surrection!**
- Gym!
  - Legs and shoulders.

# May 6, 2019

- Cut my own hair.
- Edited photos.

# May 5, 2019

- Game of Thrones, Season 8, Episode 4!

# May 4, 2019

- Star Wars!
- Edited photos.

# May 3, 2019

- Main differences between Java VS JavaScript.
  - Java.
    - Object oriented programming language.
      - Compiled (non-human readable code) then executed.
    - Mainly runs on the Java Virtual Machine (JVM).
  - JavaScript.
    - Object oriented scripting language.
      - Interpreted (not compiled).
    - Mainly runs on browser (More applications through React now).
- JavaScript Data Types?
  - Number.
  - String.
  - Boolean.
  - Object (When you don't know what it'll be during compile time).
  - Undefined.
- In JavaScript, what is the use of `isNaN` function?
  - `isNaN` returns true if argument is not a number, else false.
- How do you achieve negative infinity in JavaScript?
  - `%NEGATIVE_NUMBER%/0`
- What does `console.log(A || B) do?
  - Same as a ternary, if A exists, print A, otherwise B.
- Difference between a method and function?
  - Methods are functions that are members of a class.
  - All methods are functions, but not all functions are methods.
- When to use `throw` vs `throw e`?
  - `throw` shows all information.
  - `throw e` resets the stack trace and shows core information.
  - Best practice to use `throw`.
- `DateTime`!
  - Remember when creating updates to new objects, it doesn't update, it creates new, so must assign everytime.
  - Instead of `clockerino.AddDays(1);`, do `clockerino = clockerino.AddDays(1);`
- What do you do if you encounter a `for` loop with augmenting a string?
  - Use `StringBuilder` if available, fast and less memory.
- Photography!
  - Shot photos for an organization's banquet, over 700+ photos.
- Gym!
  - Chest and triceps.

# May 2, 2019

- More OOP understanding.
  - Classes are like blueprints.
    - These classes contain properties and methods.
      - Properties are such as "fire type".
      - Methods are such as "flamethrower".

# May 1, 2019

- Performed `Leetcode` questions.
- Object oriented programming revolves around 4 pillars.
  - Encapsulation.
    - Reduce complexity + increase resuability.
    - Charmander is hungry. You can feed() Charmander, but you can't change how hungry the cat is directly because that's private properties.
  - Abstraction.
    - Reduce complexity + isolate impact of changes.
    - Charmander can use flamethrower, but you don't know how it does it, you just use it.
  - Inheritance.
    - Eliminate redundant code.
    - Charizard inherits Charmander's traits and moves, no need to recreate.
  - Polymorphism.
    - Refactor ugly switch/case statements.
    - Charizard can use "flamethrower" like Charmander, but a different version called "fire blast!".
- Gym!
  - Back and biceps.

# April 30, 2019

- Applied to Viasat.
- **Avengers: Endgame!** Round Two!
- Minecraft!
  - Got updated with the recent patches and gathered a team to build in a snow biome.

# April 29, 2019

- Updated personal website.

# April 28, 2019

- Game of Thrones, Season 8, Episode 3!
- House work.

# April 27, 2019

- Finished curating the `Gitbook`!
- Posted to LinkedIn about the `Gitbook`.
- Tried out different online coding assessment testing such as `DevSkiller` and `Codility`.
- Photography!
  - Shot more graduation pictures, this time a group of 3.
- Gym!
  - Legs and shoulders.

# April 26, 2019

- Photography!
  - Spent the whole day editing photos and working out the Flickr account intricacies.

# April 25, 2019

- **Avengers: Endgame!**

# April 24, 2019

- Gym!
  - Chest and triceps.

# April 23, 2019

- `Gitbook` is technical on `h1` formatting, so best to stick with the original `Github` look than catering to `Gitbook` itself.

# April 22, 2019

- Gym!
  - Back and biceps.

# April 21, 2019

- Game of Thrones, Season 8, Episode 2!
- Car!
  - Changed the catalytic converter in my car.
  - Process took a while due to clearance, but that's what the WD-40 is there for.

# April 20, 2019

- Gardening!
  - Helped my father out with gardening.
  - Learned that to prevent weeds, need a black tapestry over the dirt, but surrounding the wanted potted plants.
- Photography!
  - When popping the champagne, pre-pop it already without shaking and place a finger on the top.
  - When ready to take the photo, shake the bottle, and unleash the power!
  - Always clean after yourself, confetti is everywhere from other people.

# April 19, 2019

- Photography!
  - Shot for SDSU APSA's FTS.
  - Took into account for shutter speed and ISO for dance performances (1/1000, 800 ISO).

# April 18, 2019

- Went over `ReactJS` technicalities.
- Instead of writing `.bind(this)` to every method that exists...

```js
constructor(props){
  super(props);
  this.handleClick = this.handleClick.bind(this);
}

handleClick(event){
  // do stuff!
}
```

- We can instead use lexical scope.
  - Lexical scope is where a variable can be referenced within the scope that it is defined in.

```js
handleClick = event => {
  // do stuff!
};
```

- With `Context` and `Hooks` available for `ReactJS` now, `Redux` may be a thing in the past.

# April 17, 2019

- Messaged Anthony, host of San Diego JavaScript Community Talks, about performing a talk.
- Messaged the General Assembly group of LA about future hackathons.
  - Feels nice to have a community dev spot for me in LA!
- Updated creddle.io resume.
  - Removed the `knucklesbattle` repo with the `acfromspacex` repo to harbor current technologies I'm working with which is mainly `ReactJS` as well as touching other technologies such as `GraphQL` and `Apollo'.
  - Updated skills to go from "advanced, proficient, exploring" rather than placed by "programming languages, web technologies, creative software engines, databases".
    - I thought this was necessary to avoid questions on topics I wasn't too familiar about because there were no skill levels to differentiate.
- Applied to CyberCoders.
- Cleaned out the Thunderbird email!
- Gym!
  - Legs and shoulders.

# April 16, 2019

- Created a `Gitbook` for the repository of `infinitygauntlet`.
  - `Gitbook` is a hosting platform to showcase markdown files in a repository. Great for making books.
- Started the journal! About time.
