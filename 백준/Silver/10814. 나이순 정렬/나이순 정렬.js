const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 1; i <= n; i++) {
  let a = input[i].split(' ');
  arr.push(a);
}

// 첫 번째 요소를 기준으로 정렬
arr.sort((a, b) => a[0] - b[0]);

// 배열을 문자열로 변환
let answer = arr.map(pair => pair.join(' ')).join('\n');

console.log(answer);