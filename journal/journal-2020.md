# November 5 2020

- Great sprint, installer works and was able to push out some last minute stuff with plenty of time.
- Gym!
  - Volleyball.

# November 4 2020

- Be better.
- Gym!
  - Flex.

# November 3 2020

- What defines art?
  - Display.
    - To put your art in the open.
  - Intention.
    - To create something meaningful for the purpose of aesthetic.
  - Reception.
    - Someone else has their own interpretation.
- When pushing builds to `Nexus`, instead of specifying a `.npmignore`, best to use the `files` attribute to specify which files are wanted in the final build.

```js
"files": [
  "dist/",
  "%OTHER-FILE%"
]
```

- To find out what files `npm` will publish into the tarball without actually publishing.
  - `npm pack && tar -xvzf *.tgz && rm -rf package *.tgz`
- If a directory is present, remove it, else do nothing. (No error messages)
  - `rm -rf %DIRECTORY%`
- How to release a software candidate for `Nexus` through `Jenkins`?

```
export DISPLAY=:1
rm -rf dist/
npm install
npm run test:coverage
npm run sonar
npm run build
npm run electron-builder
npm set %URL-CREDENTIALS%
npm publish --registry%REGISTRY%
```

- Gym!
  - Volleyball.

# November 2 2020

- Need to clean the car.
- Gym!
  - Flex.

# November 1 2020

- Happy birthday old man.
- Gym!
  - Flex.

# October 31 2020

- Happy halloween! (happyhalloween.netlify.app)
- Gym!
  - Volleyball.

# October 30 2020

- Got back to work feeling refreshed!
- Gym!
  - Flex.

# October 29 2020

- Gym!
  - Volleyball.

# October 28 2020

- How to do versioning?
  - `X.Y.Z` format which each character is something specific.
    - `X` = production build.
    - `Y` = sprint number.
    - `Z` = each merge.
- In `React`, how do you show an image?
  - This deals with webpack.
  - Note that assets outside of the `src/` are not supported.
  - `<img src={require("%PATH-TO-THE-IMAGE%")} alt="something"/>
- How do I transfer installed `Linux` packages and settings from one distro to another?
  
```sh
sudo apt-get install apt-clone
apt-clone clone %PACKAGE%
# Copy %PACKAGE%.apt-clone.tar.gz to the new machine and run.
sudo apt-get install apt-clone
sudo apt-clone restore %PACKAGE%.apt-clone.tar.gz
```

- Today I learned "Waterfalls" was made by TLC, the group that preformed "No Scrubs".
- Signs of a toxic friend:
  - They mostly talk about themselves.
  - They aren’t really happy for your success.
  - They tend to ignore your feelings and problems.
  - They pressure you to do things you don’t really want to do.
  - They tend to get mad at you quite easily.
  - You feel stressed and drained after the interaction.
  - They are resistant to change.
- Dead by Daylight with the Curry Crew!
- Gym!
  - Flex.

# October 27 2020

- I did it again, towards the end, anxiety riled up.
- Gym!
  - Volleyball.

# October 26 2020

- Gym!
  - Flex.

# October 25 2020

- Great vibes with FS watching Hamilton, cooking KBBQ, cookies, and playing monikers.

# October 24 2020

- Felt groggy, plenty of Genshin Impact.
- Gym!
  - Flex.

# October 23 2020

- Got to hangout with Karasuno, making kare kare, more kbbq, playing monikers, and getting empathetic.
- Gym!
  - Flex.

# October 22 2020

- What are the differences in commands of `locate` and `find`?
  - `locate` is better when you're just trying to find a particular file by name, which you know exists, but you just don't remember where it is exactly.
  - `find` is better when you have a focused area to examine, or when you need any of its many advantages.
- How do you find which people on your connection is `sudo`?
  - `getent group sudo`
- When presenting, explain the topic, what the goal was, timeline, go into the details.
- Gym!
  - Volleyball.

# October 21 2020

- Gym!
  - Flex.

# October 20 2020

- How to search for `Linux` packages in a terminal?
  - `apt search %KEYWORD%`
- Gym!
  - Volleyball.

# October 19 2020

- Gym!
  - Flex.

# October 18 2020

- Self-reflection.
- Gym!
  - Flex.

# October 17 2020

- I'm terrible.
- Gym!
  - Flex.

# October 16 2020

- How to install an extension offline in `Google Chrome`?
  - Install the extension on an online computer to `Google Chrome`.
  - Look for the extension from an upper directory able to see everything ("~" is a safe bet, meaning "home" usually.):
    - `find . -type d -iname %EXTENSION-ID%`
  - Copy that scoped directory to the offline computer.
    - Make sure that the file has a `manifest.json`.
  - On the offline computer now, open up `Google Chrome`.
  - Put in the URL `chrome://extensions`.
  - Turn on `Developer mode` at the top right.
  - Click `Load unpacked` at the top left.
  - Look for the directory of the downloaded extension and install!
- Gym!
  - Flex.

# October 15 2020

