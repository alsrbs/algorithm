const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 1; i <= n; i++) {
  let [a, b] = input[i].split(' ');
  arr.push([Number(a), Number(b)]);
}

arr.sort((a, b) => { // y좌표가 증가하는 순 y좌표가 같다면 x좌표가 증가하는 순
  if (a[1] != b[1]) return a[1] - b[1];
  else return a[0] - b[0];
})

answer = "";
for (let point of arr) {
  answer += point[0] + " " + point[1] + '\n';
}

console.log(answer);