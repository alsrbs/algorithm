const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split('\n');

let n = Number(input[0]);
let nList = input[1].split(' ').map(Number);

// 정렬된 배열에서 중복된 값을 제거하여 고유한 값만 남김
let arr = [...new Set(nList)];

// arrSort 배열을 오름차순으로 정렬
arr.sort((a, b) => a - b);

// 각 숫자의 압축된 인덱스를 저장할 객체
let arrDic = {};
for (let i = 0; i < n; i++) {
  arrDic[arr[i]] = i;
}

let answer = "";
for (let i = 0; i < n; i++) {
  answer += arrDic[nList[i]] + ' ';
}

console.log(answer);