- "MAKUAKE" by eill sounds like "Visual Dreams" by SNSD.
- Made this benchmark comparing `Includes vs. IndexOf vs. Filter vs. Find vs. FindIndex vs. Some`: https://www.measurethat.net/Benchmarks/Show/9046/0/includes-vs-indexof-vs-filter-vs-find-vs-findindex-vs-s

```
Includes x 1,987,563 ops/sec ±2.17% (60 runs sampled)
IndexOf x 178,255 ops/sec ±1.08% (64 runs sampled)
Filter x 43,810 ops/sec ±62.73% (20 runs sampled)
Find x 126,352 ops/sec ±57.21% (60 runs sampled)
FindIndex x 281,395 ops/sec ±54.44% (65 runs sampled)
Some x 286,783 ops/sec ±52.20% (64 runs sampled)

Fastest: Includes
Slowest: Filter, IndexOf
```

- Typography translated as `font-weight` deciphered:

```
100	Thin (Hairline)
200	Extra Light (Ultra Light)
300	Light
400	Normal (Regular)
500	Medium
600	Semi Bold (Demi Bold)
700	Bold
800	Extra Bold (Ultra Bold)
900	Black (Heavy)
950	Extra Black (Ultra Black)
```

- Gym!
  - Volleyball.

# October 14 2020

- "Contained in" is to have almost identical meaning.
- "Revealed by" is to explain further more.
- "Classification by Compilation" is when 2 > unclassified info create classified info.
- Extracting occurs when information is taken directly from an authorized classification guidance source and is stated verbatim in a new or different document.
- Paraphrasing or restating occurs when information is taken from an authorized source and is re-worded in a new or different document.
  - Derivative classifiers must be careful when paraphrasing or restating information to ensure that the classification has not been changed in the process.
- Generating is when information is taken from an authorized source and generated into in another form or medium, such as a video, DVD, or CD.
- Confidentiality from least to greatest.
  - Unclassified
  - Confidential
  - Secret
  - Top Secret
- What is deferential backshift?
  - "I was wondering..."
  - Remote potential in social terms creates an impression of less imposition and hence greater politeness.
  - Alternatives include:
    - "Would it be possible.."
    - "Do you think you..."
    - "I would be most grateful if..."
- How to change download place of `npm` packages? (I.E. defaults to internet, but what if wanted somewhere else?)
  - Create a `.npmrc` file and put specific locations.
  - `PROXY=https://localhost:9999/HERE`
- How to check the `package.json` to make sure it's on par on latest versions of dependencies?
  - `npm install -g npm-check-update`
  - `ncu` will let the user know about updates, but not make the updates.
  - `ncu -u` will update the `package.json` with the updates, then recommended to follow up with `npm install`.
- Gym!
  - Flex.

# October 13 2020

- :)
- Thank you to female copy of me, Rei Ayanami, and family.
- Gym!
  - Volleyball.

# October 12 2020

- Cleaned up my life.

# October 11 2020

- 15th place out of 16 in League Clash.
- Gym!
  - Flex.

# October 10 2020

- 8th place out of 16 in League Clash.

# October 9 2020

- Felt empty.

# October 8 2020

- Slept really early yesterday.
- In `Visual Studio Code`, what do the markers next to the files mean?
  - `A`: Added (This is a new file that has been added to the repository)
  - `M`: Modified (An existing file has been changed)
  - `D`: Deleted (a file has been deleted)
  - `U`: Untracked (The file is new or has been changed but has not been added to the repository yet)
  - `C`: Conflict (There is a conflict in the file)
  - `R`: Renamed (The file has been renamed)`

# October 7 2020

- Gym!
  - Flex.

# October 6 2020

- Gym!
  - Volleyball.

# October 5 2020

- Need to work on clearance.
- "Honesty tempered by love is a great thing."
- Gym!
  - Flex.

# October 4 2020

- Hung out with FS, I should be happy, but I'm sad.
- Gym!
  - Flex.

# October 3 2020

- ???

# October 2 2020

- Good day at work.

# October 1 2020

- In `Mac`, how to fix terminal issue that displays `zsh compinit: insecure directories, run compaudit for list.`?

```sh
# Lists unsecure directories.
compaudit

