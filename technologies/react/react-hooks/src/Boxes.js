import React, { useState } from "react";
import superb from "superb";
import AnimatedVisibility from "./AnimatedVisibility";

const colors = [
    "#27296D",
    "#5E63B6",
    "#A393EB",
    "#F5C7F7",
    "#AB93C9",
    "#D698B9",
    "#EDA1AB",
    "#FFBEA3",
  ];

function Box({ word }) {
  const [color] = useState(colors[Math.floor(Math.random() * colors.length)]);
  const [visible, setVisible] = useState(true);

  function hideMe() {
    setVisible(false);
  }

  let style = { borderColor: color, backgroundColor: color };

  return (
    <AnimatedVisibility
      visible={visible}
      animationIn="zoomIn"
      animationOut="zoomOut"
    >
      <div className="box" style={style}>
        <div className="center">{word}</div>
        <button className="bottom-corner" onClick={hideMe}>
          <i className="center far fa-eye fa-lg" />
        </button>
      </div>
    </AnimatedVisibility>
  );
}

export default function Boxes() {
  const startingWords = [];
  for (let i = 0; i < 12; i++) {
    startingWords[i] = superb.random();
  }
  const [words] = useState(startingWords);

  return (
    <div className="boxes">
      {words.map(word => (
        <Box key={word} word={word} />
      ))}
    </div>
  );
}