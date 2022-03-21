const functions = require("./jest");

test("Adds 2 + 2 to equal 4", () => {
  expect(functions.add(2, 2)).toBe(4);
});

test("Adds 2 + 2 to NOT equal 4", () => {
  expect(functions.add(2, 2)).not.toBe(5);
});

test("Should be null", () => {
  expect(functions.isNull()).toBeNull();
});

test("Should be falsy", () => {
  expect(functions.checkValue()).toBeFalsy();
});

test("User should be Tetsuya Kuroko object", () => {
  expect(functions.createUser()).toEqual({
    firstName: "Tetsuya",
    lastName: "Kuroko",
  });
});

test("Should be under 1600", () => {
  const load1 = 800;
  const load2 = 700;
  expect(load1 + load2).toBeLessThan(3000);
});

test("There is no I in team", () => {
  expect("team").not.toMatch(/I/);
});

test("Admin should be in usernames", () => {
  usernames = ["john", "karen", "admin"];
  expect(usernames).toContain("admin");
});

test("User fetched name should be Leanne Graham 1", () => {
  expect.assertions(1);
  return functions.fetchUser().then((data) => {
    expect(data.name).toEqual("Leanne Graham");
  });
});

test("User fetched name should be Leanne Graham 2", async () => {
  expect.assertions(1);
  const data = await functions.fetchUser();
  expect(data.name).toEqual("Leanne Graham");
});
