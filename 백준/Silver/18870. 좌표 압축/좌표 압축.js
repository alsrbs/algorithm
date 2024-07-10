const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split('\n');

let n = Number(input[0]);
let nList = input[1].split(' ');

let arr = []; // 원본 숫자 배열을 저장할 배열
let arrSort = []; // 정렬할 숫자 배열을 저장할 배열

// 숫자 리스트를 순회하며 숫자로 변환하여 arr와 arrSort에 추가
for (let i = 0; i < n; i++) {
  x = Number(nList[i]);
  arr.push(x);
  arrSort.push(x);
}

// 정렬된 배열에서 중복된 값을 제거하여 고유한 값만 남김
arrSort = [...new Set(arrSort)];

// arrSort 배열을 오름차순으로 정렬
arrSort.sort((a, b) => a - b);

// 각 숫자의 압축된 인덱스를 저장할 객체
let arrDic = {};
for (let i = 0; i < n; i++) {
  arrDic[arrSort[i]] = i;
}

let answer = "";
for (let i = 0; i < n; i++) {
  answer += arrDic[arr[i]] + ' ';
}

console.log(answer);