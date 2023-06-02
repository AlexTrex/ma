var xlsx = require("xlsx");
var fs = require("fs");

var wb = xlsx.readFile("SomeTable.xlsx");

var ws = wb.Sheets[Object.entries(wb.Sheets)[0][0]];

var output = xlsx.utils.sheet_to_json(ws, { header: 1 });

console.log(output);

fs.writeFile(
  "./my.json",

  JSON.stringify(output),

  function (err) {
    if (err) {
      console.error("Crap happens");
    }
  }
);
