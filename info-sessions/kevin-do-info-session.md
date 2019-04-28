# KEVIN DO INFO SESSION

```
Name:       Kevin Do
Time:       N/A
Bio:        Northrop Grumman Intern, PlayStation Intern, and Twitch Software Developer Engineer
Contact:    N/A
```

Notes:

```js
<html>
<head>
	<script src="https://cdnjs.cloudflare.com/ajax/libs/babel-core/5.8.24/browser.js"></script>
	<script src="https://npmcdn.com/react@15.6.2/dist/react-with-addons.js"></script>
	<script src="https://npmcdn.com/react-dom@15.6.2/dist/react-dom.js"></script>

	<style>
		body {
			background: #fff
		}
	</style>
</head>
<body>
	<div id="app"></div>
	<script type="text/babel">

class CountDown extends React.Component {
  // State? Does it re-render? Does it have any pieces that move or change?
  // Life cycle methods? Do I need to make an API call? Does this need data?
  // Render function?
  // Class Methods? Do I need a handler? onClick? onHover?
  // Props? What props does it need? What are you giving the component?

  state={
    loading: true,
    user: {}
  }
  componentDidMount() {
    fetch('/user/get', {
      method: 'get',
      header: {},
      auth: {}
    }).then(user => {
      this.setState({
        user,
        loading: false
      });
    })
  }

  render() {
    const child = this.props.num > 1 ? <Countdown num={this.props.num-1}/> : null;

    if (this.props.num <= 0) {
      return null;
    }

    return (
      <div>
        <span>{this.props.num}</span>
        {this.state.loading && <LoadingSpinner/>}
        {this.state.user && this.state.user.name && <h1>{this.state.user.name}</h1>}
        {child}
      </div>
    )
  }
}

ReactDOM.render(
	<CountDown num={5}/>,
	document.getElementById('app')
);

	</script>
</body>
</html>

// Output
-----------------------
| this.props.num = 3  |
|   ---------------   |
|   |      2      |   |
|   |   -------   |   |
|   |   |  1  |   |   |
|   |   |     |   |   |

// Add onClick for each Countdown to change colors
// Centering the number using flexbox

.css {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-content: center;
}

// Make a network API call to get username
```

- https://devskiller.com/coding-tests-skill/react/
- What’d you think of the take home test? (if they did a take home test)
- TypeScript experience? Overall JavaScript experience? Overall async experience?
- Styling? Sass, inline, other?
- React
  - General experience with React?
  - Difference between componentWillUpdate and componentWillReceiveProps?
  - Where do you put business logic?
  - When is it appropriate to use component state?
  - When would you use shouldComponentUpdate?
  - How do you group your components?
  - When do you make a component reusable?
  - At what point is a component too big? When do you split a component into several smaller components?
  - What are some use cases for React Context?
  - Any pitfalls?
  - Error handling?
- Redux / Flux
  - General experience with Redux and Flux patterns?
  - What is the difference between an action, and an action creator?
  - If Redux experience:
  - What is the Redux store?
  - What’s a reducer?
  - What’s a container component?
  - How do you deal with async actions?
  - Thunks, sagas, other?
  - if Flux experience:
  - What’s a store?
  - Separation of logic between action creators and stores?
  - Pros and cons of single dispatch?
  - How do you deal with async actions?
- Error handling?
- Testing experience? Unit tests Manual tests
- Cultural - Bias for Action
- Give me an example of a calculated risk that you have taken where speed was critical. What was the situation and how did you handle it? What steps did you take to mitigate the risk? What was the outcome?
- Describe a situation where you made an important business decision without consulting your manager. What was the situation and how did it turn out?