# To fix the error.
sudo chmod -R 755 %TARGET-DIRECTORY%
```

- Gym!
  - Volleyball.

# September 30 2020

- Felt groggy.

# September 29 2020

- Needed to see someone.
- Gym!
  - Volleyball.

# September 28 2020

- Input validation! Wow!
- Darn those `React` input validation libraries for being out of date kind of.
- How to install `Node.js` and `npm` into `Linux`!
  - `curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -`
  - `sudo apt install nodejs`
  - Verify they're installed.
  - `node --version`
  - `npm --version`
- Gym!
  - Flex.

# September 27 2020

- Went to the San Diego Zoo and Buca Di Beppo with the Yakuza.
- Streamed with positive people and felt happy about it.
- Created an "anime" Spotify playlist!

# September 26 2020

- Went to Mira Mesa to try out volleyball there and it feels expert level.
- Hung out with Karasuno playing Mahjong.
- Gym!
  - Volleyball.

# September 25 2020

- Gym!
  - Volleyball.

# September 24 2020

- Made great progress for work!
- Gym!
  - Volleyball.

# September 23 2020

- Handoo BBQ with Taeyang, Jisun, and Scantron.

# September 22 2020

- In `React`, how to add to an array using `React Hooks`?
  - `searches.push(query)`?
    - Doesn't ever get "set" with the `setSearches` hook.
  - `setSearches(searches.push(query))`?
    - `.push` returns the length of the array instead of the array itself.
  - `setSearches(searches.concat(query))?
    - Works great since `.concat` creates a new array than an old one.
  - `setSearches([query].concat(searches))`
    - Works great if needing to add to the front of the data structure.
  - `setSearches(searches => searches.concat(query))`
    - Even better since there's a wrapper function.
  - `setSearches(searches => [...searches, query])`
    - Ideal solution.
  - `setSearches(searches => [query, ...searches])`
    - Ideal solution if needing to add to the front of the data structure.
- What's a wrapper function's purpose?
  - To call another function (callback).
  - Think of it as an alarm clock, will call the proper function at the right time.
  - Can not mess a function up (usually), so I can't trust myself to wake myself up, but a wrapper function will be trustworthy to wake me up (alarm clock).
- How to create a `package.json` properly?
  - `npm init`
  - Will prompt for each field that needs input.
- In `Git`, how to change a commit message when already committed?
  - `git commit --amend`

# September 21 2020

- Gym!
  - Flex.

# September 20 2020

- Slept really.
- Gym!
  - Flex.

# September 19 2020

- Spent the day with Rei Ayanami visiting the shop, kpop store, swapmeet, bookoff, hmart, nishiki ramen, and hopefully Super Potion, but time constraints.

# September 18 2020

- ???

# September 17 2020

- Gym!
  - Volleyball.

# September 16 2020

- Gym!
  - Flex.

# September 15 2020

- How to ask a "good" Stack Overflow question?
- How do you answer a Stack Overflow
- Gym!
  - Volleyball.

# September 14 2020

- https://www.youtube.com/watch?v=sjxNTcsquG8
- https://www.psychologytoday.com/us/blog/living-forward/201511/why-ghosting-hurts-so-much
- Finite players play to beat who's around them while infinite players player to beat themselves. (Sounds awkward, but you get it.)
- In `JavaScript`, how to add leading zeroes to a date, specifically if the months or days is 1 digit, instead of the organized 2?

```js
var MyDate = new Date();
var MyDateString;

MyDate.setDate(MyDate.getDate() + 20);

MyDateString =
  ("0" + MyDate.getDate()).slice(-2) +
  "/" +
  ("0" + (MyDate.getMonth() + 1)).slice(-2) +
  "/" +
  MyDate.getFullYear();
```

- Gym!
  - Flex.

# September 13 2020

- Hung out with Clarinet and it was surprisingly easy to talk to her.
- Gym!
  - Hiking.
  - Flex.

# September 12 2020

- I spiked the wall so well and Jeff did a great serve to end the game when we were about to lose!
- Gym!
  - Volleyball.

# September 11 2020

- Felt poopy.
- Gym!
  - Flex.

# September 10 2020

- Gym!
  - Volleyball.

# September 9 2020

- Feel like I'm learning stuff, but going nowhere with the code.
- Gym!
  - Flex.

# September 8 2020

- "We always say "I'm here if you need me", assuming they have the courage to even approach you in their time of need."
- In `Git`, how do you delete all local branches except the few that you want to keep?
  - `git branch | grep -v "%BRANCH-TO-KEEP%\|%OTHER-BRANCH-TO-KEEP%" | xargs git branch -D`
- In `React`, how do you fix this error:
  - `Can't perform a React state update on an unmounted component. This is a no-op, but it indicates a memory leak in your application. To fix, cancel all subscriptions and asynchronous tasks in a useEffect cleanup function.`

```js
useEffect(
  (data) => {
    effect;
    return () => {
      cleanup;
    };
  },
  [input]
);
```

- In `React`, what's the difference between `export function` VS. `export default`.
  - Depends if you want to export a single entity VS. multiple entities.

```js
// Default export.
import DefaultExport from "./somewhere";

// Export.
import { export, export2 } from "./somewhere";
```

- Gym!
  - Volleyball.

# September 7 2020

- Fixed a lot of files, need to work on hard drive now.
- Gym!
  - Flex.

# September 6 2020

- Floating in the ocean, got home, shout outs to Apex Predator for taking me home.

# September 5 2020

- Curry Crew stream.

# September 4 2020

- Doozy.
- Need to figure out how `React` works with different pages, possibly using `react-router`.

# September 3 2020

- Gym!
  - Volleyball.

# September 2 2020

- Need to fix budget.
- Should make a Chungha, Red Velvet, Twice playlist.
- Gym!
  - Flex.

# September 1 2020

