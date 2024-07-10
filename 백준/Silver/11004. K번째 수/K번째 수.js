// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, k] = input[0].split(' ').map(Number);
let arr = input[1].split(' ').map(Number);

arr.sort((a, b) => a - b);

console.log(arr[k-1]);
