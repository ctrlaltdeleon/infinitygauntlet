import React, { Component } from "react";
import YouTube from "react-youtube";

class YoutubeVideo extends Component {
  render() {
    const opts = {
      height: 480,
      width: "100%",
      playerVars: {
        // https://developers.google.com/youtube/player_parameters
        autoplay: 1
      }
    };

    return (
      <YouTube
        videoId="QwievZ1Tx-8" // Special video here.
        opts={opts}
        onReady={this._onReady}
      />
    );
  }

  _onReady(event) {
    // Access to player in all event handlers via event.target.
    event.target.pauseVideo();
  }
}

export default Home;