- In `Material UI`, how do you get the `<Tabs>` indicator line to show up and be a specific color?

```js
// Primarily the "indicatorColor" and "value" is needed.
<Tabs indicatorColor="primary" onChange={handleTabChange} value={tabValue}>
  ...
</Tabs>
```

# August 31 2020

- Gym!
  - Flex.

# August 30 2020

- Worked on car stuff.

# August 29 2020

- Gym!
  - Volleyball.

# August 28 2020

- Went to Ikea and sushi with Rei Ayanami and Tae Yang.

# August 27 2020

- Gym!
  - Volleyball.

# August 26 2020

- Don't eat or drink alcohol before sleeping (2-3 hours), will cause sleep to feel uncomfortable and waking up tired.
- Gym!
  - Flex.

# August 25 2020

- In `bash`, what does `nslookup %COMPUTER-NAME%` do?
  - `nslookup` means "name server lookup".
  - Looks up the server and address names along with non-authoritative names.
- In `Ubuntu`, what do the different colors for files mean when doing `ls` in `bash`?
  - Blue: Directory.
  - Green: Executable or recognized data file.
  - Cyan (Sky Blue): Symbolic link file.
  - Yellow w/ black background: Device.
  - Magenta (Pink): Graphic image file.
  - Red: Archive file.
  - Red w/ black background: Broken link.
- Since schools are moving online, do costs go down?
  - Costs would stay the same as the funds are allocated from physical campus cost to online costs (maintaining users, mangaging databases, working with subscription services, webcams, computers, servers, etc.)
- Gym!
  - Flex.

# August 24 2020

- How do you access a shared folder on a Linux Ubuntu 18.04 VM?
  - `sudo adduser %YOUR-USER% vboxsf`
  - Reboot.
  - If that doesn't work, try `sudo usermod -aG vboxsf $(whoami)`.
- Was able to make an executable!

# August 23 2020

- Hung out unexpectedly and had Taco Stand for the first time as well as Camellia Rd in a while.

# August 22 2020

- Got to see Rei Ayanami and Tae Yang for some KBBQ and run errands.

# August 21 2020

- How should file names be typed?
  - `like-this-no-matter-what-08-21-2020.jpeg`
  - Dashes everywhere for consistency and required for dates as it's the global usage.
  - Google standard.

# August 20 2020

- Virtual machine is back up, made a new one!
- Gym!
  - Volleyball.

# August 19 2020

- Accidentally broke my virtual machine at work and need to restart.
- Gym!
  - Flex.

# August 18 2020

- On `Mac`, what does `drutil tray eject` do?
  - Ejects the cd in the drive "nicely", if it fails to respond physically.

# August 17 2020

- Learning how to create a front-end executable.
- Gym!
  - Flex.

# August 16 2020

- Relaxed.

# August 15 2020

- Relaxed.

# August 14 2020

- Met a friend named Nobu and they're moving to Maryland for work.

# August 13 2020

- Gym!
  - Volleyball.

# August 12 2020

- How to install a font into an application?

```sh
# Command.
npm install typeface-roboto --save

# Index.js.
import 'typeface-roboto';
```

- Difference between "disc" and "disk"?
  - Not much of a difference, debatable.
  - Disc for circular objects.
  - Disk for angular objects.
- Favorite terminal editor?
  - There's several out there including `emacs`, `nano`, `vim`, but favorite one is `gedit` since it pops out a text editor to what I'm used to.

# August 11 2020

- In `React`, how do you have a child component change the state of a parent component?

```js
// Parent.
import React, { useState } from "react";
import Child from "./Child";

export default function App() {
  const [nameState, setNameState] = useState("AC");

  return (
    <div className="parent">
      <h1>Hello, my name is {nameState}</h1>
      <Child onChange={(value) => setNameState(value)} />
    </div>
  );
}

// Child.
import React from "react";

const Child = props => {
  turn (
    <div>
    <input type="text" placeholder="Update name..." onChange={(event) => props.onChange(event.target.value)}>
    </div>
  )
}
```

- How to add spacing between items in the front-end?
  - `&nbsp;` (It should have a semi-colon on the end) is an entity for a non-breaking space.
  - `margin` can add spacing between two objects by adding margin on its sides.
- Gym!
  - Flex.

# August 10 2020

- In `Material UI`, what is the difference between styled components `props` and `CSS` stylesheets?
  - Styled components `props` pros.
    - No global selectors, no worries about overriding selectors.
    - Consistency.
    - `Sass` syntax out of the box.
    - Themes, making a parent's style accessible to children.
    - Easy to use props with different definitions such as `small`, `medium`, and `large` rather than hard-coding each.
  - Styled components `props` cons.
    - Learning curve.
    - Integration with legacy `CSS`.
    - Potentially a "fad".
    - Performance.
  - `CSS` stylesheets pros.
    - Unopinionated and universal, the same old.
    - Caching and performance.
    - Quickly iterate a new design by replacing the respective stylesheet with a new one.
    - Ease of use.
    - Frameworks which provide tutorials and foundation.
  - `CSS stylesheets cons.
    - Readability.
    - Legacy CSS can live forever and may be difficult to deal with in the future.
    - Global scope and specificity.
    - No true dynamic styling.
    - Maintaining consistency.
- When to use "&" versus "and"?
  - Only use "&" when comparing proper nouns or things that are a "pair".
    - "Research & Design", "Web & Mobile", "AT&T".
  - Otherwise "and" is the default case.
    - "Family and friends", "small, medium, and large".
- In `React`, how is `clsx` used?
  - `clsx` is generally used to conditionally apply a given `className`.

```js
import clsx from "clsx";

