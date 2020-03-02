# March 3, 2020

- ?

# March 2, 2020

- Robinhood sadly down for black monday.

# March 1, 2020

- Relaxed.
- Organized budget sheet thoroughly and updated it.

# February 29, 2020

- It's a leap year!
- Made some more keys for brother's house.
- Car!
  - Oil change.

# February 28, 2020

- Dentist!
  - Fixed my cavities and teeth cleaning.

# February 27, 2020

- Developing database designs before creating the database itself is incredibly helpful.

# February 26, 2020

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
const Attraction = props => {
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

# February 25, 2020

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

# February 24, 2020

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

# February 23, 2020

- Relaxed.

# February 22, 2020

- Went to SDSU VSA Film Festival.
- Supported my friends.

# February 21, 2020

- Need to get familiar with `MongoDB` and connecting to the back-end in general.
- Gym!
  - Legs and shoulders.

# February 20, 2020

- What is `Maven`?
  - A software project management and comprehension tool.
  - Similar to `npm`.
- What is `IntelliJ IDEA`?
  - An integrated development environment written in Java.
  - Similar to `Visual Studio Code`.

# February 19, 2020

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

# February 18, 2020

- Big day today at work.
- Learning about Docker.
  - Install an OS essentially in a container with the needed packages within `dockerfile`.
- Gym!
  - Back and biceps.

# February 17, 2020

- Ate out at Buca Di Beppo with my friends!
- Stardew Valley intimacy.

# February 16, 2020

- Photography!
  - Shot for Super Potion at San Diego City College.

# February 15, 2020

- Met with my friend who went to China.
- Met with my tall friend who plays basketball.
- Gym!
  - Legs and shoulders.
  - Volleyball.

# February 14, 2020

- ?

# February 13, 2020

- Long day of meetings.

# February 12, 2020

- Gym!
  - Chest and triceps.
  - Volleyball.

# February 11, 2020

- Presented my front-end development research with flying colors.
- Gym!
  - Back and biceps.

# February 10, 2020

- Why involve the development team in UX research?
  - The whole team can witness the users use a product.
  - Realize they themselves aren't users, but the users are the users.
- Gym!
  - Volleyball.

# February 9, 2020

- Met with a creative friend.

# February 8, 2020

- Gym!
  - Volleyball.
- Relaxed.

# February 7, 2020

- Office was pretty empty.
- Gym!
  - Leg and shoulders.
  - Volleyball.

# February 6, 2020

- STEM Research Fair!

# February 5, 2020

- Make sure to build the application before testing.
- What is the difference between `HTTP` and `WebSockets`?
  - `HTTP` is a single call between server and client, like a call to an API.
  - `WebSockets` is a call that's kept alive between server and client.
- Gym!
  - Volleyball.

# February 4, 2020

- What is `Webpack`?
  - An open-source JavaScript module bundler that takes modules with dependencies and generates static assets representing those modules.
  - If you have 5 `.css` files, `Webpack` transforms them into 1 `.css` to alleviate call noise.
- How to check if a package is installed globally?
  - `npm list -g`
  - `npm list -g %PACKAGE_NAME%`
- Gym!
  - Back and biceps.

# February 3, 2020

- Gym!
  - Volleyball.

# February 2, 2020

- Superbowl!
  - Kansas City Chiefs won against the San Francisco 49ers.

# February 1, 2020

- Gym!
  - Volleyball.
- Cleaned the car.

# January 31, 2020

- Commissioned artist for her time and received the product.
- Gym!
  - Leg and shoulders.
  - Volleyball.

# January 30, 2020

- UI/UX meeting.
  - It's about efficiency and ease of use rather than prettiness.

# January 29, 2020

- Embedding VS. Referencing in database design?
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

# January 28, 2020

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

# January 27, 2020

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

# January 26, 2020

- Cut hair.
- Relaxed.
- Photography!
  - Edited photos.

# January 25, 2020

- Gym!
  - Volleyball.
- Tet festival.
- Gun range.
- Axe throwing.

# January 24, 2020

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

# January 23, 2020

- Always do `.gitignore` before making anything in the directory!

# January 22, 2020

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

# January 21, 2020

- What are documentation tools?
  - Documentation.js.
  - JSDoc.
  - Natural Docs.
- Difference between installing local and global?
  - Install a module locally if you're going to require() it.
  - Install a module globally if you're going to run it on the command line.
- Gym!
  - Back and biceps.

# January 20, 2020

- Martin Luther King Jr. Day.

# January 19, 2020

- Ikea.

# January 18, 2020

- Movie!
  - Weathering with you.

# January 17, 2020

- Movie!
  - Star Wars: The Rise of Skywalker.

# January 16, 2020

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

# January 15, 2020

- What does `sudo` do in Linux?
  - Superuser do.
  - Best and safest way to elevate privileges to do something by asking for a password.
- Gym!
  - Chest and triceps.

# January 14, 2020

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

# January 13, 2020

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
- What are the differences between VMs VS. containers?
  - VMs are not as flexible when utilizing resources on the hardware where containers are flexible and use what it needs, not fixed.
- Why use `Docker`?
  - Makes it easy to develop and deploy apps inside neat containers.
- Instead of controlling 1 container at a time, `Docker Compose` is a tool to use to affect multiple containers at once.

# January 12, 2020

- FS Retreat!

# January 11, 2020

- FS Retreat!

# January 10, 2020

- FS Retreat!

# January 9, 2020

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

# January 8, 2020

- Gym!
  - Legs and shoulders.

# January 7, 2020

- Looked up insurance options.
- What is `Electron`?
  - A combination of `Chromium`, `Node.js`, and native APIs such as open file dialogs, notifications, etc.
  - Provides a browser window with customizability as opposed to browsers.
- Gym!
  - Chest and triceps.

# January 6, 2020

- Where does one put the `<script>` tag in an `index.html` file?
  - Usually in the `<body>`, towards the very end.
  - This makes sure the DOM is ready to be manipulated before the `JavaScript` goes in.
- What does "DOM" mean?
  - Document Object Model.
  - Treats a `HTML` document as a tree structure.
- Created a password generator in `JavaScript`.
- Gym!
  - Volleyball.

# January 5, 2020

- ?

# January 4, 2020

- Gym!
  - Back and biceps.
- Watched Japanese wrestling.

# January 3, 2020

- ?

# January 2, 2020

- Work.
- Fixed all my repos and learned a bunch `JavaScript` related.
- What does it mean to `amend` a commit?
  - To combine the current and previous commit into 1.

# January 1, 2020

- Happy new year!
