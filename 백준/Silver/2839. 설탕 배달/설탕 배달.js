const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString();

let n = Number(input);

if ([1, 2, 4, 7].includes(n)) {
    console.log(-1);
} else {
    console.log(Math.floor(n / 5) + Math.floor((n % 5) / 3) + (n % 5) % 3);
}
