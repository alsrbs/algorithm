const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let nums = input.map(Number)
let Max_num = Math.max(...nums)
console.log(Max_num)
console.log(nums.indexOf(Max_num) + 1)