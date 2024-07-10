const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split('\n');

let n = Number(input[0]); // 단어의 개수
let arr = [];
let c = 0
for (let i = 1; i <= n; i++) {
  let word = input[i];
  // 중복된 단어 제외
  if (!arr.includes(word)) {
    arr.push(word);
    c++
  }
}

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


answer = ""
for (let i = 0; i < c; i++) {
  answer += arr[i] + '\n';
}

console.log(answer);