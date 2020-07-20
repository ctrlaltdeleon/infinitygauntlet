# July 19 2020

- Submitted what I could for work, still a lot to consider.
- Gym!
  - Freedom.

# July 18 2020

- Went to Sharetea, Ikea, Sushi Kuchi, and Mount Soledad with friends and it was nice.

# July 17 2020

- Relaxed, caught up on sleep.

# July 16 2020

- Gym!
  - Volleyball.
- Went over to help out a friend with their computer and it's working!

# July 15 2020

- ???

# July 14 2020

- How to iterate over all the properties of an object `obj`?

```jsx
for (var key in obj) {
  console.log(key, obj[key]);
}

// If you want to avoid inherited properties:

for (var key in obj) {
  if (!obj.hasOwnProperty(key)) continue;
  console.log(key, obj[key]);
}

// For the new ECMAScript 5th Edition:
Object.keys(obj).forEach(function (key) {
  console.log(key, obj[key]);
});
```

- What does the `array.forEach()` method do?
  - Iterates over the array items, in ascending order (0, 1, 2...), without mutating the array.
- What are the differences in defining state value in `React`?

```jsx
// Previously.
class App extends React.component {
  state = {
    messageCount: 0
  };

  const messageCount = this.state.messageCount;

  setMessageCount = count => (
    setState({messageCount:count});
  )
  ...
}

// Now!
function App() {
  count [messageCount, setMessageCount] = useState(0);
}
```

- How to access the last element of an array in `Javascript`?
  - `var last_element = my_array[my_array.length - 1]`
- How to add new properties to an object?
  - There's 2 ways.
  - Dot notation!
    - `obj.new_key = "new_value";`
  - Square bracket notation!
    - `obj["new_key"] = "new_value";`
- How to check if object value exists within a `Javascript` array of objects?

```jsx
const arr = [
  { id: 1, username: "fred" },
  { id: 2, username: "bill" },
  { id: 3, username: "ted" },
];

function add(arr, name) {
  const { length } = arr;
  const id = length + 1;
  // If the array has a username equivalent to the parameter given username.
  const found = arr.some((el) => el.username === name);
  // If the username is unique, push the new object username.
  if (!found) arr.push({ id, username: name });
  return arr;
}

console.log(add(arr, "ted"));
```

- Twitch!
  - Great stream.

# July 13 2020

- I need to catch up on sleep, haven't been feeling well.
- Gym!
  - Freedom.

# July 12 2020

- ???

# July 11 2020

- Went to say goodbye to a friend who's moving back to LA.
- Got to meet up with unexpected friends, truly blessed.

# July 10 2020

- ???

# July 9 2020

- What happens if there's nothing for the second argument of a `useEffect()` function?
  - Infinitely loops as opposed to an empty array for the second argument would be only 1 run.
- Is it possible to not use state and just use refs?
  - Can't.
  - Refs aren't reactive so when those are changed, there are no re-renders done as opposed to state.

# July 8 2020

- In `React`, how could you call a method on load once when `componentDidMount` is not in use?

```js
// This is in the case of a function component.
// The `useEffect` component will act as a initial load.

function MyComponent(props) {
  useEffect(() => {
    // Stuff!
  }, []); // Empty dependency!
  return <div></div>;
}
```

- Gym!
  - Freedom.
  - Tennis.

# July 7 2020

- How to bring other branches onto your branch view, but not update the branch you're working on?
  - `git fetch origin`
- What are actions in `React`?
  - They are payloads of information that send data from your application to the store.
- What are reducers in `React`?
  - Specify how the application's state changes changes in response to actions sent to the store.

# July 6 2020

- Back on the software engineer grind.
- Let's learn!

# July 5 2020

- Relaxed.
- Gym!
  - Freedom.

# July 4 2020

- Relaxed.

# July 3 2020

- Made Twitch Affiliate!

# July 2 2020

- Relaxed.

# July 1 2020

- Relaxed.

# June 30 2020

- What does `React Hooks` and `Context API` help make?
  - A `Flux/Redux` pattern.
- What is the `useEffect` hook for?
  - It'll be similar to previous `React` lifecycle methods such as `componentDidMount`, `componentDidUpdate`, and `componentWillUnmount`.

# June 29 2020

- Bolt appointment that turned into a surgery.
- DMV called about license plate, so I had to pick it up.
- Slept early, no social interaction today.
- Gym!
  - Freedom.

# June 29 2020

- Another example of `React Context` is in the `react/context/` folder.
- When would you use class components over functional components?
  - It's gotten to the point where the only use is for access lifecycle methods that are specific to class components, otherwise can stick to functional.

# June 28 2020

- What is `React Context`?
  - Global state management for an application.
  - Context provides a way to pass data through the component tree without having to pass props down manually at every level.
- Why use `React Context`?
  - Imagine passing down `props` which in itself isn't so bad across 2 components.
  - If it's across multiple components with multiple nested structures, it becomes difficult to manage.
- How to start with `React Context`?
  - Create the context, `React.createContext()`
  - Provide a context value, `<UserProvider value={...something}>`
  - Consume the context value, `<UserConsumer>...</UserConsumer>`