const [open, setOpen] = useState(true);
const classes = useStyles();

const handleDrawerOpen = () => {
  setOpen(true);
};

const handleDrawerClose = () => {
  setOpen(false);
};

<Drawer
  variant="permanent"
  classes={{
    // Always show drawer, unless open changes to false, then close the drawer.
    paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose),
  }}
  open={open}
>
  <div className={classes.toolbarIcon}>
    <IconButton onClick={handleDrawerClose}>
      <ChevronLeftIcon />
    </IconButton>
  </div>
  <Divider />
  <List>{mainListItems}</List>
  <Divider />
  <List>{secondaryListItems}</List>
</Drawer>;
```

- Gym!
  - Flex.

# August 9 2020

- League of Legends Clash Tournament, got 2nd place out of 8 teams.
  - Zac is good if choosing not to skirmish before level 9 otherwise it's hard to land skillshots and get in range.
  - Great skirmishers early?
    - Elise.
    - Jarvan IV.
    - Kayn.
    - Lee Sin.
    - Nocturne.
  - Great skirmishers late?
    - Amumu.
    - Kayn.
    - Zac.
  - Felt like I let me team down by dying a lot for objectives and losing fights.
- Gym!
  - Flex.

# August 8 2020

- Gym!
  - Flex.

# August 7 2020

- Slowly becoming a `Material UI` veteran.

# August 6 2020

- Don't be scared to look for opportunities!

# August 5 2020

- In `CSS`, what is `rem`?
  - "The root element's font-size" or "root em" for short or even shorter `rem`.
  - Say the base font size is `16px`, `1.25rem` === `20px`. (16 \* 1.25 = 20)
- In `Android`, what is `dp`?
  - Density independent pixels (dp) is the `Android` equivalent to `CSS` `px`.
- Gym!
  - Flex.

# August 4 2020

- What does the `static` keyword do?
  - Static methods are called directly on the class without creating an instance/object of the class.
- Why would someone want to use the `static` keyword?
  - "Does it make sense to call this method, even if no object has been constructed yet?"
    - If so, it should definitely be static.
  - An example would be if there was a car class with a `static` method called `convertMpgToKpl()` which could be used without creating a car, it could be done outside of it.
  - Usually utility classes will encompass these `static` methods due to their scope and flexibility for all other files to use.
- How can the size of files and directories in `Linux` be seen within the terminal?

```sh
# ls = files
# du = directories

ls -l $FILENAME% # Displays size of the specified file.
ls -l *          # Displays size of all the files in the current directory.
ls -al *         # Displays size of all the files including hidden files in the current directory.
ls -al dir/      # Displays size of all the files including hidden files in the 'dir' directory.

du -sh %DIRECTORY-NAME%  # Gives you the summarized (-s) size of the directory in human readable (-h) format.
du -bsh *                # Gives you the apparent (-b) summarized (-s) size of all the files and directories in the current directory in human readable (-h) format.
```

- What is the standard way to call `static` methods?

```js
// Be mindful of inheritance syntax.

class Super {
  static whoami() {
    return "Super";
  }
  lognameA() {
    console.log(Super.whoami());
  }
  lognameB() {
    console.log(this.constructor.whoami());
  }
}

class Sub extends Super {
  static whoami() {
    return "Sub";
  }
}

new Sub().lognameA();
// "Super".

new Sub().lognameB();
// "Sub".
```

- In `CSS`, what is `flex-grow`?
  - This property specifies how much of the remaining space in the flex container should be assigned to the item.
- In `CSS`, what is `CSS Baseline`?
  - A collection of HTML element and attribute style-normalizations, a global reset.
- In `CSS`, what is `aria-label`?
  - The `aria-label` attribute is used to define a string that labels the current element.
  - Use it in cases where a text label is not visible on the screen.
  - If there is visible text labeling the element, use `aria-labelled` by instead.
- In `CSS`, what is `ARIA`?
  - Accessible Rich Internet Applications (ARIA) is a set of attributes that define ways to make web content and web applications (especially those developed with JavaScript) more accessible to people with disabilities.
- In `Material-UI`, what's the purpose of having both `AppBar` and `Toolbar`?
  - Think of `AppBar` as the header and `Toolbar` of the amount of horizontal bars within the header.

# August 3 2020

- In `JavaScript`, how does the `splice()` function work?
  - Can be used to delete, add, or replace with the data structure being an array.
  - To delete, `.splice(index, number of elements to delete)`
  - To add, `.splice(index, number of elements to delete, thing to be added in, another thing, etc.)`
  - To replace, `.splice(index, number of elements, thing to replace)`

```js
// Delete.
let scores = [1, 2, 3, 4, 5];
let deletedScores = scores.splice(0, 3);
console.log(scores); //  [4, 5]
console.log(deletedScores); // [1, 2, 3]

