const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]); 
const arr = [];
for (let i = 1; i <= n; i++) arr.push(input[i].split(" ").map(Number));

// 종료 시간 기준으로 정렬
arr.sort();
arr.sort((a, b) => a[1] - b[1]);

let cur = 0, result = 1;

for (let i = 1; i < n; i++) {
    // 이전 작업의 종료 시간이 다음 작업의 시작 시간보다 작거나 같으면
    if (arr[cur][1] <= arr[i][0]) {
        cur = i; // 다음 작업 선택
        result += 1; // 완료된 작업 카운트 증가
    }
}

console.log(result);
