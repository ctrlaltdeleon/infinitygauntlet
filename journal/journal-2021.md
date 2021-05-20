# May 22 2021
# May 21 2021

- End of the work week.
- We almost forgot a coworkers lunch so we had to go back and drive to the restaurant again.

# May 20 2021

- Gym!
  - Chest and triceps.
- Decided to start my series called "I review %INSERT-TOPIC-HERE% in 30 seconds".
  - Wanted to include mainly media such as movies, anime, shows, and manga, but can be extended.
# May 19 2021

- Played volleyball and Santa Venetia park with friends.

# May 18 2021

- Chose to telework today.
- Lots of emails to sift through, I don't like getting unneeded emails.

# May 17 2021

- Feel pretty tired today.
- Car didn't start up due to my radar being plugged into the 12V socket in the car which never turns off.

# May 16 2021

- Finishing up the "The New Mutants" movie.
- Kuya visited then I took a nap.
- Played volleyball and had good numbers and good players, but could tell people got tired at the end.
- Went to Brenners.
  - Won both times in spikeball.
  - 1 with Kirby and 1 with Brenner.
  - It started raining during the 2nd game so we tried playing under the tarp, but was too low.
  - Pulled in Puzzle & Dragons since it was a Demon Slayer event.
    - Got Nezuko!
    - Got Zenitsu!

# May 15 2021

- Went to a family party where it was Pokemon themed.

# May 14 2021

-

# May 13 2021
# May 12 2021
# May 11 2021
# May 10 2021
# May 9 2021
# May 8 2021
# May 7 2021
# May 6 2021
# May 5 2021
# May 4 2021

- Happy Star Wars day!
- In `Java`, how is a class extended to have additional capability?

```java
public class Monster {
  private String name;
  private String attribute;
  private String type;

  // Setters and getters.
}

// This will have all of "Monster" plus additional effects.
public class EffectMonster extends Monster {
  private String effect;

  public EffectMonster setEffect(String param) {
    this.effect = param;
    return this;
  }

  public String getEffect() {
    return this.effect;
  }
}
```

# May 3 2021

- ???

# May 2 2021

- ???

# May 1 2021

- ???

# April 30 2021

- ???

# April 29 2021

- I know who shot JFK!
- Got some custom vans shoes.
  - Skate pro slip ons!
  - One is sky blue with "uwu, uwu" embroidered on them.
  - One is natural white with "ily, 3000" embroidered on them.
  - It was about $100 each, but hey it's gonna be worth it.
    - I hope.
- In `Electron`, how does one render a save dialog with proper information being transferred?
  
```js
const { BrowserWindow, dialog, ipcMain } = require("electron");
const fs = require("fs");

// Note that Electron doesn't do well with Blob data.
ipcMain.on("%SOME-ROUTE-NAME%, function (event, data) {
  let options = {
    title: "Save As...",
    defaultPath: data.nameOfFile,
    buttonLabel: "Save file!",
    filters: [
      {
        name: "Word Document",
        extensions: ["docx"],
      }
    ]
  }

  let errorOptions = {
    title: "ERROR!",
    type: "error",
    message: "Something went wrong.",
    buttons: ["Close"],
  }

  // Saving dialog area.
  dialog.showSaveDialog(options).then((result) => {
    // This part below is important due to changes in Electron for filename.
    filename = result.filePath;
    if (filename === undefined) {
      dialog.showMessageBox(BrowserWindow.getFocusedWindow(), errorOptions);
      return;
    }
    fs.writeFile(filename, Buffer.from(%SOME-ARRAY-BUFFER%), (err) => {
      if (!err) {
        let successOptions = {
          title: "Download success!",
          type: "info",
          message: `Saved to ${filename}`,
          buttons: ["Close"],
        }
        dialog.showMessageBox(BrowserWindow.getFocusedWindow(), successOptions);
      }
    })
  }).catch((err) => {
    dialog.showMessageBox(BrowserWindow.getFocusedWindow(), errorOptions);
  });
```

# April 28 2021

- Was planning to eat at Hanu, but the wait time was too long so Manna instead with Kirby!
- Gym!
  - Chest and triceps.

# April 27 2021

