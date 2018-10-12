import React, { Component } from "react";
// import axios from "axios";
import { Link } from "react-router-dom";
import Pokeball from "../pokeball.png";
import { connect } from "react-redux";

class Home extends Component {
  // Replaced w/ Redux
  // state = {
  //   posts: []
  // };

  // componentDidMount() {
  //   axios.get("https://jsonplaceholder.typicode.com/posts").then(res => {
  //     console.log(res);
  //     this.setState({
  //       posts: res.data.slice(0, 10)
  //     });
  //   });
  // }
  render() {
    const { posts } = this.props;
    // post.length checks if there's any post to begin with
    const postList = posts.length ? (
      posts.map(post => {
        return (
          <div className="post card" key={post.id}>
            <img src={Pokeball} alt="Pokeball" />
            <div className="card-content">
              <Link to={"/" + post.id}>
                <span className="card-title red-text">{post.title}</span>
              </Link>
              <p>{post.body}</p>
            </div>
          </div>
        );
      })
    ) : (
      <div className="center">No posts yet!</div>
    );
    return (
      <div className="container home">
        <h4 className="center">Home</h4>
        {postList}
      </div>
    );
  }
}

const mapStateToProps = state => {
  return {
    // Get the state which happens to have the post from the rootReducer.js
    posts: state.posts
  };
};

export default connect(mapStateToProps)(Home);
