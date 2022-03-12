const { createStore } = Redux;

const initState = {
  todos: [],
  posts: [],
};

function myReducer(state = initState, action) {
  if (action.type == "ADD_TODO") {
    return {
      ...state,
      todos: [...state.todos, action.payloadTodo],
    };
  }

  if (action.type == "ADD_POST") {
    return {
      ...state,
      posts: [...state.posts, action.payloadPost],
    };
  }
}

const store = createStore(myreducer);

store.subscribe(() => {
  console.log("state updated");
  console.log(store.getState());
});

// const todoAction = { type: 'ADD_TODO', payload: 'buy milk' };

// store.dispatch(todoAction)

store.dispatch({ type: "ADD_TODO", payloadTodo: "this is todo 1" });
store.dispatch({ type: "ADD_TODO", payloadTodo: "this is todo 2" });
store.dispatch({ type: "ADD_POST", payloadPost: "this is post 1" });
