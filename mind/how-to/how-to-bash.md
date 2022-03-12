# HOW TO BASH

Last updated: 2021-09-10

## Chapters

1. Introduction
2. Commands
3. Fun Stuff
   1. Computer Freeze
   2. Infinite Output
4. Conclusion
   1. My Take

## 1: Introduction

- This is a simple guide of how to bash.

## 2: Commands

- Need to remove a directory?
  - `rm -rf %DIRECTORY%`
- Need to check a directory's contents?
  - `ls`

## 3: Fun Stuff

- Some fun tidbits.

## 3.1: Computer Freeze

- `:(){ :|:& };:`
  - Essentially a recursion call that calls it's parent twice.
  - An infinite tree which causes the PC to freeze.

## 3.2: Infinite Output

- `yes`
  - Prints out `y` consecutively in a column.
- `yes '<something>'`
  - Prints out `<something>` consecutively in a column.
- `yes 420|tr '\n' ' '`
  - Prints out `420` every space, and starts a new line when the amount in the line is filled.

## 4: Conclusion

- Thank you.

## 4.1: My Take

- N/A