// Add.
let colors = ["red", "green", "blue"];
colors.splice(2, 0, "purple");
console.log(colors); // ["red", "green", "purple", "blue"]

// Replace.
let languages = ["C", "C++", "Java", "JavaScript"];
languages.splice(2, 1, "C#", "Swift", "Go");
console.log(languages); // ["C", "Python", "C#", "Swift", "Go", "JavaScript"]
```

- In `Javascript`, how to determine the variable is `undefined` or `null` properly?

```js
// Since "null == undefined" already, just do this.
if (variable == null) {
  // Your code here.
}
```

- In `JavaScript`, how to sort array of objects by property value?

```js
var champions = [
  { name: "Jarvan IV", group: "Demacia", stars: 1 },
  { name: "Kayn", group: "Edgelord", stars: 3 },
  { name: "Zac", group: "Slime", stars: 5 },
];

function compare(a, b) {
  if (a.stars < b.stars) {
    return -1;
  }
  if (a.stars > b.stars) {
    return 1;
  }
  return 0;
}

champions.sort(compare);

// OR!

champions.sort((a, b) => (a.stars > b.stars ? 1 : b.stars > a.stars ? -1 : 0));

// OR!

champions.sort((a, b) => {
  if (a.stars < b.stars) {
    return -1;
  }
  if (a.stars > b.stars) {
    return 1;
  }
  return 0;
});
```

- In `JavaScript`, how to achieve the first or last item in an array?

```js
let champions = ["Ezreal", "Vayne", "Zac"];

console.log(champions[0]);
// "Ezreal".

console.log(champions[champions.length - 1]);
// "Zac".
```

- Gym!
  - Flex.

# August 2 2020

- Hung out with video editing friend to get Sharetea, Vons, and talk at a park.

# August 1 2020

- Gym!
  - Flex.

# July 31 2020

- Hung out with friends at Tapex, the shop, Everbowl, Rohr Park, Marharlika, Kaiyo Sushi, Happy Lemon, and elevator house.

# July 30 2020

- Last minute quick commits to save the day.

# July 29 2020

- What are the differences between `onBlur()` VS `onFocus()`.
  - `onBlur()` activates when a component is out of focus, such as saving an edit that's not complete.
  - `onFocus()` activates what a component is focused, such as having the intent to edit something.
- What's the hard thing about update within a `CRUD` pattern?
  - Need to account the past states and the future states, with the present state.
- Stayed up with a friend since she's going through a difficult time.
  - Unsure how to progress other than being there for here.

# July 28 2020

- What is `CRUD`?
  - Create, read, update, and delete.
- What is the purpose for the `CRUD` functions of create, read, update, and delete?
  - Create would be called to make new objects that have unique ids.
  - Read would be called to see all objects, no alteration.
  - Update would be called when an object makes a change, either whole or partly.
  - Delete would be called when an object is to be removed.
- When would someone call these particular functions in an application?
  - Create:
    - Add new user.
    - Add a comment.
  - Read:
    - Load feed.
    - Load comments.
  - Update:
    - Edit profile.
    - Edit a comment.
  - Delete:
    - Delete account.
    - Delete a comment.
- Gym!
  - Flex.
  - Changed "freedom" to "flex" since less letters and makes more sense.
- Great stream last night!
  - Coding, Duolingo, and Marbles are the way to go!

# July 27 2020

- In `JavaScript`, `for` VS `forEach`?
  - `for` for flexibility using `break` or iterating in reverse.
  - `forEach` for readability and simple usage.
- In `JavaScript`, how does the `find` function work?

```js
const array1 = [5, 12, 8, 130, 44];

const found = array1.find((element) => element > 10);

