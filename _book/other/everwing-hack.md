# EVERWING HACK

- Inspect Game.
- Go to Console (If you see "STOP", good job).
- Go to Alice.
- Equip.
- Go to Fiona.
- Above the stop, click the right address (Should be VMxxx:xxx).
- `Prettyify` code.
- Ctrl + F -> InstanceCache.prototype.writeDirtyInstancesToState.
- Find `var i = this.\_cachedKeys[t]` about 3 lines below.
- Click on respective line (the number to the left).
- Click "equip" on Fiona.
- Look to right and open "scope" arrow.
- Click on letter "e".
- Click on "instances".
- `Alt + left` mouse button, opens every entry.
- Look for "currency".
- Update values accordingly (Don't go crazy).
- Uncheck breakpoint.
- Enjoy.

Can also input scripts to modify eggs, note sidekick key names to obtain correct key, for example:

- prismaticusAwakens
  - FC14 --> Stoke, Forge, Bellows
  - LC11 --> Sparx, Sparkene, Sparzelle
  - NC11 --> Eve, Levee, Leavesly
  - SC12 --> Fetora, Miasmus, Mephititus
  - WC15 --> Dew, Dilius, Deliquess
  - PC00 --> Pris, Prima, Prismaticus

Get all new sidekicks

```
var count = e.instances.length - 6;

e.instances[count++].modelID = "Item:sidekick:FC14";
e.instances[count++].modelID = "Item:sidekick:LC11";
e.instances[count++].modelID = "Item:sidekick:NC11";
e.instances[count++].modelID = "Item:sidekick:SC12";
e.instances[count++].modelID = "Item:sidekick:WC15";
e.instances[count++].modelID = "Item:sidekick:PC00";
```

Max sidekicks

```
for (var i = e.instances.length - 6; i < e.instances.length; i++) {
e.instances[i].stats.xp = 125800;
e.instances[i].stats.maturity = 3;
e.instances[i].stats.zodiacBonus = 2;
}
```
