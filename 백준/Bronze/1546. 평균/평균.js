const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let l = Number(input[0]);
let nums = input[1].split(' ').map(Number);
let M = Math.max(...nums);

let newNums = [];
nums.forEach((num) => {
  newNums.push((num*10000)/(M*100));
});

let sum = newNums.reduce((acc, curr) => acc + curr, 0);
console.log(sum/l)