```js
// userContext.js

import React from 'react';

const UserContext = React.createContext();

const UserProvider = UserContext.Provider;
const UserConsumer = UserContext.Consumer;

export { UserProvider, UserConsumer };

export default UserContext;

// App.js

import React, { Component } from 'react';
import AAAComponent from './components/AAAComponent';
import { UserProvider } from './components/userContext';

class App extends Component {
  render() {
    const user = {firstName: 'AC', lastName: 'De Leon'}
    return (
      <div className="App">
        <UserProvider value={...user}>
          <AAAComponent/>
        </UserProvider>
      </div>
    )
  }
};

export default App

// AAAComponent.js

import React, { Component } from 'react';
import BBBComponent from './components/BBBComponent';

class AAAComponent extends Component {
  render() {
    return (
      <div>
        <BBBComponent/>
      </div>
    )
  }
};

// BBBComponent.js

import React, { Component } from 'react';
import AAAComponent from './AAAComponent';
import UserContext from './userContext';

class BBBComponent extends Component {
  render() {
    return (
      <UserContext.Consumer>
        {user => (
          <p>User: {user.firstName} {user.lastName}</p>
        )}
      </UserContext.Consumer>
    )
  }
}

BBBComponent.contextType = UserContext;

export default BBBComponent

```

# June 27 2020

- Relaxed.
- Getting back on the grind of continuing this journal.

# June 26 2020

- Gym!
  - Freedom.

# June 25 2020

- Gym!
  - Volleyball.

# June 24 2020

- ???

# June 23 2020

- ???

# June 22 2020

- Gym!
  - Freedom.

# June 21 2020

- ???

# June 20 2020

- Gym!
  - Freedom.

# June 19 2020

- Gym!
  - Freedom.

# June 18 2020

- Left my second tour and decided where I want to go permanent.
- Gym!
  - Freedom.

# June 17 2020

- Gym!
  - Freedom.

# June 16 2020

- ???

# June 15 2020

- Gym!
  - Freedom.

# June 14 2020

- ???

# June 13 2020

- Gym!
  - Freedom.

# June 12 2020

# June 11 2020

# June 10 2020

- Gym!
  - Freedom.

# June 9 2020

- Gym!
  - Freedom.

# June 8 2020

- Gym!
  - Freedom.

# June 7 2020

# June 6 2020

# June 5 2020

- Gym!
  - Freedom.

# June 4 2020

# June 3 2020

- Gym!
  - Freedom.

# June 2 2020

# June 1 2020

- Gym!
  - Freedom.

# May 31 2020

# May 30 2020

# May 29 2020

# May 28 2020

- Gym!
  - Freedom.

# May 27 2020

# May 26 2020

- Gym!
  - Freedom.

# May 25 2020

# May 24 2020

# May 23 2020

- Gym!
  - Freedom.

# May 22 2020

# May 21 2020

# May 20 2020

# May 19 2020

- Gym!
  - Freedom.

# May 18 2020

# May 17 2020

# May 16 2020

# May 15 2020

- Gym!
  - Freedom.

# May 14 2020

# May 13 2020

- Gym!
  - Freedom.

# May 12 2020

# May 11 2020

- Gym!
  - Freedom.

# May 10 2020

# May 9 2020

# May 8 2020

- Gym!
  - Chest and triceps.

# May 7 2020

# May 6 2020

- Gym!
  - Freedom.

# May 5 2020

- Gym!
  - Freedom.

# May 4 2020

# May 3 2020

# May 2 2020

# May 1 2020

# April 30 2020

- Gym!

  - Freedom.

# April 29 2020

- Gym!

  - Freedom.

# April 28 2020

- Gym!
  - Freedom.

# April 27 2020

- Researched mechanical keyboards for a good portion of my day.
  - Decided I want a 75 keyboard. (Removes the numpad at the right while staying compact.)
- Gym!
  - Freedom.

# April 14 2020

- Gym!
  - Freedom.

# April 13 2020

- Bought a lot of things due to quarantine.
- Gym!
  - Freedom.

# April 12 2020

- Gym!
  - Freedom.

# April 11 2020

- Helped around the house.
- Thought of some video ideas dealing with city pop.
- Gym!
  - Freedom.

# April 10 2020

- Gym!
  - Freedom.

# April 9 2020

- Working with `SonarLint` in `JavaScript`.
  - MAJOR - S3404: Remove this "!==" check; it will always be true. Did you mean to use "!="?
    - `"3" != 3` will return false because `JavaScript` will perform type coercion and compare values.
    - `"3" !== 3` will return true because since they are different types, despite the value, it will never be equal.
- What is type coercion in `JavaScript`?
  - When the operands of an operator are different types, one of them will be converted to an "equivalent" value of the other operand's type.
  - `boolean == integer` will cause the boolean to be converted to an integer.
  - `false` becomes `0` and `true` becomes `1`.
- Gym!
  - Freedom.

# April 8 2020

- Work.
- Gym!
  - Freedom.

# April 7 2020

- Work.
- Gym!
  - Freedom.

# April 6 2020

- Work.
- Gym!
  - Freedom.

# April 5 2020

- Gym!
  - Freedom.

# April 4 2020

- Gym!
  - Freedom.

# April 3 2020

- Work.
- Gym!
  - Freedom.

# April 2 2020

- Work.
- Gym!
  - Freedom.

# April 1 2020

- Work.
- Gym!
  - Freedom.

# March 31 2020

- Work.

# March 30 2020

- Work.

# March 29 2020

- Relaxed.

# March 28 2020

- Relaxed.

# March 27 2020

- Relaxed.

# March 26 2020

- Work.

# March 25 2020

- With my new tour and going over `SonarQube` and running it locally.

# March 24 2020

- Trying to get my development environment up.
  - Confusing, wish I had physical help to get jump started.
- Gym!
  - Freedom.

# March 23 2020

- Lots of email and loose ends to finish up before going to my next tour.

# March 22 2020

- Relaxed.
- Gym!
  - Freedom!

# March 21 2020

- Relaxed.

# March 20 2020

