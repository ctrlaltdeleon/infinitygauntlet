// Setup the elements
// querySelector() returns the first single element in the document that matches the CSS
// querySelectorAll() returns a collection of all elements that match the selector
// preferably if you have 1 instance use querySelector(), other wise querySelectorAll()
// getElementById & getElementsByTagName returns by ID/tag name
// getElementsByClassName returns a collection of elements that have a specified class (not a selector)
const player = document.querySelector(".player");
const video = player.querySelector(".viewer");
const progress = player.querySelector(".progress");
const progressBar = player.querySelector(".progress__filled");
const toggle = player.querySelector(".toggle");
const skipButtons = player.querySelectorAll("[data-skip]");
const ranges = player.querySelectorAll(".player__slider");

// Build out functions
function togglePlay() {
  const method = video.paused ? "play" : "pause";
  // Conditional (ternary) operator to be called
  // video.paused is true?
  // video[method](); -> video.play();
  // video.paused is false?
  // video[method](); -> video.pause();
  video[method]();
}

function updateButton() {
  const icon = this.paused ? "►" : "❚ ❚";
  // reference the user-created toggle button
  // textContent is built into JS, referencing the text and all descendants
  toggle.textContent = icon;
}

function skip() {
  // this.dataset gets the attached user-classes to the input
  // parseFloat() parses a string and returns a floating point number
  video.currentTime += parseFloat(this.dataset.skip);
}

// Hook up event listeners
// the pre-variable is user-created
video.addEventListener("click", togglePlay);
video.addEventListener("play", updateButton);
video.addEventListener("pause", updateButton);
toggle.addEventListener("click", togglePlay);
// considers each skip button
skipButtons.forEach(button => button.addEventListener("click", skip));

// 10:15 timestamp
