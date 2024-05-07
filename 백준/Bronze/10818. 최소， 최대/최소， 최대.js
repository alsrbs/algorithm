const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let nums = input[1].split(' ').map(Number);
console.log(Math.min.apply(null, nums), Math.max.apply(null, nums))

