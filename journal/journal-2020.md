# January 22, 2020

- Gym!
  - Chest and triceps.
  - Volleyball.

# January 21, 2020

- What are documentation tools?
  - Documentation.js.
  - JSDoc.
  - Natural Docs.
- Difference between installing local and global?
  - Install a module locally if you're going to require() it.
  - Install a module globally if you're going to run it on the command line.
- Gym!
  - Back and biceps.

# January 20, 2020

- Martin Luther King Jr. Day.

# January 19, 2020

- Ikea.

# January 18, 2020

- Movie!
  - Weathering with you.

# January 17, 2020

- Movie!
  - Star Wars: The Rise of Skywalker.

# January 16, 2020

- What is `Karma`?
  - A testing framework that runs on multiple browsers.
- What is `Picture-In-Picture`?
  - A feature originated from television receivers where it displays a smaller video program alongside the main video program.
- Firefox and Chrome both have Picture-In-Picture options.
- How to remove terminal prompt?
  - `export PS1='>'`
  - Changes the terminal prompt to `>`.
- How to increase a `VirtualBox` disk size?
  - Make sure virtual machines are off.
  - Highlight virtual machine in `VirtualBox`.
  - Go to settings.
  - Go to storage.
  - Click the controller SATA under storage devices.
    - Usually the VDI file.
  - Make sure the information for:
    - Type (format) is VDI or VHD.
    - Details is dynamically allocated.
  - Copy the address location.
  - Open terminal.
  - Change location to the address location, but one folder up.
  - To check contents use `ls -la`.
  - Make a back-up via `cp %FILE_NAME%.VDI %BACK_UP_FILE_NAME%.VDI`.
  - Resize the file `vboxmanage modifyhd %FILE_NAME%.VDI --resize 100000`
    - 100000 is approximately 100 gigabytes.
  - Highlight virtual machine in `VirtualBox`.
  - Go to settings.
  - Go to storage.
  - Click the controller IDE under storage devices.
    - Usually empty.
  - To the side in attributes, change the optical drive to the OS system you used to boot up.
  - Click ok.
  - Start up the virtual machine.
  - Open up GParted in the virtual machine.
  - Click the old memory space.
  - Resize to take all unallocated space.
  - Apply operations.
  - Go back to the controller IDE under storage devices.
  - Remove disk from virtual drive.
  - Enjoy!

# January 15, 2020

- What does `sudo` do in Linux?
  - Superuser do.
  - Best and safest way to elevate privileges to do something by asking for a password.
- Gym!
  - Chest and triceps.

# January 14, 2020

- What is the relationship of `Spectron` to `WebdriverIO` and `Selenium WebDriver`?
  - `Selenium WebDriver` allows developers to write tests that control a web browser so they can test apps from a user's perspective.
  - `WebdriverIO` wraps the `Selenium WebDriver` with a pleasant `JavaScript` API and makes it easy to use from within `Node.js` or an `Electron` application in our case.
  - `Spectron` allows access to `WebdriverIO` with a environment custom-tailored functionality for `Electron` applications.
- What is the primary way to use `Spectron`?
  - Create an `Application` instance.
  - This object includes a number of child objects that allow us to access different parts of the application.
- What are the different parts of `Spectron`?
  - `client`
    - The underlying `WebdriverIO` instance.
  - `electron`
    - `Electron`'s renderer process API.
  - `browserWindow`
    - The currently focused browser window.
  - `webContents`
    - `Electron`'s WebContents API.
  - `mainProcess`
    - Node's process object in the main process.
  - `rendererProcess`
    - Node's process object in the renderer process.
- Is it better to have the front-end and back-end in the same repo or separate repos.
  - Depends.
  - Usually separate repos is desirable due to modularization and scalability.
  - Reasons for same repos is for the engineers to understand the product as a whole.
- How does a standard `Electron` test file look like?

