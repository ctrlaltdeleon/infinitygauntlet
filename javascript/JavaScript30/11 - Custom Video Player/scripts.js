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
  if (video.paused) {
    video.play();
  } else {
    video.pause();
  }
}

// Hook up event listeners
