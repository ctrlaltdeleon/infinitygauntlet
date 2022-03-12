import React, { Component } from "react";

// react-leaflet
import { Map, Marker, Popup, TileLayer } from "react-leaflet";
import "leaflet/dist/leaflet.css";

class App extends Component {
  render() {
    const position = [32, 117];
    return (
      <div className="Main">
        <div className="Content">
          <Map
            style={{ width: "100%", height: "400px" }}
            center={position}
            zoom={13}
          >
            <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
            <Marker position={position}>
              <Popup>
                A pretty CSS3 popup.
                <br />
                Easily customizable.
              </Popup>
            </Marker>
          </Map>
        </div>
      </div>
    );
  }
}

export default App;
