# ODD NOTES

## ???

- Website vs web application is that one doesn't use a back-end, one does, respectively.
  - Not much of a difference though, it's the same term.
- Code splitting.

```js
// before
import { add } from "./math";

console.log(add(16, 26));
```

```js
// after
import("./math").then(math => {
  console.log(math.add(16, 26));
});
```
