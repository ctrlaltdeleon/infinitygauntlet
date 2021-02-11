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

- How to ask a Stack Overflow question?
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
  - Soul.
- Thanks Kirby.
- Gym!
  - Volleyball.
# January 1 2021

- Happy new year!
- Fell asleep through it lol.
- Got to talk to Pickles and Illaoi then others showed up later after attending a get together.