```js
const Application = require("spectron").Application; // `Spectron`'s application driver.
const assert = require("assert"); // `Node.js`'s built in assertion library.
const electronPath = require("electron"); // Locally installed development version of `Electron`.
const path = require("path"); // `Node.js`'s helper utility for working with file paths.

const app = new Application({
  path: electronPath,
  args: [path.join(__dirname, "..")], // Points to root directory of application as a starting point.
});

describe("Application launch", function() {
  this.timeout(10000); // `Mocha`'s default timeout because launching can take a while.

  beforeEach(() => {
    return app.start(); // Starts application before each test.
  });

  afterEach(() => {
    if (app && app.isRunning()) {
      return app.stop(); // Stops the application after each test.
    }
  });

  it("should have 1 window", function() {
    const count = await app.client.getWindowCount();
    return assert.equal(count, 1);
  })
});
```

- What is a callback function?
  - A function where it's accessible by another function.
  - Usually when a certain function is finished, another takes its place.
- Gym!
  - Back and biceps.

# January 13, 2020

- What is `Mocha`?
  - JavaScript test framework running on `Node.js` and in the browser.
- What is `Chai`?
  - A BDD/TDD (Behavioral Driven Development/Technical Driven Development) assertion library for `Node.js`.
  - Makes it easy to express and be readable to anyone.
- How to run scripts after one each other in `Linux`?
  - Use `&` between scripts.
- How to run scripts simultaneously in `Linux`?
  - Use `|` between scripts.
- There are different auto-documentation tools that look at the code and create a `HTML` file from it that's fast and easy to access.
- What is a traditional virtualization?
  - Hardware (Server).
  - Operating System.
  - Hypervisor (Translating system for app to OS).
  - Multiple VMS.
- What is a traditional containerization?
  - Hardware (Server).
  - Operating System.
  - Containers.
- What are the differences between VMs VS. containers?
  - VMs are not as flexible when utilizing resources on the hardware where containers are flexible and use what it needs, not fixed.
- Why use `Docker`?
  - Makes it easy to develop and deploy apps inside neat containers.
- Instead of controlling 1 container at a time, `Docker Compose` is a tool to use to affect multiple containers at once.

# January 12, 2020

- FS Retreat!

# January 11, 2020

- FS Retreat!

# January 10, 2020

- FS Retreat!

# January 9, 2020

- What is `Cucumber`?
  - An open source, multiple language support, that provides BDD tools.
- What is "BDD"?
  - Behavioral Driven Development.
  - Allows for non-technical developers to collaborate more in the development process.

```
Feature: Reset functionality on login page of application.

Scenario: Verification of reset button.
Given... Open the Firefox and launch the application.
When... Enter the Username and Password.
Then... Reset the credential.
```

- What is `Selenium`?
  - Automation browser-based application.
- Electron provide us an easy and fast way to develop native Windows or Mac-OS application.
- React library makes web development more structure and modular by it’s component based approach.
- Combination of Electron and React will be an awesome way to develop desktop application.
- Made a Electron, React, Spectron boilerplate.
  - Needs Jest/Enzyme?

# January 8, 2020

- Gym!
  - Legs and shoulders.

# January 7, 2020

- Looked up insurance options.
- What is `Electron`?
  - A combination of `Chromium`, `Node.js`, and native APIs such as open file dialogs, notifications, etc.
  - Provides a browser window with customizability as opposed to browsers.
- Gym!
  - Chest and triceps.

# January 6, 2020

- Where does one put the `<script>` tag in an `index.html` file?
  - Usually in the `<body>`, towards the very end.
  - This makes sure the DOM is ready to be manipulated before the `JavaScript` goes in.
- What does "DOM" mean?
  - Document Object Model.
  - Treats a `HTML` document as a tree structure.
- Created a password generator in `JavaScript`.
- Gym!
  - Volleyball.

# January 5, 2020

- ?

# January 4, 2020

- Gym!
  - Back and biceps.
- Watched Japanese wrestling.

# January 3, 2020

- ?

# January 2, 2020

- Work.
- Fixed all my repos and learned a bunch `JavaScript` related.
- What does it mean to `amend` a commit?
  - To combine the current and previous commit into 1.

# January 1, 2020

- Happy new year!
