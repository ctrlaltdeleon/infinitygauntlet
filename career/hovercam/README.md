# HOVERCAM

## Round 1 (Phone)

- 30 minutes.
- Behavioral questions from Office Manager.
- "Tell me about yourself."
- "Tell me about a typical day."
- "How would you start designing a product?"
- "What kind of dogs do you have?"

## Round 2 (On-Site)

- Technical questions from CEO and Lead Engineer.
- Office Manager was present observing.
- "What's the difference between C/C++?"
  - C.
    - Procedural programming class.
    - Does not support classes and objects.
    - Low level.
  - C++.
    - Supports both procedural and object oriented programming language
    - Hybrid language.
    - High level.
- "How would you make a class?"
  - It's a blueprint to an object, so you describe it with attributes needed.

```javascript
// javascript

class Hero {
  constructor(name, level) {
    this.name = name;
    this.level = level;
  }
}
```

- "How does memory allocation work?"
  - As you ask a computer to remember things, it occupies more memory.
    - This could lead to problems such as crashing due to possible memory leak.
  - The moment you don't need to memorize the said thing, the memory attached to it can be released.
  - The mechanism that handles this is called a garbage collector.
  - This can lead to inefficiency if using an auto garbage collector, thus one needs to manually allocate memory.
- "MVC, what's that?"
  - Model view controller.
    - An architectural pattern commonly used for developing user interfaces.
    - View (CLIENT) gives user actions, take updates.
      - "Can I see my favorite data?"
    - Controller (SERVER) gives updates, takes data.
      - "Show favorite data dependent on the user!"
    - Model (DATABASE) gives data, takes updates.
      - "I contain all the data!"
  - Pros.
    - Easier code maintenance and reusability.
    - Easier to coordinate in teams due to separation.
    - Multiple views.
    - Asynchronous implementations.
  - Cons.
    - An increased complex setup process.
    - Dependencies, changes to model or controller affect the whole entity.
- "How would you build a mobile app?"
  - Depends on the stack.
  - Personally I would use:
    - Model: Firebase.
    - View: React Native.
    - Controller: Redux. (An implementation of Flux)
- "How would you make a commercial product?"
  - Robust.
  - Test cases.
  - Scalability.

## Round 3 (Offer)

- Did not make it.
