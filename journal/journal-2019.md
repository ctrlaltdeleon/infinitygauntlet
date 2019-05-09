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

# May 6, 2019

- Cut my own hair.

# May 5, 2019

- Game of Thrones, Season 8, Episode 4!

# May 4, 2019

- Star Wars!

# May 3, 2019

- Photography!
  - Shot photos for an organization's banquet, over 700+ photos.
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

# April 30, 2019

- **Avengers: Endgame!** Round Two!
- Minecraft!
  - Got updated with the recent patches and gathered a team to build in a snow biome.
- Applied to Viasat.

# April 29, 2019

- Updated personal website.

# April 28, 2019

- Game of Thrones, Season 8, Episode 3!
- House work.

# April 27, 2019

- Photography!
  - Shot more graduation pictures, this time a group of 3.
- Finished curating the `Gitbook`!
- Posted to LinkedIn about the `Gitbook`.
- Tried out different online coding assessment testing such as `DevSkiller` and `Codility`.

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

# April 16, 2019

- Created a `Gitbook` for the repository of `infinitygauntlet`.
  - `Gitbook` is a hosting platform to showcase markdown files in a repository. Great for making books.
