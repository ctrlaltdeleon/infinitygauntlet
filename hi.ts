const testObject = {
  a: 1,
  b: {
    c: 2,
    d: {
      e: {
        f: ["s", "hi"],
        g: "s",
      },
      h: {
        i: [
          {
            j: "UNK",
          },
          {
            k: "yeehaw",
          },
        ],
      },
    },
  },
};

/**
 * Flatten a multidimensional object
 *
 * For example:
 *   flattenObject{ a: 1, b: { c: 2 } }
 * Returns:
 *   { a: 1, c: 2}
 */
const flattenObject = (obj, searchForThis) => {
  const flattened = {};
  const found = {
    "FOUND IT": true,
  };

  Object.keys(obj).forEach((key) => {
    const value = obj[key];
    if (typeof value === "object" && value !== null && !Array.isArray(value)) {
      Object.assign(flattened, flattenObject(value));
    } else {
      flattened[key] = value;
    }
  });

  for (const obj in flattened) {
    console.log(typeof flattened[obj], flattened[obj]);
    if (flattened[obj] === searchForThis) {
      return found;
    }
    // elseif (typeof flattened[obj] === )
  }

  return flattened;
};

// Render example
document.getElementById("before").innerHTML = JSON.stringify(
  testObject,
  null,
  2
);
document.getElementById("after").innerHTML = JSON.stringify(
  flattenObject(testObject, "UNK"),
  null,
  2
);