- Emergency meeting, telework mandatory unless stated otherwise.

# March 19 2020

- Got approved for telework!
- `Docx`, a library that translates within `JavaScript` to a `.docx` file, is painfully hard to work with due to the differences of time between technologies.
  - For example having `React` create a 2007 Microsoft Word file? Geez.

# March 18 2020

- Getting ready for telework soon.
- PDFs are so hard to work with.

# March 17 2020

- Fixed up code, `SonarQube` has stopped yelling at me.
- The virus is getting worse it feels like.

# March 16 2020

- How to make nested attributes within a class?

```java
// Notice that it's a class within a class.

public class PositionObject {
  private int id;
  private Position position;

  public PositionObject (int id, Position position) {
      this.id = id;
      this.position = position;
  }

  class Position {
    Float lat;
    Float lon;

    Position (Float lat, Float lon) {
      this.lat = lat
      this.lon = lon
    }
  }
}

// & to call the class.

PositionObject positionObject = new PositionObject(1, new Position(2f, 3f));
```

- What are the state and life cycle changes to `React`?
  - The need for class components has significantly lowered down since functional can just do the same with less code.
  - Instead of defining initial state in a constructor, we can use `React Hooks`, specifically `useState`.
  - Instead of `componentDidMount` and `componentDidUpdate`, `useEffect`, which is part of `React Hooks`, can manage changes made to the state.
- How to untrack files already added to `Git` when adding the `.gitignore` afterwards?
  - Commit all changes, including `.gitignore`.
  - `git rm -r --cached .`
  - `git add .`
  - `git commit -m "[-] .gitignore fix"`
  - Done!
- Try to workout when you can.
- Gym!
  - Freedom.

# March 15 2020

- Stores were barren of supplies such as:
  - Shampoo.
  - Soap.
  - Toilet paper.
  - Toothpaste.
- If you're reading this, stay safe out there.

# March 14 2020

- Relaxed.
- Wanted to go out, but COVID-19.

# March 13 2020

- Hung out with friends at Shabumi, Cafe Hue, and Nishiki.

# March 12 2020

- Last sprint review for the code I'm touring with.
- How do you print the contents of an object in `Java`?
  - Go to the class object, right click the class to create an auto-generated `toString()` function.

# March 11 2020

- How do children access parent libraries in software development?
  - It shouldn't be the case as a library should be imported in the module that actually uses it.
  - Explicit is better than implicit.
- What are the different ways to kill a process?
  - `Ctrl + Z` pauses a process.
  - `Ctrl + C` politely asks the process to shut down now.
  - `Ctrl + /` this process just got CLAPPED. 👏
- Gym!
  - Chest and triceps.

# March 10 2020

- Relaxed.

# March 9 2020

- After playing with `IntelliJ` I realize I have no idea how `Java` works.
- How do you check your `Maven` set-up?
  - `mvn --version`
- What is the difference between `Float` and `float`?
  - The object `Float` can be set to null to represent a value that is unknown.
  - The primitive `float` is guaranteed to have a value.
- Gym!
  - Back and biceps.

# March 8 2020

- Relaxed.

# March 7 2020

- Happy birthday Japanese child.
- Movie!
  - Boku no Hero Academia: Heroes Rising.
- Gym!
  - Volleyball.
  - Remember it's not about you.

# March 6 2020

- In `React`, what does `useEffect` hook do?
  - Replaces `componentDidMount` and `ComponentDidUpdate`.
  - The second argument of `useEffect` will go over an array of values the effect depends on.
    - Passing an empty array, the `useEffect` will only run on first render.
- How to stash in the terminal for `Git`?
  - `git stash` or `git stash push`
- How do you apply the stash in the terminal for `Git`?
  - `git stash apply`
- What if you have multiple stashes, how do you choose which one to apply?
  - `git stash apply "stash@{n}"` (Quotations may or may not be used depending on the shell.)
- What is a framework?
  - A framework (or a library) is pre-written code that makes it easier to build the same kind of thing repeatedly.
- What is front-end?
  - Anything that has to do with the UI/UX software development.
  - Front-end is not always client-side, but client-side is always front-end.
- What is a front-end framework?
  - This term causes confusion as most people really mean is client-side rendering framework.
  - Generally (in the 2020 context, future readers of this journal), a front-end framework is a code library (aka pre-written) to make client-side rendering easier & faster.
  - Examples include:
    - React.
    - Vue.
    - Angular.
- What is back-end?
  - Anything that has to do with nothing of the UI/UX sort.
- What is a back-end framework?
  - They're usually "general purpose web frameworks".
  - Can do back-end and front-end duties.
  - Examples include:
    - Rails.
    - Django.
    - Laravel.
    - ExpressJS.
- Gym!
  - Legs and shoulders.

# March 5 2020

- Why do bash script history persist even after shutdown of `Linux` in virtual machine?

```bash
# Due to the `~/.bashrc` having this...

# Make Bash append rather than overwrite the history on disk:
shopt -s histappend
# A new shell gets the history lines from all previous shells
PROMPT_COMMAND='history -a'
# Don't put duplicate lines in the history.
export HISTCONTROL=ignoredups
```

- Gym!
  - Volleyball.

# March 4 2020

- How do you check permissions on files in `Linux`?
  - `ls -al`
- What is `Netty`?
  - A non-blocking I/O client-server framework for the development of Java network applications.
- What is a `Socket`?
  - A socket is one end-point of a two-way communication link between two programs running on the network.
- Non-taxable wages include insurance.
- TSP SAVINGS + ROTH DED = TSP BASIC + TSP MATCHING.
- What is a server?
  - A computer that is on the internet.
