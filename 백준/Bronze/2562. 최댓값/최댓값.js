const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [answer, idx] = [0, 0];
let nums = input.map(Number)
for(let i = 0; i <= 8; i++) {
  if (answer < nums[i]) {
    answer = nums[i];
    idx = i;
  }
}
console.log(answer)
console.log(idx + 1)