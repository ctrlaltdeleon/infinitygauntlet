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
  console.log(
    "%cSOMEONE OUT THERE CARES ABOUT YOU",
    "font-size:40px; background:pink;"
  );
  console.log("me");
  video.currentTime += parseFloat(this.dataset.skip);
}

function handleRangeUpdate() {
  // take the specific video[range] and change the value
  video[this.name] = this.value;
}

function handleProgress() {
  // this is for the visual aspect
  const percent = (video.currentTime / video.duration) * 100;
  // flex-basis CSS that sets the initial main size of a flex item
  progressBar.style.flexBasis = `${percent}%`;
}

function scrub(e) {
  const scrubTime = (e.offsetX / progress.offsetWidth) * video.duration;
  video.currentTime = scrubTime;
}

// Hook up event listeners
// the pre-variable is user-created
video.addEventListener("click", togglePlay);
video.addEventListener("play", updateButton);
video.addEventListener("pause", updateButton);
video.addEventListener("timeupdate", handleProgress);
toggle.addEventListener("click", togglePlay);
// considers each skip button
skipButtons.forEach((button) => button.addEventListener("click", skip));
ranges.forEach((range) => range.addEventListener("change", handleRangeUpdate));
ranges.forEach((range) =>
  range.addEventListener("mousemove", handleRangeUpdate)
);
// this is for the mousemove option, because we need a mousedown before firing or it's constant on hover
let mousedown = false;
// we look at the what's clicked (e) and check offsetX
progress.addEventListener("click", scrub);
progress.addEventListener("mousemove", (e) => mousedown && scrub(e));
progress.addEventListener("mousedown", () => (mousedown = true));
progress.addEventListener("mouseup", () => (mousedown = false));

// Try making fullscreen button
