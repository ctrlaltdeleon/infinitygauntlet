# 12-31

# 12-30

# 12-29

# 12-28

# 12-27

# 12-26

# 12-25

# 12-24

# 12-23

# 12-22

# 12-21

# 12-20

# 12-19

# 12-18

# 12-17

# 12-16

# 12-15

# 12-14

# 12-13

# 12-12

# 12-11

# 12-10

# 12-9

# 12-8

# 12-7

# 12-6

# 12-5

# 12-4

# 12-3

# 12-2

# 12-1

# 11-30

# 11-29

# 11-28

# 11-27

# 11-26

# 11-25

# 11-24

# 11-23

# 11-22

# 11-21

# 11-20

# 11-19

# 11-18

# 11-17

# 11-16

# 11-15

# 11-14

# 11-13

# 11-12

# 11-11

# 11-10

# 11-9

# 11-8

# 11-7

# 11-6

# 11-5

# 11-4

# 11-3

# 11-2

# 11-1

# 10-31

# 10-30

# 10-29

# 10-28

# 10-27

# 10-26

# 10-25

# 10-24

# 10-23

# 10-22

# 10-21

# 10-20

# 10-19

# 10-18

# 10-17

# 10-16

# 10-15

# 10-14

# 10-13

# 10-12

# 10-11

# 10-10

# 10-9

# 10-8

# 10-7

# 10-6

# 10-5

# 10-4

# 10-3

# 10-2

# 10-1

# 9-30

# 9-29

# 9-28

# 9-27

# 9-26

# 9-25

# 9-24

# 9-23

# 9-22

# 9-21

# 9-20

# 9-19

# 9-18

# 9-17

# 9-16

# 9-15

# 9-14

# 9-13

# 9-12

# 9-11

# 9-10

# 9-9

# 9-8

# 9-7

# 9-6

# 9-5

# 9-4

# 9-3

# 9-2

# 9-1

# 8-31

# 8-30

# 8-29

# 8-28

# 8-27

# 8-26

# 8-25

# 8-24

# 8-23

# 8-22

# 8-21

# 8-20

# 8-19

# 8-18

# 8-17

# 8-16

# 8-15

# 8-14

# 8-13

# 8-12

# 8-11

# 8-10

# 8-9

# 8-8

# 8-7

# 8-6

# 8-5

# 8-4

# 8-3

# 8-2

# 8-1

# 7-31

# 7-30

# 7-29

# 7-28

# 7-27

# 7-26

# 7-25

# 7-24

# 7-23

# 7-22

# 7-21

# 7-20

# 7-19

# 7-18

# 7-17

# 7-16

# 7-15

# 7-14

# 7-13

# 7-12

# 7-11

# 7-10

# 7-9

# 7-8

# 7-7

# 7-6

# 7-5

# 7-4

# 7-3

# 7-2

# 7-1

# 6-30

# 6-29

# 6-28

# 6-27

# 6-26

# 6-25

# 6-24

# 6-23

# 6-22

# 6-21

# 6-20

# 6-19

# 6-18

# 6-17

# 6-16

# 6-15

# 6-14

# 6-13

# 6-12

# 6-11

# 6-10

# 6-9

# 6-8

# 6-7

# 6-6

# 6-5

# 6-4

# 6-3

# 6-2

# 6-1

# 5-31

# 5-30

# 5-29

# 5-28

# 5-27

# 5-26

# 5-25

# 5-24

# 5-23

# 5-22

# 5-21

# 5-20

# 5-19

# 5-18

# 5-17

# 5-16

# 5-15

# 5-14

# 5-13

# 5-12

# 5-11

# 5-10

# 5-9

# 5-8

# 5-7

# 5-6

# 5-5

# 5-4

# 5-3

# 5-2

# 5-1

# 4-30

# 4-29

# 4-28

# 4-27

# 4-26

# 4-25

# 4-24

# 4-23

# 4-22