- Woke up feeling refreshed a bit, even after snoozing the button a couple of times.
  - Apparently sleeping and then waking up at 90 minute increments (1.5 hours, 3 hours, 4.5 hours, etc.) abides by the sleep cycle.
- In `Git`, what's the main differences between `git rebase` vs `git merge`?
  - If one would prefer a clean, linear history free of unnecessary merge commits, `git rebase`.
  - If one wants to preserve the complete history, `git merge`.
- Volleyball!
  - Santa Venetia park and met some new people such as Alina (?) and John (?).
  - I don't know how to spell names.

# April 26 2021

- Gym!
  - Back and biceps.

# April 25 2021

- Ate at Menya Ultra with Kirby.
  - WE MISSED THE BRAISED CHASHU, WE WERE #7 & #8 AND THEY ONLY HAVE 5 AT OPENING.
- Melted away my worries by just spending the day.
  - Daiso!
  - Camellia Road!
- Volleyball!
  - Long time since we played, Will hit me in the face when serving. :(
- Went to Brenners!
  - Salty runback of 5 minute dungeon.
# April 24 2021

- We lose 2v4 hehe.

# April 23 2021

- Played 5 minute dungeon with Karasuno.
  - They seemed to enjoy it a lot!
  - Brandon, Will, and Kalani hopped in one at a time in the order and liked the game.
# April 22 2021

- In `Git`, how does one check the amount of commits on a branch that has been worked on?
  - `git rev-list --count HEAD^%YOUR-BRANCH-NAME%

# April 21 2021

- Gym!
  - Chest and triceps.

# April 20 2021

- 2nd dose of the Pfizer shot!

# April 19 2021

- Felt very tired this day.

# April 18 2021

- Played volleyball then spikeball.

# April 17 2021

- ???

# April 16 2021

- Watched highlights.

# April 15 2021

- ???

# April 14 2021

- ???

# April 13 2021

- Looked somewhat cloudy today, light rain.

# April 12 2021

- Dressed up today for work then being notified the admiral isn't coming, phew.
- When making object classes, how should it be formatted?

```js
// Should be 1 to 1, no changes, changes happen when receiving the data.
export class %SOME-OBJECT% {
  constructor(%ATTRIBUTE-1%, %ATTRIBUTE-2%, %ATTRIBUTE-3%) {
    this.%ATTRIBUTE-1% = %ATTRIBUTE-1%;
    this.%ATTRIBUTE-2% = %ATTRIBUTE-2%;
    this.%ATTRIBUTE-3% = %ATTRIBUTE-3%;
  }
}
```

- Happy Birthday Kirby!
- Gym!
  - Flex.
- Had to bring home Taco Bell for the family.
- Fixing trading cards, need to figure out a way to document pricing of cards.

# April 11 2021

- Went to Gamezone with Citrus, Junpei, and Kirby.
  - Got these items:
    - Legendary Duelist Decks II (Yugioh).
    - Maximum Gold Box (4 pack) (Yugioh).
    - Trainer Toolset (Pokemon).
- Went to Plaza Bonita Mall with Citrus, Junpei, and Kirby.
  - Stopped by Comics-N-Stuff.
  - Tried out the new restaurant called "Firebirds Chicken".
  - We got too much Cinnabon omg.
- Went to Brenners.
  - ABG and Jello made some cheese corn.
  - We got too much Cinnabon omg.
  - Spikeball!
    - Marco has a wicked serve.

# April 10 2021

- Beach Volleyball!
- Just wanted some time to myself this day.

# April 9 2021

- Went to see the doctor, referred me to a dermatologist.
  - Took about 2 hours for general checkup, urine test, blood tests, and pharmacy.
- "The Falcon and the Winter Soldier"!
  - That was a bloody shield.
  - I liked Battlestar, shame he died.

# April 8 2021

- ???

# April 7 2021

- ???

# April 6 2021

- ???

# April 5 2021

- Back to work!
- Left earlier than usual, but due to traffic, arrived at the same time I usually do.
- Got Subway today, apparently their register wasn't working for cards.
  - Led to lunch time rush bust. :(
  
# April 4 2021

- Took long required naps today.
- Family got their first dose of COVID-19 vaccines.
- Picked up Kirby and went to Partyrental's backyard and played some spikeball.
  - Felt bad today because I felt like everyone was attacking me.
  - Felt bad for feeling that way and expressing it?
  - I just felt bad haha.

# April 3 2021

- Menya Ultra with Kirby first thing in the morning.
- While waiting for Menya Ultra, explored Daiso.
- 30 minutes after opening, no more braised chashu at Menya Ultra. :(
- Got Ootea!
- Went to Gamezone and got a transparent container, small sleeves, and Yugioh cards!
  - Relived the original Yugi decks and got Exodia!
- Gym!
  - Volleyball for almost 5 hours.

# April 2 2021

- Feel pretty good about outfit today, plain black shirts are nice.

# April 1 2021

- In `Git`, how does one rename a local branch that you're on?
  - `git branch -m %NEW-BRANCH-NAME%`
  - On Windows: `git branch -M %NEW-BRANCH-NAME%`
- Full ACAT request from Robinhood to Public.
- Super lathered the anti-dandruff shampoo in my hair.
- Gym!
  - Flex.

# March 31 2021

- Arm feels a bit sore.
- Got together with San Diego friends to eat out.
  - Tried a new place called "Michoacana" which is this mexican, video-game, dessert place.
  - Went to Chili's and experienced poor slow service, I was falling asleep.
- Got to see Kirby!
- Gym!
  - Flex.

# March 30 2021

- Got my first dose of the Pfizer vaccine for COVID-19!
- Went to San Ysidro school area to eat some Tacos El Gordo with Kirby.
  - Has some nice fields and playgrounds, potential sport area, really nice!
- Movie!
  - "Zack Snyder's Justice League"
  - Finally finished it after so long since it's 4 hours.

# March 29 2021

- Fixed up my desk a bit, mostly just boxes, cables.
- Gym!
  - Flex.

# March 28 2021

- ???

# March 27 2021

- ???

# March 26 2021

- ???

# March 25 2021

- ???

# March 24 2021

- ???

# March 23 2021

- ???

# March 22 2021

- ???

# March 21 2021

- ???

# March 20 2021

- ???

# March 19 2021

- ???

# March 18 2021

- ???

# March 17 2021

- ???

# March 16 2021

- ???

# March 15 2021

- Tattoo today!
  - Princess Mononoke inspired, the scene where Ashitaka says "you're beautiful" to San.

# March 14 2021

- Happy birthday to Jean from Genshin Impact.
- Went to Brendan's!
  - 
- Played spikeball with the homies and "Betrayal at House on the Hill" wh

# March 13 2021

- ???

# March 12 2021

- ???

# March 11 2021

- ???

# March 10 2021

- ???

# March 9 2021

- ???

# March 8 2021

- ???

# March 7 2021

- ???

# March 6 2021

- ???

# March 5 2021

- "Wandavision"!

# March 4 2021

- ???

# March 3 2021

- Movie!
  - "The Great Gatsby".
- Rewatched some funny scenes from "The Office".

# March 2 2021

- Started "Darling the in the Franxx".
- No more Pokemon cereal boxes. 😞
  
# March 1 2021

- Start of another work week.
- Thanks for being there for me Kirby.

# Feburary 28 2021

- Started lubing up the switches, I definitely do feel a difference between lubed vs unlubed.
# Feburary 27 2021

- ???
# Feburary 26 2021

- ???

# Feburary 25 2021

- Got gymnastics rings!

# Feburary 24 2021

- ???
# Feburary 23 2021

- ???
  
# Feburary 22 2021

- ???

# Feburary 21 2021

- ???

# Feburary 20 2021

- ???

# Feburary 19 2021

- ???

# Feburary 18 2021

- Can one chain ternary operations?

```java
// Yes.
int value = input == null ? 0 : input.equals("") ? 0 : Integer.parseInt(input);
// If the input is null, value is 0.
// Else if the input is blank, value is also 0.
// Else parse the input.
```
# Feburary 17 2021

- In your case start with 5% in the Roth TSP to get the match, then start working on maxing out a Roth IRA, then back to the TSP.
- Usually, people invest into their 401k up to the company match, and then their IRA to the max, and then back to the 401k to the max. The reason they do this is because the average 401k usually has higher fees than their IRA does, but leaving free money (the match) on the table would be stupid; hence the match, IRA, back to 401k.
# Feburary 16 2021

-

# Feburary 15 2021
# Feburary 14 2021
# Feburary 13 2021
# Feburary 12 2021
# Feburary 11 2021
# Feburary 10 2021
# Feburary 9 2021
# Feburary 8 2021
# Feburary 7 2021
# Feburary 6 2021
# Feburary 5 2021
# Feburary 4 2021
# Feburary 3 2021
# Feburary 2 2021

- Gym!
  - Volleyball.
# Feburary 1 2021

- In `JavaScript`, is there an easy way to automatically add properties to objects that are undefined?

```js
// For hard coded keys.
var test = {};
test.hello = test.hello || {};
test.hello.world = "Hello world!";

// For variable keys.
var test = {};
test[variable] = test.hello || {};
test[variable].world = "Hello world!";
```

- How does one ask a Stack Overflow question?
  - What am I trying to do?
  - What is the code that currently tries to do that?
  - What do I expect the result to be?
  - What is the actual result?
  - What I think the problem could be?

```
// Copy pasta.
**What am I trying to do?**
**What is the code that currently tries to do that?**
**What do I expect the result to be?**
**What is the actual result?**
**What I think the problem could be?**
```

- Gym!
  - Flex.

# January 31 2021

- Got to see the old gang again and played spikeball, secret hitler, and more.
- Gym!
  - Flex.
  
# January 30 2021

- I think I'm falling for you.
  
# January 29 2021

- Donut Bar, Zion Market, WandaVision EP. 4.
- Slept all day.
  
# January 28 2021

- I don't think you can really go wrong with any of the three; I'm a long-time customer of two of them.

The biggest difference, in my eyes, is the actual structure of the companies themselves--

-Schwab is a publicly traded company, and management is responsible to a board of directors and holders of their stock. When they cut fees, they're cutting their profit margin, and presumably the value that they can return to their shareholders

-Fidelity is a privately held company, primarily owned and controlled by the descendants of its founder, and other company executives. While they're still a for-profit enterprise, the fact that they're private and closely-held gives them much more latitude in how they operate-- they don't have to make their earnings public, and they don't have to worry about a shareholder otherwise unconnected with the company exerting influence on how they run the business.

-Vanguard is essentially a mutual company. The company itself is owned by its funds, so in owning shares in a Vanguard fund, you own part of Vanguard itself-- the structure is a little like a credit union. The return of value to the 'shareholders' (i.e. the investors in Vanguard funds) comes in the form of reduced fees.

# January 27 2021

- Gym!
  - Volleyball.
  - Went to Rohr Park this time around, plenty of spots, lights are great.
  
# January 26 2021

- ???
- 
# January 25 2021

Former optician here!

I highly recommend polycarbonate lenses (as opposed to a basic plastic lens- also known as CR) they are more durable and naturally scratch-resistant and have UV protection. When I worked as an optician, we could only add UV and scratch resistant coatings to a basic plastic lens.

High Index Lenses are typically better suited for prescriptions under - 2 but of course that is up to your personal preference. Some frames are not well-suited to high index lenses.

Anti-Reflective Coating helps reduce glare from nighttime driving, computer screens and helps reduce eye fatigue. If your eyes are sensitive to changes in light it is worth the cost.

Transitions/tinting is completely personal preference. Just be aware most transitions are NOT polarized the way normal sunglasses are.

If you have any other questions I’d be happy to help :)

- Finally finished my long task.

# January 24 2021

- Stayed home.

# January 23 2021

- Uncle Agapito.

# January 22 2021

- Stayed home.
# January 21 2021

- In `React`, how should autosave be handled in terms of string inputs?
  
```js
// With autosave.
const [autoSave, setAutoSave] = useState("");
const [state, setState] = useStateWithCallback("");

const handleState = (event) => {
    setState(event, (update) => console.log("Do something with update", update));
}

const stateAutoSave = (event) => {
    setAutoSave(event);
    if (autoSave.length % 10 === 0 && autoSave.length !== 0) {
        handleState(event);
    }
}

onBlur={(event) => handleState(event.target.value)};
onChange={(event) => stateAutoSave(event.target.value)};

// Without autosave.
const [state, setState] = useStateWithCallback("");

const handleState = (event) => {
    console.log("Do something with state", state);
}

onBlur={handleState};
onChange={(event) => setState(event.target.value)};
```
# January 20 2021

- Gym!
  - Volleyball.

# January 19 2021

- What is relationship anarchy?
  - The idea of relationships decided by people and what they bring out of you rather than labels.
- Was extremely tired.
- Gym!
  - Volleyball.
  - Took it easy and went for setter position to give hitters what they can which worked out well.
  
# January 18 2021

- Martin Luther King Jr. day.
- Gym!
  - Volleyball.
  - Was pissed and just want to be better.

# January 17 2021

- Slept.
  
# January 16 2021

- Gym!
  - Volleyball.
  - Flex.

# January 15 2021

- Gym!
  - Flex.

# January 14 2021

- Gym!
  - Volleyball.

# January 13 2021

- Anybody with flights to the USA will need a negative status of COVID.

# January 12 2021

- Protein intake should be near 1 gram per kilogram of bodyweight.
  - Currently at ~70 kilograms, so ~70 grams of protein per day.
  - Protein shake gives ~25 grams.
  - Protein bars gives ~10 grams.
- Gym!
  - Volleyball.
  - Got one really nice pipe spike in, but it hit the net, but ended on the other side.

# January 11 2021

- Gym!
  - Flex.
# January 10 2021

- Gym!
  - Flex.
# January 9 2021

- Gym!
  - Volleyball.
# January 8 2021

- Working on self assessment.
# January 7 2021

- Amount of downloads `@acfromspace/weeb` has thus far?
  - 684.
- What is  ultimate achievement in Hollywood?
  - Achieving an Emmy, a Grammy, an Oscar, and a Tony, also referred to as an "EGOT".
- What are the differences between an Emmy, a Grammy, an Oscary, and a Tony?
  - Emmy is for television.
  - Grammy is for music.
  - Oscar is for film.
  - Tony is for theatre.
# January 6 2021

- Gym!
  - Flex.
# January 5 2021

- Time to teach `MongoDB`!
  - Went really well! Besides the `.git` mess we ended up in, mostly due to `NetBeans` IDE going into `IntelliJ` IDE.
- In `IntelliJ`, how does one organize the imports in alphabetical order?
  - `Ctrl + Alt + O`
  - This also adds required imports and removes unneeded imports.

# January 4 2021

- Finally back to work with the whole team.
- In `JavaScript`, how does one insert characters in a string at specific locations, I.E. a phone number?

```js
// Link: https://stackoverflow.com/a/6981793/12458952

var n = "1234567899";
console.log(n.replace(/(\d{3})(\d{3})(\d{4})/, "$1-$2-$3")); // Returns "123-456-7899".
```

- In `JavaScript`, what are some key things to note about the `JavaScript Date` object?

```js
// Link: https://stackoverflow.com/a/31732581/12458952

new Date("2011-09-24"); // "Year-Month-Day".
// => Fri Sep 23 2011 17:00:00 GMT-0700 (MST) - ONE DAY OFF.

new Date("09-24-2011");
// => Sat Sep 24 2011 00:00:00 GMT-0700 (MST) - CORRECT DATE.

new Date("2011/09/24"); // Change from "-" to "/".
// => Sat Sep 24 2011 00:00:00 GMT-0700 (MST) - CORRECT DATE.
```

- How does one `return` with a ternary?

```java
// Link: https://stackoverflow.com/a/23089965/12458952

public static String createCharacterElement(Character character) {
    return character.getElement() != null ? "Element: " + character.getElement() : "Element: N/A";
}
```

- Gym!
  - Flex.

# January 3 2021

- Cleaning my room, finally got to it after taking long naps and trying to put myself together.
- Got stuff to return eventually.
- Demoralized from League of Legends, just was not able to carry the team despite the effort I put in.
# January 2 2021

- Movie!
  - "Soul".
- Thanks Kirby.
- Gym!
  - Volleyball.
# January 1 2021

- Happy new year!
- Fell asleep through it lol.
- Got to talk to Pickles and Illaoi then others showed up later after attending a get together.