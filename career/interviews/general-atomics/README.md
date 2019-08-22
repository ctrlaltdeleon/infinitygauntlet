# GENERAL ATOMICS

## Round 1 (Phone)

- 1 hour with Software Engineer (Alex Hay).
- Technical.
- "What is the range of values of a signed 16-bit?"
  - `-(2^16)` to `2^16`
  - `-32768` to `32767`
- "What about the range of values of a unsigned 16-bit?"
  - `0` to `65535`.
- "How would you design a repo with access to mission plans and having clients have access to those mission plans?"
  - Modularity of calls.
  - Giving what the client exactly needs instead of extra fluff.
- "How would you design a certain function if multiple clients were trying to access a single mission plan?"
  - Multithreading.
- "How would you record feedback of a pilot who inputs values at a certain time?"
  - With a dictionary.
  - `{ %TIME_STAMP% : %KEY_PRESSED%, ...}`
- Background of the company culture and the projects to be handled.
  - Mission Assistance Rancho Bernardo.
  - `C#` heavy.

## Round 2 (On-site)

- ?