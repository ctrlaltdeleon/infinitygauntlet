# HOW TO USE BASH

1. Introduction
2. Commands
3. Scenarios
   1. Computer Freeze
   2. Infinite Output
## Commands

Need to remove a directory?

```bash
rm -rf %DIRECTORY%
```

Need to check the contents of the area you're in?

```bash
ls
```

## Computer Freeze

- `:(){ :|:& };:`
  - Essentially a recursion call that calls it's parent twice, so an infinite tree which causes the PC to freeze.

## Infinite Output

- `yes`
  - Prints out `y` consecutively in a column.
- `yes '<something>`
  - Prints out `<something>` consecutively in a column.
- `yes 420|tr '\n' ' '`
  - Prints out `420` every space, and starts a new line when the amount in the line is filled.

## Conclusion:

- Thank you.