console.log(found);
// expected output: 12
```

- In `JavaScript`, what are the main differences between `.find()` and `.some()`.
  - `.find()` returns a value and used to look for one specific value.
    - "Is there a dog here named "Bolt"?"
  - `.some()` returns a boolean and checks to see if the data structure does have what the user is looking for.
    - "Is there a white dog here?"
- In `JavaScript`, is `.find()` faster than a `for` loop?
  - Yes, 30% faster.
- Gym!
  - Flex.

# July 26 2020

- Headed home from LA.
- Saw some birds and squirrels near Camp Pendleton, was cute.
- Jamming to 2000s songs.

# July 24 2020

- Head up to LA for stream group.
- Met a lot of great people! (Hope I spelled their names right.)
  - Nic.
  - Matt.
  - Jared.
  - Cheyenne.
  - Darren.
- Made sure to clean up after myself.

# July 24 2020

- How do you delete a line in `Visual Studio Code` dependent on where the cursor is?
  - `Ctrl + K`

# July 23 2020

- How do you render `ctrl + caret`, while still having the caret being the symbol in markdown?
  - I don't think it's possible.
- How do you `scp` multiple files from a source?
  - `scp %USER%@%HOST%:/%SOME-DIRECTORY/\{%FILE-1%,%FILE-2%\} /%TO-DESTINATION%/`
- What is `Chaos Engineering`?
  - Chaos engineering is the discipline of experimenting on a software system in production in order to build confidence in the system's capability to withstand turbulent and unexpected conditions.
  - Implemented due to deadlines of projects without enough time to test vulnerabilities.
- What are the `Chaos Engineering` goals?
  - Given a software system's ability, ensuring adequate quality of service, also known as resiliency.
  - Main tests would be:
    - Infrastructure failures.
    - Network failures.
    - Application failures.
- If you're typing in the terminal and want to restart, how do you do it?
  - `Ctrl + U` will erase everything and start from the beginning, granted the cursor as at the end.
  - `Ctrl + Y` will bring back the line deleted from previously.

# July 22 2020

- How to fix multiple monitors for displaying a `VirtualBox` image?
  - Go into the settings of the image.
  - Set monitors to 2+.
  - Save.
  - Launch the image.
  - From here there should be 2+ instances of `VirtualBox`.
  - To properly resize, instead of `VirtualBox` itself, go within the virtual machines themselves and fix the settings.
- What is `Mission Control` on `Mac`?
  - The area to see all your apps and screens on a global level.

# July 21 2020

- Pre-exercise to building high-performing teams.
  - Quadrants are based on importance and urgency.
  - 1 = High importance, high urgency.
    - Deadlines.
    - Emergencies.
  - 2 = High importance, low urgency.
    - Recreation.
    - Relationships.
  - 3 = Low importance, low urgency.
    - Entertainment.
    - Social media.
  - 4 = Low importance, high urgency.
    - Interruptions.
    - Meetings.
- Gym!
  - Flex.

# July 20 2020

- The job search for other software engineers is rough.
  - 1 person during the pandemic is as follows:
    - 476 applications.
    - 470 rejections.
    - 23 first rounds.
    - 5 second rounds.
    - 5 cancelled offers. (!)
    - 1 offer.
- Feeling good about my progress at work.
  - Managing state within the application and making sure the frontend reflects the backend properly.

# July 19 2020

- Submitted what I could for work, still a lot to consider.
- Gym!
  - Flex.

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

- In `Javascript`, how do you iterate over all the properties of an object `obj`?

```js
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

```js
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

- How to access the last element of an array in `JavaScript`?
  - `var last-element = my-array[my-array.length - 1]`
- How to add new properties to an object?
  - There's 2 ways.
  - Dot notation!
    - `obj.new-key = "new-value";`
  - Square bracket notation!
    - `obj["new-key"] = "new-value";`
- How to check if object value exists within a `JavaScript` array of objects?

```js
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
  - Flex.

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
  - Flex.
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
  - Flex.

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
  - Flex.

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
  - Flex.

# June 25 2020

- Gym!
  - Volleyball.

# June 24 2020

- ???

# June 23 2020

- ???

# June 22 2020

- Gym!
  - Flex.

# June 21 2020

- ???

# June 20 2020

- Gym!
  - Flex.

# June 19 2020

- Gym!
  - Flex.

# June 18 2020

- Left my second tour and decided where I want to go permanent.
- Gym!
  - Flex.

# June 17 2020

- Gym!
  - Flex.

# June 16 2020

- ???

# June 15 2020

- Gym!
  - Flex.

# June 14 2020

- ???

# June 13 2020

- Gym!
  - Flex.

# June 12 2020

- ???

# June 11 2020

- ???

# June 10 2020

- Gym!
  - Flex.

# June 9 2020

- Gym!
  - Flex.

# June 8 2020

- Gym!
  - Flex.

# June 7 2020

- ???

# June 6 2020

- ???

# June 5 2020

- Gym!
  - Flex.

# June 4 2020

- ???

# June 3 2020

- Gym!
  - Flex.

# June 2 2020

- ???

# June 1 2020

- Gym!
  - Flex.

# May 31 2020

- ???

# May 30 2020

- ???

# May 29 2020

- ???

# May 28 2020

- Gym!
  - Flex.

# May 27 2020

- ???

# May 26 2020

- Gym!
  - Flex.

# May 25 2020

- ???

# May 24 2020

- ???

# May 23 2020

- Gym!
  - Flex.

# May 22 2020

- ???

# May 21 2020

- ???

# May 20 2020

- ???

# May 19 2020

- Gym!
  - Flex.

# May 18 2020

- ???

# May 17 2020

- ???

# May 16 2020

- ???

# May 15 2020

- Gym!
  - Flex.

# May 14 2020

- ???

# May 13 2020

- Gym!
  - Flex.

# May 12 2020

- ???

# May 11 2020

- Gym!
  - Flex.

# May 10 2020

- ???

# May 9 2020

- ???