- What is the internet?
  - A collection of many servers.
- What is a client?
  - The software that runs on the user's computer that communicates with the server.
- What are client-side operations?
  - Things that can be done on the user's side without much communication.
  - It's like building up something then sending it to the server in a nice package so it's only 1 call.
- What are server-side operations?
  - Things that require heavy amount of resources and space that the server performs.
  - Also handles security issues.
    - I can't just look at someone's profile if I'm not friend's with them, so the server places security.
- What is rendering?
  - In this context, a combination of data from the server with the client to be displayed.
- Key thing is to download aesthetics once, data endlessly.
- Gym!
  - Chest and triceps.
  - Volleyball.
    - Vibes felt off today, unsure why.

# March 3 2020

- Connecting backend to frontend is difficult.
- What is `ACK`?
  - A signal that is passed between communicating computers to signify acknowledgement, or receipt of message.
- Gym!
  - Back and biceps.

# March 2 2020

- Robinhood sadly down for black monday.
- How do you rename files in `Linux` using the terminal?
  - `mv %OLD_FILE_NAME% %NEW_FILE_NAME%`
- Difference between Sockets and WebSockets?
  - WebSockets run from browsers connecting to application server over a protocol similar to HTTP that runs over TCP/IP.
    - Primarily for web apps that require a permanent connection to its server.
  - Sockets run over TCP/IP, but they are not restricted to browsers or HTTP protocol.
    - Could be used to implement any kind of communication.
  - Gym!
    - Volleyball.

# March 1 2020

- Relaxed.
- Organized budget sheet thoroughly and updated it.

# February 29 2020

- It's a leap year!
- Made some more keys for brother's house.
- Car!
  - Changed oil.

# February 28 2020

- Dentist!
  - Fixed my cavities and teeth cleaning.

# February 27 2020

- Developing database designs before creating the database itself is incredibly helpful.

# February 26 2020

- What is destructing? (Examples in `ReactJS`)

```js
// Imagine you have a person object with the following properties.
const person = {
  firstName: "Lindsay",
  lastName: "Criswell",
  city: "NYC",
};

// To obtain each property individually.
console.log(person.firstName);
console.log(person.lastName);
console.log(person.city);

// Destructuring lets us streamline this code.
const { firstName, lastName, city } = person;

// Which is equivalent to.
const firstName = person.firstName;
const lastName = person.lastName;
const city = person.city;

// So now we can access the properties without the `person` prefix.
console.log(firstName); // Lindsay
console.log(lastName); // Criswell
console.log(city); // NYC

// First level with props.
const Attraction = (props) => {
  return (
    <div auth={props.auth} key={props.attraction.id}>
      <Link
        auth={props.auth.token}
        to={`/attractions/${props.attraction.url_name}`}
        key={props.attraction.id}
      >
        <img alt={props.attraction.name} src={props.attraction.image_url} />
        <h1>{props.attraction.name}</h1>
      </Link>
      <StarRatings rating={props.attraction.average_rating} />
    </div>
  );
};

// Second level without props.
const Attraction = ({ auth, attraction }) => {
  return (
    <div auth={auth} key={attraction.id}>
      <Link
        token={auth.token}
        to={`/attractions/${attraction.url_name}`}
        key={attraction.id}
      >
        <img alt={attraction.name} src={attraction.image_url} />
        <h1>{attraction.name}</h1>
      </Link>
      <StarRatings rating={attraction.average_rating} />
    </div>
  );
};

// Third level destructuring the destruction.
const Attraction = ({
  // `auth` and `auth: { token }` gives access to both the whole `auth` object and its `token`.
  // So if you need to pass down more than just the `token`, this is what is needed.
  auth,
  auth: { token },
  attraction: { id, url_name, name, image_url, average_rating },
}) => {
  return (
    <div auth={auth} key={id}>
      <Link token={token} to={`/attractions/${url_name}`} key={id}>
        <img alt={name} src={image_url} />
        <h1>{name}</h1>
      </Link>
      <StarRatings rating={average_rating} />
    </div>
  );
};
```

- What does `map`, `filter`, and `reduce` do?

```js
// Maps an action to the data and returns the results.
map([🌽, 🐮, 🐔], cook) => [🍿, 🍔, 🍳]

// Filters the data with a condition.
filter([🍿, 🍔, 🍳], isVegetarian) => [🍿, 🍳]

// Reduces the data to an accumulated result.
reduce([🍿, 🍳], eat) => 💩
```

- What is the difference between `React Hooks` and `React Context API`?
  - `React Hooks` allows you to use local state inside of function components.
  - `React Context API` allows you to share state with other components.
- How to `git pull` multiple repositories at once? (Still need fixing of checkout branch)
  - `find . -mindepth 1 -maxdepth 1 -type d -print -exec git -C {} pull \;`
  - Made a shortcut called `git-pull-all` by doing so:

```bash
# Go to home directory, show hidden files, and go into `.bashrc`.

# ` git-pull-all`
alias git-pull-all="find . -mindepth 1 -maxdepth 1 -type d -print -exec git -C {} pull \;"
```

# February 25 2020

