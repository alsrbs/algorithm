const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split('');

// 오름차순 정렬
input.sort((a, b) => b - a);

// 배열을 문자열로 변환
let answer = input.join('');

console.log(answer);