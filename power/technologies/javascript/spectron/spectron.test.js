const Application = require("spectron").Application; // `Spectron`'s application driver.
const assert = require("assert"); // `Node.js`'s built in assertion library.
const electronPath = require("electron"); // Locally installed development version of `Electron`.
const path = require("path"); // `Node.js`'s helper utility for working with file paths.
const spectronKeys = require("spectron-keys");

const app = new Application({
  path: electronPath,
  args: [path.join(__dirname, "..")], // Points to root directory of application as a starting point.
});

/**
 * This function tests the application.
 * @param {none}
 * @returns {App} Returns test conclusion.
 * @example Show an example here.
 */
describe("Application launches! 🚀", function() {
  this.timeout(10000);

  beforeEach(() => {
    return app.start();
  });

  afterEach(() => {
    if (app && app.isRunning()) {
      return app.stop();
    }
  });

  it("on add button click a new item should be made ", async () => {
    await app.client
      // #addButton.click({ button: 2, x: 30, y: 50 })
      // .click("#myButton", { button: 2, x: 50, y: 50 })
      .click("#myButton")
      .pause(1000)
      .keys(spectronKeys.mapAccelerator("Shift+F10"))
      .pause(1000)
      .click("#myButton")
      .pause(3000)
      .keys(spectronKeys.mapAccelerator("Shift"));
    const text = await app.client.getText("#someText");
    return assert.equal(text, "I was clicked");
  });

  it("shows an initial window", async () => {
    const count = await app.client.getWindowCount();
    return assert.equal(count, 1);
  });

  it("has the correct title", async () => {
    const title = await app.client.waitUntilWindowLoaded().getTitle();
    return assert.equal(title, "React App"); // `npm run start` first.
  });

  it("does not have the developer tools open", async () => {
    const devToolsAreOpen = await app.client
      .waitUntilWindowLoaded()
      .browserWindow.isDevToolsOpened();
    return assert.equal(devToolsAreOpen, false);
  });

  it('has a link named "Learn React!"', async () => {
    const text = await app.client.getText(".App-link"); // Has to be a class or id.
    return assert.equal(text, "Learn React!");
  });

  it('should only have 1 "Learn React!" link', async () => {
    await app.client.waitUntilWindowLoaded();
    // `$` = `document.querySelector`
    // `$$` = `document.querySelectorAll`
    const link = await app.client.$$(".App-link");
    return assert.equal(link.length, 1);
  });

  it("when link is clicked, should have 2 windows open", async () => {
    await app.client.waitUntilWindowLoaded();
    await app.client.click(".App-link").pause(2000);
    const count = await app.client.getWindowCount();
    return assert.equal(count, 2);
  });

  // it("right-click", async () => {
  //   await app.client.waitUntilWindowLoaded();
  //   await app.client.click({"#myButton", button: "right"});
  // });

  // Writing text.

  // it("should have the correct text in a new clipping", async () => {
  //   await app.client.waitUntilWindowLoaded();
  //   await app.electron.clipboard.writeText("Vegan Ham");
  //   await app.client.click("#copy-from-clipboard");
  //   const clippingText = await app.client.getText(".clipping-text");
  //   return assert.equal(clippingText, "Vegan Ham");
  // });

  // it("should write the clipping text to the clipboard", async () => {
  //   await app.client.waitUntilWindowLoaded();
  //   await app.electron.clipboard.writeText("Vegan Ham");
  //   await app.client.click("#copy-from-clipboard");
  //   await app.electron.clipboard.writeText("Something different");
  //   await app.client.click(".copy-clipping");
  //   const clipboardText = await app.electron.clipboard.readText();
  //   return assert.equal(clipboardText, "Vegan Ham");
  // });
});
