// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

let arr = input.map(Number)

// 선택 정렬
function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let minindex = i; // 가장 작은 원소의 인덱스
    for (let j = i + 1; j < arr.length; j ++) {
      if (arr[minindex] > arr[j]) minindex = j;
    }
    let temp = arr[i];
    arr[i] = arr[minindex];
    arr[minindex] = temp;
  }
}

// 오름차순 정렬 수행
selectionSort(arr);

let answer = "";
for (let i = 0; i < arr.length; i++) {
  answer += arr[i] + " ";
}
console.log(answer)