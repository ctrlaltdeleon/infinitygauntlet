# Google Script Count Color

```cs
/**
* @param {range} countRange Range to be evaluated
* @param {range} colorRef Cell with background color to be searched for in countRange
* @return {number}
* @example { =COUNTCOLOR(A2:A5,E5) }
*/

function COUNTCOLOR(countRange, colorRef) {
  // Use formula variable to link to `rangeA1Notation` and `colorCellA1Notation`.
  var activeRange = SpreadsheetApp.getActiveRange();
  var activeSheet = activeRange.getSheet();
  var formula = activeRange.getFormula();
  
  // We want the backgrounds and the values for the `countRange`.
  var rangeA1Notation = formula.match(/\((.*)\,/).pop();
  var range = activeSheet.getRange(rangeA1Notation);
  var bg = range.getBackgrounds();
  var values = range.getValues();
  
  // We want the background for the `colorRef`.
  var colorCellA1Notation = formula.match(/\,(.*)\)/).pop();
  var colorCell = activeSheet.getRange(colorCellA1Notation);
  var color = colorCell.getBackground();
  
  var count = 0;
  
  // Check columns.
  for(var i=0;i<bg.length;i++)
    // Check rows.
    for(var j=0;j<bg[0].length;j++)
      // If the cell we're checking is the color being referenced, increment.
      if(bg[i][j] == color)
        count += 1;
  
  return count;
};
```