# 4-21

# 4-20

# 4-19

# 4-18

# 4-17

# 4-16

# 4-15

# 4-14

# 4-13

# 4-12

# 4-11

# 4-10

# 4-9

# 4-8

# 4-7

# 4-6

# 4-5

# 4-4

# 4-3

# 4-2

# 4-1

- What is circular importing?
  - When a package you're importing and the file name are the same.

# 3-31

- Why use `lambda` functions? (Also known as `anonymous functions`)

```py
# Imagine...

def key(x):
    return x[1]

# Appears 300 lines away from...

[(1,2), (3,1), (5,10), (11,-3)].sort(key)

# What does key do? There's really no indication.

[(1,2), (3,1), (5,10), (11,-3)].sort(lambda x: x[1])

# This shows clearly, "oh, it sorts by the the x[1] value of each tuple within the list.
# We expect -3, 1, 2, 10 which is the result.
# Result: [(11, -3), (3, 1), (1, 2), (5, 10)]
```

# 3-30

# 3-29

- `Pycharm` vs `VS Code`?
  - In terms of `Python`, use `Pycharm`.
  - In terms of customizability and full language use, use `VS Code`.
- What's an `AVSC` file?
  - An Apache Avro Schema.
- What's a schema?
  - A blueprint of what data is supposed to be in there.
- What's in an `AVSC`?
  - `"type"`
    - `"record"`
    - `["double", "null"]`
    - `["string", "null"]`
    - `[ {...}, "null" ]`
  - `"name"`
    - Seems like you can put anything here.
  - `"namespace"`
    - Seems like references to other things?
    - "com.hello.fuse.model.Detection.Detection"
  - `"fields"`
    - Seems to always be an array of objects?
    - Holds an object with properties `"name"` and `"type"`.
- How to install packages into `Pycharm`?
  - There's a tab at the bottom called "Python Packages".

# 3-28

- In `JavaScript`, one can combine objects like so:

```js
const newObject = { ...object1, ...object2 };
// Whatever is in object2 will overwrite object1 if they have the same property keys.
```

- What is an object really?
  - They are associative arrays.
  - They store properties.
  - These properties are usually depicted by key to value pairs.
- Working on a new project where we get raw data => JSON => CSV/AVRO
  - Raw data => ???
  - JSON => JavaScript Object Notation (Human-readable text to store and transmit data objects)
  - CSV => Comma Separated Values (Stores values in a spreadsheet-like way)
  - Avro => Data serialization framework (Similar to JSON and XML, but it's in binary format designed for speed, not human readable)

# 3-27

# 3-26

# 3-25

# 3-24

# 3-23

# 3-22

- Done with fixing the infinity gauntlet!

# 3-21

# 3-20

# 3-19

# 3-18

# 3-17

# 3-16

# 3-15

# 3-14

# 3-13

# 3-12

# 3-11

# 3-10

# 3-9

# 3-8

# 3-7

# 3-6

# 3-5

# 3-4

# 3-3

# 3-2

# 3-1

# 2-29

# 2-28

# 2-27

# 2-26

# 2-25

# 2-24

# 2-23

# 2-22

# 2-21

# 2-20

# 2-19

# 2-18

# 2-17

# 2-16

# 2-15

# 2-14

# 2-13

# 2-12

# 2-11

# 2-10

# 2-9

# 2-8

# 2-7

# 2-6

# 2-5

# 2-4

# 2-3

# 2-2

# 2-1

# 1-31

# 1-30

# 1-29

# 1-28

# 1-27

# 1-26

# 1-25

# 1-24

# 1-23

# 1-22

# 1-21

# 1-20

# 1-19

# 1-18

# 1-17

# 1-16

# 1-15

# 1-14

# 1-13

# 1-12

# 1-11

# 1-10

# 1-9

# 1-8

# 1-7

# 1-6

# 1-5

# 1-4

# 1-3

# 1-2

# 1-1
