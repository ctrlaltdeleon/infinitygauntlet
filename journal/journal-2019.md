# Month Day, Year

- N/A

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

# April 17 2019

- Updated creddle.io resume.
  - Updated skills to go from "advanced, proficient, exploring" rather than placed by "programming languages, web technologies, creative software engines, databases".
    - I thought this was necessary to avoid questions on topics I wasn't too familiar about because there were no skill levels to differentiate.
  - Removed the `knucklesbattle` repo with the `acfromspacex` repo to harbor current technologies I'm working with which is mainly `ReactJS` as well as touching other technologies such as `GraphQL` and `Apollo'.
- Cleaned out the Thunderbird email!
- Applied to CyberCoders.
- Messaged Anthony, host of San Diego JavaScript Community Talks, about performing a talk.
- Messaged the General Assembly group of LA about future hackathons.
  - Feels nice to have a community dev spot for me in LA!

# April 16 2019

- Created a Gitbook for the repository of `infinitygauntlet`.
  - Gitbook is a hosting platform to showcase markdown files in a repository. Great for making books.