- What are some `MongoDB` commands?
  - Make sure the to start the `MongoDB` service before activating `MongoDB` command line.
    - `sudo service mongodb start`, `mongo`
  - Shows databases that are present in `MongoDB`.
    - `show dbs`
  - To create a new database or switch database.
    - `use %DATABASE_NAME%`
  - To check what database you're in.
    - `db`
  - To add a collection to the database you're in.
    - `db.%COLLECTION_NAME%.insert({"name" : "AC"})`
  - To show all collections in all databases.
    - `show collections`
  - To show all the documents in the collection.
    - `db.%COLLECTION_NAME%.find()`
  - To show a specific document in a collection, specify a key value pair.
    - `db.%COLLECTION_NAME%.find({%KEY%: "%VALUE%"})`
  - To show a document in a collection in a pretty style.
    - `db.%COLLECTION_NAME%.find({%KEY%: "%VALUE%"}).pretty()`
- How do you `scp` a file with spaces within?
  - `scp ac@localmachine:~/'Front-End\ Initial\ Software\ Design\ Diagram.odg' ~/`
- Gym!
  - Back and biceps.

# February 24 2020

- Learned about candles.
  - Green means that the overall stock increased in price from open to close.
  - Red means the overall stock decreased in price from open to close.
  - The wicks represent highest and lowest price from open to close.
  - Doji candles mean that the stock is static though may have had changes, open to close is still the same.
- What are the database concepts from tabular (relational) databases to `MongoDB` (respectively)?
  - Database is a Database.
  - Table is a Collection.
  - Row is a Document.
  - Index is an Index.
  - Join is a \$lookup.
  - Foreign Key is a Reference.
- What is `BSON`?
  - A binary format for `JSON` files.
- Gym!
  - Volleyball.

# February 23 2020

- Relaxed.

# February 22 2020

- Went to SDSU VSA Film Festival.
- Supported my friends.

# February 21 2020

- Need to get familiar with `MongoDB` and connecting to the back-end in general.
- Gym!
  - Legs and shoulders.

# February 20 2020

- What is `Maven`?
  - A software project management and comprehension tool.
  - Similar to `npm`.
- What is `IntelliJ IDEA`?
  - An integrated development environment written in Java.
  - Similar to `Visual Studio Code`.

# February 19 2020

- How to find out who are the super users on a system?
  - `grep '^sudo:.*$' /etc/group | cut -d: -f4`
- How to check privileges of a user?
  - `sudo -l -U %USERNAME%`
- How to unmodify a file that's modified in `Git`?
  - `git checkout -- %FILE_NAME%`
- How to select files in another branch that you want in your branch?
  - Be in your branch where you want the changes.
  - `git checkout --patch %OTHER_BRANCH% %FILE_NAME%`
  - Remove `--patch` if the files you want are new to your branch.
- Learning `vim`. Yikes.
- Gym!
  - Chest and triceps.
  - Volleyball.

# February 18 2020

- Big day today at work.
- Learning about Docker.
  - Install an OS essentially in a container with the needed packages within `dockerfile`.
- Gym!
  - Back and biceps.

# February 17 2020

- Ate out at Buca Di Beppo with my friends!
- Stardew Valley intimacy.

# February 16 2020

- Photography!
  - Shot for Super Potion at San Diego City College.

# February 15 2020

- Met with my friend who went to China.
- Met with my tall friend who plays basketball.
- Gym!
  - Legs and shoulders.
  - Volleyball.

# February 14 2020

- ?

# February 13 2020

- Long day of meetings.

# February 12 2020

- Gym!
  - Chest and triceps.
  - Volleyball.

# February 11 2020

- Presented my front-end development research with flying colors.
- Gym!
  - Back and biceps.

# February 10 2020

- Why involve the development team in UX research?
  - The whole team can witness the users use a product.
  - Realize they themselves aren't users, but the users are the users.
- Gym!
  - Volleyball.

# February 9 2020

- Met with a creative friend.

# February 8 2020

- Gym!
  - Volleyball.
- Relaxed.

# February 7 2020

- Office was pretty empty.
- Gym!
  - Leg and shoulders.
  - Volleyball.

# February 6 2020

- STEM Research Fair!

# February 5 2020

- Make sure to build the application before testing.
- What is the difference between `HTTP` and `WebSockets`?
  - `HTTP` is a single call between server and client, like a call to an API.
  - `WebSockets` is a call that's kept alive between server and client.
- Gym!
  - Volleyball.

# February 4 2020

- What is `Webpack`?
  - An open-source JavaScript module bundler that takes modules with dependencies and generates static assets representing those modules.
  - If you have 5 `.css` files, `Webpack` transforms them into 1 `.css` to alleviate call noise.
- How to check if a package is installed globally?
  - `npm list -g`
  - `npm list -g %PACKAGE_NAME%`
- Gym!
  - Back and biceps.

# February 3 2020

- Gym!
  - Volleyball.

# February 2 2020

- Superbowl!
  - Kansas City Chiefs won against the San Francisco 49ers.

# February 1 2020

- Gym!
  - Volleyball.
- Cleaned the car.

# January 31 2020

- Commissioned artist for her time and received the product.
- Gym!
  - Leg and shoulders.
  - Volleyball.

# January 30 2020

- UI/UX meeting.
  - It's about efficiency and ease of use rather than prettiness.

# January 29 2020

- Embedding VS Referencing in database design?
  - Embedded should be used when:
    - Child data "belongs" to parent data (1-to-1).
    - Sub-documents are small in size.
    - Hierarchical structures.
  - Referencing should be used when:
    - Many-to-many relationships.
    - Sub-documents that continuously increase in size.
    - Large (16MB) sub-document information.
  - Cautions with embedding!
    - With properties that grow, unnecessary data could be sent with each query.
      - When scrolling on social media, we just want 10 posts at a time, not all the posts.
    - Many-to-many relationships can get messy.
  - Cautions with references!
    - References requires queries for each individual document for each individual document: O(n2)
    - If only using references, relational database may be better.
  - How to pick what to utilize?
    - Depends on how much you use a specific thing.
    - If it's static and/or used a lot, embedded is best.
    - If it's dynamic and/or used less, references is best.

