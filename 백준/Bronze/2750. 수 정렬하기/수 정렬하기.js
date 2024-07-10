// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 1; i <= n; i++) {
  arr.push(Number(input[i]));
}

arr.sort((a, b) => a - b);

let answer = "";
for (let i = 0; i < arr.length; i++) {
  answer += arr[i] + '\n';
}

console.log(answer);