# May 8 2020

- Gym!
  - Chest and triceps.

# May 7 2020

- ???

# May 6 2020

- Gym!
  - Flex.

# May 5 2020

- Gym!
  - Flex.

# May 4 2020

- ???

# May 3 2020

- ???

# May 2 2020

- ???

# May 1 2020

- ???

# April 30 2020

- Gym!

  - Flex.

# April 29 2020

- Gym!

  - Flex.

# April 28 2020

- Gym!
  - Flex.

# April 27 2020

- Researched mechanical keyboards for a good portion of my day.
  - Decided I want a 75 keyboard. (Removes the numpad at the right while staying compact.)
- Gym!
  - Flex.

# April 14 2020

- Gym!
  - Flex.

# April 13 2020

- Bought a lot of things due to quarantine.
- Gym!
  - Flex.

# April 12 2020

- Gym!
  - Flex.

# April 11 2020

- Helped around the house.
- Thought of some video ideas dealing with city pop.
- Gym!
  - Flex.

# April 10 2020

- Gym!
  - Flex.

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
  - Flex.

# April 8 2020

- Work.
- Gym!
  - Flex.

# April 7 2020

- Work.
- Gym!
  - Flex.

# April 6 2020

- Work.
- Gym!
  - Flex.

# April 5 2020

- Gym!
  - Flex.

# April 4 2020

- Gym!
  - Flex.

# April 3 2020

- Work.
- Gym!
  - Flex.

# April 2 2020

- Work.
- Gym!
  - Flex.

# April 1 2020

- Work.
- Gym!
  - Flex.

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
  - Flex.

# March 23 2020

- Lots of email and loose ends to finish up before going to my next tour.

# March 22 2020

- Relaxed.
- Gym!
  - Flex.

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

// and to call the class.

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
  - Flex.

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
  - Generally (in the 2020 context, future readers of this journal), a front-end framework is a code library (aka pre-written) to make client-side rendering easier and faster.
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
PROMPT-COMMAND='history -a'
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
  - `mv %OLD-FILE-NAME% %NEW-FILE-NAME%`
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
        to={`/attractions/${props.attraction.url-name}`}
        key={props.attraction.id}
      >
        <img alt={props.attraction.name} src={props.attraction.image-url} />
        <h1>{props.attraction.name}</h1>
      </Link>
      <StarRatings rating={props.attraction.average-rating} />
    </div>
  );
};

// Second level without props.
const Attraction = ({ auth, attraction }) => {
  return (
    <div auth={auth} key={attraction.id}>
      <Link
        token={auth.token}
        to={`/attractions/${attraction.url-name}`}
        key={attraction.id}
      >
        <img alt={attraction.name} src={attraction.image-url} />
        <h1>{attraction.name}</h1>
      </Link>
      <StarRatings rating={attraction.average-rating} />
    </div>
  );
};

// Third level destructuring the destruction.
const Attraction = ({
  // `auth` and `auth: { token }` gives access to both the whole `auth` object and its `token`.
  // So if you need to pass down more than just the `token`, this is what is needed.
  auth,
  auth: { token },
  attraction: { id, url-name, name, image-url, average-rating },
}) => {
  return (
    <div auth={auth} key={id}>
      <Link token={token} to={`/attractions/${url-name}`} key={id}>
        <img alt={name} src={image-url} />
        <h1>{name}</h1>
      </Link>
      <StarRatings rating={average-rating} />
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
    - `use %DATABASE-NAME%`
  - To check what database you're in.
    - `db`
  - To add a collection to the database you're in.
    - `db.%COLLECTION-NAME%.insert({"name" : "AC"})`
  - To show all collections in all databases.
    - `show collections`
  - To show all the documents in the collection.
    - `db.%COLLECTION-NAME%.find()`
  - To show a specific document in a collection, specify a key value pair.
    - `db.%COLLECTION-NAME%.find({%KEY%: "%VALUE%"})`
  - To show a document in a collection in a pretty style.
    - `db.%COLLECTION-NAME%.find({%KEY%: "%VALUE%"}).pretty()`
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
  - `git checkout -- %FILE-NAME%`
- How to select files in another branch that you want in your branch?
  - Be in your branch where you want the changes.
  - `git checkout --patch %OTHER-BRANCH% %FILE-NAME%`
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
  - An open-source JavaScript module bundler that takes modules with dependencies and generates `static` assets representing those modules.
  - If you have 5 `.css` files, `Webpack` transforms them into 1 `.css` to alleviate call noise.
- How to check if a package is installed globally?
  - `npm list -g`
  - `npm list -g %PACKAGE-NAME%`
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

```js
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
  - `cp %I-WANT-TO-COPY-YOU-FILES% %DESTINATION-AREA%`
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
  - `scp ac@starkiller:~/%FILE-NAME% .`
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
  - Make a back-up via `cp %FILE-NAME%.VDI %BACK-UP-FILE-NAME%.VDI`.
  - Resize the file `vboxmanage modifyhd %FILE-NAME%.VDI --resize 100000`
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