```
// Example 1.

// Embedded.
{
  blog: "This is a blog."
  posts: [
    {
      title: "Hello!",
      content: "Lorum ipsum.",
      comments: [{/*...*/}]
    },
    {
      title: "Hello!",
      content: "Lorum ipsum.",
      comments: [{/*...*/}]
    },
  ]
}

// Referenced.
{
  blog: "This is a blog."
  posts: [ "someid1", "someid2" ]
}

posts: [
  {
    id: "someid1"
    title: "Hello!",
    content: "Lorum ipsum.",
    comments: [{/*...*/}]
  },
  {
    id: "someid2"
    title: "Hello!",
    content: "Lorum ipsum.",
    comments: [{/*...*/}]
  },
]

// Example 2.

// Embedded.
// We don't always need to call the `orderHistory`.
{
  username: "ac",
  address: {
    line1: "123 Main St.",
    line2: null,
    city: "Corona",
    state: "CO",
    zip: 12345
  }
  cart: {
    items: [ { id: "someid" , id: "someid", etc. }]
    status: "Active"
  },
  orderHistory: [
    {
      items: [ { id: "someid" , id: "someid", etc. }],
      status: "Paid"
    },
    {
      items: [ { id: "someid" , id: "someid", etc. }],
      status: "Paid"
    },
  ]
}

// Referenced.
// Best to have the `cart` right there instead of searching by ID to see what's inside.
{
  username: "ac",
  address: {
    line1: "123 Main St.",
    line2: null,
    city: "Corona",
    state: "CO",
    zip: 12345
  }
  cart: { id: "someid" },
  orderHistory: [
    { id: "someid" },
    { id: "someid" },
    { etc. }
  ]
}

// Both!
// Best of both worlds.
{
  username: "ac",
  address: {
    line1: "123 Main St.",
    line2: null,
    city: "Corona",
    state: "CO",
    zip: 12345
  }
  cart: {
    items: [ { id: "someid" , id: "someid", etc. }]
    status: "Active"
  },
  orderHistory: [
    { id: "someid" },
    { id: "someid" },
    { etc. }
  ]
}
```

- What does `stat` do in `Linux`?
  - Prints information about given files, notably time stamps.
- Gym!
  - Volleyball.

# January 28 2020

- What's the difference between `state` and `props` in `React`?
  - `state` is managed within the component.
  - `props` is passed to the component.
- A bunch of components in `React` together create a?
  - Template, container.
- How do you perform a right-click in `Spectron`?
  - Must install `spectron-keys` library first.

```
const spectronKeys = require("spectron-keys");

it("Right click on item", async () => {
  await app.client
    .click("the button with the text")
    .pause(1000)
    .keys(spectronKeys.mapAccelerator("Shift+F10"))
    .pause(1000)
    .click("the button with the text, but it right clicks")
    .pause(3000)
    .keys(spectronKeys.mapAccelerator("Shift"));
});
```

- Gym!
  - Back and biceps.

# January 27 2020

- What does `mutt` do in `Linux`?
  - A command line based email client.
- What kind of file structures are there?
  - By features or routes.
  - By file type.
  - Rule of thumb is that:
    - Avoid too much nesting.
    - Don't overthink it.
    - Filenames should be lowercase due to compatibility issues.

```
// By features or routes.
common/
  Avatar.js;
  Avatar.css;
  APIUtils.js;
  APIUtils.test.js;
feed/
  index.js;
  Feed.js;
  Feed.css;
  FeedStory.js;
  FeedStory.test.js;
  FeedAPI.js;
  profile / index.js;
  Profile.js;
  ProfileHeader.js;
  ProfileHeader.css;
  ProfileAPI.js;

// By file type.
api/
  APIUtils.js;
  APIUtils.test.js;
  ProfileAPI.js;
  UserAPI.js;
components/
  Avatar.js;
  Avatar.css;
  Feed.js;
  Feed.css;
  FeedStory.js;
  FeedStory.test.js;
  Profile.js;
  ProfileHeader.js;
  ProfileHeader.css;

// Opinionated.
node_modules/
public/
  favicon.ico
  index.html
  manifest.json
src/
  components/
    app/
      app.css
      app.js
    text-box-button/
      text-box-button.css
      text-box-button.js
  images/
    dog.jpg
  index.css
  index.js
test/
  app.test.js
  text-box-button.test.js
.gitignore
package.json

// If `test/` could be implemented.
node_modules/
public/
  favicon.ico
  index.html
  manifest.json
src/
  components/
    app/
      app.css
      app.js
      app.test.js
    text-box-button/
      text-box-button.css
      text-box-button.js
      text-box-button.test.js
  images/
    dog.jpg
  index.css
  index.js
.gitignore
package.json
```

- What is `useRef()` in `React`?
  - Uses a references to an `HTML` component in a `.js` file.

```js
function App() {
  const todoNameRef = useRef();

  function handleAddTodo(e) {
    const name = todoNameRef.current.value;
    console.log(name)
  }

  return(
    <div>
      <input ref = {todoNameRef} type "text" />
    </div>
  )
}
```

- Gym!
  - Volleyball.

# January 26 2020

- Cut hair.
- Relaxed.
- Photography!
  - Edited photos.

# January 25 2020

- Gym!
  - Volleyball.
- Tet festival.
- Gun range.
- Axe throwing.

# January 24 2020

