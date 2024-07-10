const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split('\n');

let n = Number(input[0]);
let arr = input[1].split(' ').map(Number);

// 정렬된 배열에서 중복된 값을 제거하여 고유한 값만 남김
let uniqueArray = [...new Set(arr)];

// arrSort 배열을 오름차순으로 정렬
uniqueArray.sort((a, b) => a - b);

// 각 숫자의 압축된 인덱스를 저장할 객체
let myMap = new Map;
for (let i = 0; i < n; i++) {
  myMap.set(uniqueArray[i], i);
}

let answer = "";
for (let i = 0; i < n; i++) {
  answer += myMap.get(arr[i]) + ' ';
}

console.log(answer);