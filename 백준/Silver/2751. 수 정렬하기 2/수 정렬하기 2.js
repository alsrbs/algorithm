const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let n = Number(input[0]);
let arr = [];
for (let i = 1; i <= n; i++) {
  arr.push(Number(input[i]));
}


// 병합 정렬 수행
function merge(arr, left, mid, right) {
  let i = left;
  let j = mid + 1;
  let k = left;

  while (i <= mid && j <= right) {
    if (arr[i] <= arr[j]) sorted[k++] = arr[i++];
    else sorted[k++] = arr[j++];
  }
  
  // 왼쪽 배열에 대한 처리가 다 끝난 경우
  if (i > mid) {
    for (; j <= right; j++) sorted[k++] = arr[j];
  }
  // 오른쪽 배열에 대한 처리가 다 끝난 경우
  else {
    for (; i <= mid; i++) sorted[k++] = arr[i];
  }
  // 정렬된 배열 결과를 원본 배열에 반영하기
  for (let x = left; x <= right; x++) {
    arr[x] = sorted[x];
  }
}


// 병합 정렬
function mergeSort(arr, left, right) {
  if (left < right) {
    let mid = parseInt((left + right) / 2); // 2개의 부분 배열로 분할
    mergeSort(arr, left, mid); // 왼쪽 부분 배열 정렬
    mergeSort(arr, mid + 1, right); // 오른쪽 부분 배열 정렬
    merge(arr, left, mid, right); // 정렬된 2개의 배열을 하나로 병합
  }
}


let sorted = Array.from({ length: arr.length }, () => 0); // 임시 정렬 배열 정의
mergeSort(arr, 0, arr.length - 1);

// 정렬된 결과를 출력
let answer = "";
for (let i = 0; i < arr.length; i++) {
  answer += arr[i] + '\n';
}

console.log(answer);
