const readline = require("readline");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

let input = [];

rl.on("line", (line) => {
  input.push(line);
  if (input.length === 3) {
    console.log(+input[0] + +input[1] - +input[2]);
    console.log(+(input[0] + input[1]) - +input[2]);
    rl.close();
  }
});

rl.on("close", () => {
  process.exit();
});