- What does `umask` do in `Linux`? (There's a lot of info on this: https://en.wikipedia.org/wiki/Umask)
  - Determines the settings of a mask that controls how file permissions are set for newly created files.

```bash
$ umask 007    # set the mask to 007
$ umask        # display the mask (in octal)
0007           #   0 - special permissions (setuid | setgid | sticky )
               #   0 - (u)ser/owner part of mask
               #   0 - (g)roup part of mask
               #   7 - (o)thers/not-in-group part of mask
$ umask -S     # display the mask symbolically
u=rwx,g=rwx,o=
```

- What do the octal codes mean in `umask`?
  - `0`
    - Any permission may be set (read, write, execute).
  - `1`
    - Setting of execute permission is prohibited (read and write).
  - `2`
    - Setting of write permission is prohibited (read and execute).
  - `3`
    - Setting of write and execute permission is prohibited (read only).
  - `4`
    - Setting of read permission is prohibited (write and execute).
  - `5`
    - Setting of read and execute permission is prohibited (write only).
  - `6`
    - Setting of read and write permission is prohibited (execute only).
  - `7`
    - All permissions are prohibited from being set (no permissions).
- What does `cp` do in `Linux`?
  - Copies files or directories.
  - Also know as "copy".
  - `cp %I_WANT_TO_COPY_YOU_FILES% %DESTINATION_AREA%`
  - `cp README.md ~/`
- What is `Gitlab`?
  - A web-based DevOps life cycle tool that provides a `Git`-repository manager providing wiki, issue-tracking and CI/CD pipeline features, using an open source license.
- What is `Portainer`?
  - A lightweight management UI which allows easy to manage software containers.
- What is `GanttLab Live`?
  - A tool to master time and deadlines that works with `GitLab` and `Github`.
- What is `Nexus Repository`?
  - A beacon for components, binaries, build artifacts, and distribution center for parts and containers to developers.
- What is `Jenkins`?
  - A free and open source automation server.
- What is `SonarQube`?
  - An open source platform for continuous inspection of code quality to perform automatic reviews with static analysis of code to detect bugs, code smells, and security vulnerabilities on 20+ programming languages.
- What is `Grafana`?
  - A open source analytics and monitoring solution for every database.
- What is `Prometheus`?
  - Prometheus is a free software application used for event monitoring and alerting.
- How to extract a `.tar.gz` file?
  - `gunzip %FILE%.tar.gz`
  - `tar -xvf %FILE%.tar`
- Gym!
  - Legs and shoulders.
  - Volleyball.

# January 23 2020

- Always do `.gitignore` before making anything in the directory!

# January 22 2020

- What does `ssh` do in `Linux`?
  - Gives a secure way to access a computer over an unsecured network.
  - Also known as "secure shell" or "secure socket shell".
- What does `scp` do in `Linux`?
  - Allows files to be copied to, from, or between different hosts.
  - Also known as "secure copy".
  - `scp ac@starkiller:~/%FILE_NAME% .`
- How do you remove a file in `Linux`?
  - `rm`
- How do you remove a directory in `Linux`?
  - `rmdir`
- What's the difference between `.zip`, `.tar.xz`, and `.7z`?
  - `.zip` compatible with all operating systems.
  - `.tar.xz` smaller archives but `Linux` and `Mac` only.
  - `.7z` smaller archives but must be installed on `Windows` and `Mac`.
- Gym!
  - Chest and triceps.
  - Volleyball.

# January 21 2020

- What are documentation tools?
  - Documentation.js.
  - JSDoc.
  - Natural Docs.
- Difference between installing local and global?
  - Install a module locally if you're going to require() it.
  - Install a module globally if you're going to run it on the command line.
- Gym!
  - Back and biceps.

# January 20 2020

- Martin Luther King Jr. Day.

# January 19 2020

- Ikea.

# January 18 2020

- Movie!
  - Weathering with you.

# January 17 2020

- Movie!
  - Star Wars: The Rise of Skywalker.

# January 16 2020

- What is `Karma`?
  - A testing framework that runs on multiple browsers.
- What is `Picture-In-Picture`?
  - A feature originated from television receivers where it displays a smaller video program alongside the main video program.
- Firefox and Chrome both have Picture-In-Picture options.
- How to remove terminal prompt?
  - `export PS1='>'`
  - Changes the terminal prompt to `>`.
- How to increase a `VirtualBox` disk size?
  - Make sure virtual machines are off.
  - Highlight virtual machine in `VirtualBox`.
  - Go to settings.
  - Go to storage.
  - Click the controller SATA under storage devices.
    - Usually the VDI file.
  - Make sure the information for:
    - Type (format) is VDI or VHD.
    - Details is dynamically allocated.
  - Copy the address location.
  - Open terminal.
  - Change location to the address location, but one folder up.
  - To check contents use `ls -la`.
  - Make a back-up via `cp %FILE_NAME%.VDI %BACK_UP_FILE_NAME%.VDI`.
  - Resize the file `vboxmanage modifyhd %FILE_NAME%.VDI --resize 100000`
    - 100000 is approximately 100 gigabytes.
  - Highlight virtual machine in `VirtualBox`.
  - Go to settings.
  - Go to storage.
  - Click the controller IDE under storage devices.
    - Usually empty.
  - To the side in attributes, change the optical drive to the OS system you used to boot up.
  - Click ok.
  - Start up the virtual machine.
  - Open up GParted in the virtual machine.
  - Click the old memory space.
  - Resize to take all unallocated space.
  - Apply operations.
  - Go back to the controller IDE under storage devices.
  - Remove disk from virtual drive.
  - Enjoy!

# January 15 2020

- What does `sudo` do in Linux?
  - Superuser do.
  - Best and safest way to elevate privileges to do something by asking for a password.
- Gym!
  - Chest and triceps.

# January 14 2020

- What is the relationship of `Spectron` to `WebdriverIO` and `Selenium WebDriver`?
  - `Selenium WebDriver` allows developers to write tests that control a web browser so they can test apps from a user's perspective.
  - `WebdriverIO` wraps the `Selenium WebDriver` with a pleasant `JavaScript` API and makes it easy to use from within `Node.js` or an `Electron` application in our case.
  - `Spectron` allows access to `WebdriverIO` with a environment custom-tailored functionality for `Electron` applications.
- What is the primary way to use `Spectron`?
  - Create an `Application` instance.
  - This object includes a number of child objects that allow us to access different parts of the application.
- What are the different parts of `Spectron`?
  - `client`
    - The underlying `WebdriverIO` instance.
  - `electron`
    - `Electron`'s renderer process API.
  - `browserWindow`
    - The currently focused browser window.
  - `webContents`
    - `Electron`'s WebContents API.
  - `mainProcess`
    - Node's process object in the main process.
  - `rendererProcess`
    - Node's process object in the renderer process.
- Is it better to have the front-end and back-end in the same repo or separate repos.
  - Depends.
  - Usually separate repos is desirable due to modularization and scalability.
  - Reasons for same repos is for the engineers to understand the product as a whole.
- How does a standard `Electron` test file look like?

```js
const Application = require("spectron").Application; // `Spectron`'s application driver.
const assert = require("assert"); // `Node.js`'s built in assertion library.
const electronPath = require("electron"); // Locally installed development version of `Electron`.
const path = require("path"); // `Node.js`'s helper utility for working with file paths.

const app = new Application({
  path: electronPath,
  args: [path.join(__dirname, "..")], // Points to root directory of application as a starting point.
});

describe("Application launch", function() {
  this.timeout(10000); // `Mocha`'s default timeout because launching can take a while.

  beforeEach(() => {
    return app.start(); // Starts application before each test.
  });

  afterEach(() => {
    if (app && app.isRunning()) {
      return app.stop(); // Stops the application after each test.
    }
  });

  it("should have 1 window", function() {
    const count = await app.client.getWindowCount();
    return assert.equal(count, 1);
  })
});
```

- What is a callback function?
  - A function where it's accessible by another function.
  - Usually when a certain function is finished, another takes its place.
- Gym!
  - Back and biceps.

# January 13 2020

- What is `Mocha`?
  - JavaScript test framework running on `Node.js` and in the browser.
- What is `Chai`?
  - A BDD/TDD (Behavioral Driven Development/Technical Driven Development) assertion library for `Node.js`.
  - Makes it easy to express and be readable to anyone.
- How to run scripts after one each other in `Linux`?
  - Use `&` between scripts.
- How to run scripts simultaneously in `Linux`?
  - Use `|` between scripts.
- There are different auto-documentation tools that look at the code and create a `HTML` file from it that's fast and easy to access.
- What is a traditional virtualization?
  - Hardware (Server).
  - Operating System.
  - Hypervisor (Translating system for app to OS).
  - Multiple VMS.
- What is a traditional containerization?
  - Hardware (Server).
  - Operating System.
  - Containers.
- What are the differences between VMs VS containers?
  - VMs are not as flexible when utilizing resources on the hardware where containers are flexible and use what it needs, not fixed.
- Why use `Docker`?
  - Makes it easy to develop and deploy apps inside neat containers.
- Instead of controlling 1 container at a time, `Docker Compose` is a tool to use to affect multiple containers at once.

# January 12 2020

- FS Retreat!

# January 11 2020

- FS Retreat!

# January 10 2020

- FS Retreat!

# January 9 2020

- What is `Cucumber`?
  - An open source, multiple language support, that provides BDD tools.
- What is "BDD"?
  - Behavioral Driven Development.
  - Allows for non-technical developers to collaborate more in the development process.

```
Feature: Reset functionality on login page of application.

Scenario: Verification of reset button.
Given... Open the Firefox and launch the application.
When... Enter the Username and Password.
Then... Reset the credential.
```

- What is `Selenium`?
  - Automation browser-based application.
- Electron provide us an easy and fast way to develop native Windows or Mac-OS application.
- React library makes web development more structure and modular by it’s component based approach.
- Combination of Electron and React will be an awesome way to develop desktop application.
- Made a Electron, React, Spectron boilerplate.
  - Needs Jest/Enzyme?

# January 8 2020

- Gym!
  - Legs and shoulders.

# January 7 2020

- Looked up insurance options.
- What is `Electron`?
  - A combination of `Chromium`, `Node.js`, and native APIs such as open file dialogs, notifications, etc.
  - Provides a browser window with customizability as opposed to browsers.
- Gym!
  - Chest and triceps.

# January 6 2020

- Where does one put the `<script>` tag in an `index.html` file?
  - Usually in the `<body>`, towards the very end.
  - This makes sure the DOM is ready to be manipulated before the `JavaScript` goes in.
- What does "DOM" mean?
  - Document Object Model.
  - Treats a `HTML` document as a tree structure.
- Created a password generator in `JavaScript`.
- Gym!
  - Volleyball.

# January 5 2020

- ?

# January 4 2020

- Gym!
  - Back and biceps.
- Watched Japanese wrestling.

# January 3 2020

- ?

# January 2 2020

- Work.
- Fixed all my repos and learned a bunch `JavaScript` related.
- What does it mean to `amend` a commit?
  - To combine the current and previous commit into 1.

# January 1 2020

- Happy new year!
