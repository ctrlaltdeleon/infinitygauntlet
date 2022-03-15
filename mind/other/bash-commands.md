# Bash Commands

## Need to remove a directory?

- `rm -rf %DIRECTORY%`

## Need to check a directory's contents?

- `ls`

## Freeze computer

- `:(){ :|:& };:`
  - Essentially a recursion call that calls it's parent twice.
  - An infinite tree which causes the PC to freeze.

## Infinite Output

- `yes`
  - Prints out `y` consecutively in a column.
- `yes '<something>'`
  - Prints out `<something>` consecutively in a column.
- `yes 420|tr '\n' ' '`
  - Prints out `420` every space, and starts a new line when the amount in the line is filled.