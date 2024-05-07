const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let nums = input[1].split(' ').map(Number);
nums.sort((a, b) => a - b);
console.log(nums[0], nums[input[0] - 1])
