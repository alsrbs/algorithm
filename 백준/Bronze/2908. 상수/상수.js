const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

function reverseString(str) {
  return str.split('').reverse().join('');
}

let [a, b] = input
console.log(Math.max(reverseString(a), reverseString(b)))