// DOM elements.
const resultEl = document.getElementById("result");
const lengthEl = document.getElementById("length");
const lowercaseEl = document.getElementById("lowercase");
const uppercaseEl = document.getElementById("uppercase");
const numbersEl = document.getElementById("numbers");
const symbolsEl = document.getElementById("symbols");
const generateEl = document.getElementById("generate");
const clipboardEl = document.getElementById("clipboard");

const randomFunc = {
  lower: getRandomLower,
  upper: getRandomUpper,
  number: getRandomNumber,
  symbol: getRandomSymbol,
};

// Generate event listen.
generateEl.addEventListener("click", () => {
  // The `+` parse the `lengthEl.value` into a number instead of a string.
  const length = +lengthEl.value;
  const hasLower = lowercaseEl.checked;
  const hasUpper = uppercaseEl.checked;
  const hasNumber = numbersEl.checked;
  const hasSymbol = symbolsEl.checked;
  resultEl.innerText = generatePassword(
    hasLower,
    hasUpper,
    hasNumber,
    hasSymbol,
    length,
  );
});

// Copy password to clipboard.
clipboardEl.addEventListener("click", () => {
  const textarea = document.createElement("textarea");
  const password = resultEl.innerText;

  if (!password) {
    return;
  }

  textarea.value = password;
  document.body.appendChild(textarea);
  textarea.select();
  document.execCommand("copy");
  textarea.remove();
  alert("Password copied to clipboard!");
});

// Generate password function.
function generatePassword(lower, upper, number, symbol, length) {
  // 1. Init password variable.
  // 2. Filter out unchecked types.
  // 3. Loop over length call generator function.
  // 4. Add final password to password variable and return.
  let generatedPassword = "";
  const typesCount = lower + upper + number + symbol;

  // Array of objects.
  const typesArr = [{ lower }, { upper }, { number }, { symbol }].filter(
    // Filter through each object and check the item's value.
    // Item in this case is the `lower`, `upper`, etc.
    item => Object.values(item)[0],
  );

  // If no boxes are checked, make no password.
  if (typesCount === 0) {
    return "";
  }

  for (let i = 0; i < length; i++) {
    // Previous code, but went through a specific order which is not random.
    // typesArr.forEach(type => {
    //   // `funcName` = `lower`, `upper`, etc.
    //   const funcName = Object.keys(type)[0];
    //   generatedPassword += randomFunc[funcName]();
    // });
    const funcName = Object.keys(
      typesArr[Math.floor(Math.random() * typesArr.length)],
    )[0];
    // Executes given `funcName`.
    generatedPassword += randomFunc[funcName]();
  }

  const finalPassword = generatedPassword.slice(0, length);

  return finalPassword;
}

// Generator functions.
// http://www.net-comber.com/charset.html

function getRandomLower() {
  // From ID 97 which is "a" to ID 122 which is "z" pick a random lowercase letter.
  return String.fromCharCode(Math.floor(Math.random() * 26) + 97);
}

function getRandomUpper() {
  // From ID 65 which is "A" to ID 90 which is "Z" pick a random uppercase letter.
  return String.fromCharCode(Math.floor(Math.random() * 26) + 65);
}

function getRandomNumber() {
  // From ID 48 which is "0" to ID 57 which is "9" pick a random number letter.
  return String.fromCharCode(Math.floor(Math.random() * 10) + 48);
}

function getRandomSymbol() {
  const symbols = "!@#$%^&*()[]{};:,.<>/?";
  return symbols[Math.floor(Math.random() * symbols.length)];
}
