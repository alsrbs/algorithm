const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let nums = input.map(Number)
let answer = new Set();
for (let i = 0; i <= 9; i++) {
  answer.add(nums[i]%42);
}
console.log(answer.size);