# Factory Method

# What is it?

- It provides a way to delegate the instantiation logic to child classes.
- Instead of the hiring manager interviewing all candidates, have specialized interviewers interview sections of candidates.

# When to use?

- Useful when there is some generic processing in a class but the required sub-class is dynamically decided at runtime.
- Or putting it in other words, when the client doesn't know what exact sub-class it might need.
- In this case, when the hiring manager doesn't know what exact managers needed to interview candidates.

```jsx
import React from "react";
import ReactDOM from "react-dom";

// An interviewer asks questions!
class Interviewer {
  constructor() {
    this.askQuestions = () => {};
  }
}

// Interviewing developer candidates would be asked about design patterns!
class Developer extends Interviewer {
  constructor() {
    super();
    this.askQuestions = () => "asking about design patterns!";
  }
}

// Interviewing marketing candidates would be asked about social media!
class Marketing extends Interviewer {
  constructor() {
    super();
    this.askQuestions = () => "asking about social media!";
  }
}

// The hiring manager will assign interviewers to candidates.
class HiringManager {
  constructor() {
    this.makeInterviewer = () => new Interviewer();
    this.takeInterview = () => {
      const interviewer = this.makeInterviewer();
      return interviewer.askQuestions();
    };
  }
}

// The development manager receives the order and obtains the Developer class to ask developer questions.
class DevelopmentManager extends HiringManager {
  constructor() {
    super();
    this.makeInterviewer = () => new Developer();
  }
}

// The marketing manager receives the order and obtains the Marketing class to ask marketing questions.
class MarketingManager extends HiringManager {
  constructor() {
    super();
    this.makeInterviewer = () => new Marketing();
  }
}

// Create a development manager to ask developer questions.
const devMgr = new DevelopmentManager();
const devQs = devMgr.takeInterview();

// Create a marketing manager to ask marketing questions.
const markMgr = new MarketingManager();
const markQs = markMgr.takeInterview();

function App() {
  return (
    <div className="App">
      <p>Dev manager will be {devQs}</p>{" "}
      {/* Dev manager will be asking about design patterns! */}
      <p>Marketing manager will be {markQs}</p> {/* Marketing manager will be asking about social media! */}
    </div>
  );
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
```
