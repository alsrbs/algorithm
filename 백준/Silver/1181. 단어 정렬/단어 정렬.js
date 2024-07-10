const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split('\n');

let n = Number(input[0]); // 단어의 개수
let arr = [];
for (let i = 1; i <= n; i++) {
  arr.push(input[i]);
}

arr = [...new Set(arr)]

// 1. 길이가 짧은 것부터
// 2. 길이가 같으면 사전 순
arr.sort((a, b) => {
  if (a.length != b.length) return a.length - b.length;
  else {
    if (a < b) return -1;
    else if (a > b) return 1;
    else return 0;
  }
})

answer = "";
for (let i = 0; i < arr.length; i++) {
  answer += arr[i] + '\n';
}

console.log(answer);