import React from "react";

// Component Life Cycle
// 1. Birth/Mount
// - constructor()
// - static getDerivedStateFromProps()
// - render()
// - componentDidMount()
// 2. Growth/Update
// - static getDerivedStateFromProps()
// - shouldComponentUpdate()
// - render()
// - getSnapshotBeforeUpdate()
// - componentDidUpdate()
// 3. Death/Unmount
// - componentWillUnmount()
// Other!
// - static getDerivedStateFromError()
// - componentDidCatch()
// - setState()
// - forceUpdate()
// Class Properties!
// - defaultProps
// - displayName
// Instance Properties!
// - props
// - state

export default class FreddieMercury extends React.Component {
  // `construct()`
  // First method to call before mounting.
  // Freddie gets prepared beforehand knowing the song, dance moves, and environment.
  constructor(props) {
    super(props);
    this.state = {
      danceMoves: ["flex", "arm wind up"],
      emotion: "nervous",
      songName: "Don't Stop Me Now",
      speakerVolume: 0,
    };
  }

  initConcert() {
    this.concert = "Concert live!";
  }

  // Note: This is legacy and may not work in the future!
  // `componentWillMount()`
  // Called before mounting on the server, getting ready for the first render, dependent on state.
  // Freddie is standing behind stage waiting for the curtains to be raised and the volume to go up.
  componentWillMount() {
    if (this.state.speakerVolume === 0) {
      this.setState({
        speakerVolume: 100,
      });
    }
  }

  // `componentDidMount()`
  // Called immediately after mounting, can call data points since the component may now render.
  // Freddie is on stage and ready to perform, he needs to recall his dance moves and lyrics!
  componentDidMount() {
    axios
      .get(`someURL/getFurtherDanceMoves`)
      .then((response) => {
        console.log(response);
        this.setState({ danceMoves: response });
      })
      .catch((error) => {
        console.log(error);
      });
    this.initConcert();
  }

  // Note: This is legacy and may not work in the future!
  // `componentWillReceiveProps()`
  // If the parent class passes props to the child class after mounting, this updates the component.
  // Freddie is performing and the audience loves it! Freddie is now happy.
  componentWillReceiveProps(nextProps) {
    if (nextProps.applause) {
      this.setState({ emotion: "happy" });
    }
  }

  // `componentDidUpdate()`
  // Used as an opportunity to operate on the DOM when the component has been updated!
  // Freddie took a break to use the bathroom, if the singer isn't there, get Freddie back on stage!
  componentDidUpdate(prevProps, prevState, snapshot) {
    // Typical usage (don't forget to compare props).
    if (prevProps.singer !== this.props.singer) {
      this.fetchData(this.props.singer);
    }
  }

  // `componentWillUnmount()`
  // Cleans memory leaks and bad references to optimize.
  // Freddie is finished with the concert! The concert is now destroyed (well ended).
  componentWillUnmount() {
    this.concert = this.concert.destroy();
  }

  // `render()`
  // Pure component, displays output for the user.
  // Freddie is showing that they're wearing a white shirt.
  render() {
    return <div>shirtColor: {this.props.shirtColor}</div>;
  }
}

// Audience class that provides for `componentWillReceiveProps` as well as providing it's own life cycles.
export class Audience extends React.Component {
  constructor(props) {
    super(props);
    this.state = { applause: false, applauseVolume: 0, lights: 0 };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(event) {
    this.setState({ applause: true });
  }

  getLouder(event) {
    this.setState({ applauseVolume: (this.state.applauseVolume += 1) });
  }

  getLights(event) {
    this.setState({ lights: (this.state.lights += 1) });
  }

  // `shouldComponentUpdate()`
  // Optimizes performance by updating the component when it needs to.
  // The audience volume rises and Freddie knows it!
  // If the amount of lights is over 10, everyone will start putting their lights on and re-renders!
  shouldComponentUpdate(nextProps, nextState) {
    // Update the volume heard when it rises!
    if (nextState.applauseVolume !== this.state.applauseVolume) return true;
    // Update if the lights are greater than 10!
    else if (this.state.lights >= 10) return true;
    else return false;
  }

  // Note: This is legacy and may not work in the future!
  // `componentWillUpdate()`
  // It is called whenever a re-render is required! Before rendering new props or state when received.
  // Freddie will receive a message that he is loved by the amount of lights in the distance!
  componentWillUpdate(nextProps, nextState) {
    // When the amount of lights go to 100 from 99, we call the `Loved()` function to let Freddie know that he's loved.
    if (nextState.lights === 100 && this.state.lights === 99) {
      console.log("You are loved!");
    }
  }

  render() {
    return (
      <div>
        <button type="button" onChange={() => this.handleChange()}>
          Appreciate performance!
        </button>
        <Freddie applause={this.state.applause} />
        <div>Audience volume: {this.state.applauseVolume}</div>
        <div>Lights: {this.state.lights}</div>
        <div>
          <button onClick={(event) => this.getLouder(event)}>
            Get louder!
          </button>
        </div>
      </div>
    );
  }
}

// defaultProps
// Think a constructor to set default values props for the class.
// Freddie forgot a shirt, the concert has an available white shirt by default.
FreddieMercury.defaultProps = { shirtColor: "white" };
