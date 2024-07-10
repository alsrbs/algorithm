const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 1; i <= n; i++) {
  let a = input[i].split(' ');
  arr.push(a);
}

arr.sort((a, b) => a[0] - b[0]);

let answer = "";
for (let i = 0; i < n; i++) {
  answer += arr[i][0] + ' ' + arr[i][1] + '\n';
}

console.log(answer);