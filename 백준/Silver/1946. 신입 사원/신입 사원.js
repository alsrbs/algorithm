const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let t = parseInt(input[0]);  // 테스트 케이스 수
let idx = 1;  // 현재 처리할 줄의 인덱스

for (let _ = 0; _ < t; _++) {
    let n = parseInt(input[idx]);  // 각 테스트 케이스에서 면접자의 수
    let arr = [];

    // 면접자의 점수 입력받기
    for (let i = 1; i <= n; i++) {
        const scores = input[idx + i].split(' ').map(Number);
        arr.push(scores);
    }

    // 1차 점수를 기준으로 오름차순 정렬
    arr.sort((a, b) => a[0] - b[0]);

    let ans = 1;  // 첫 번째 지원자는 항상 선발됨
    let bestSecondScore = arr[0][1];  // 현재까지의 최소 2차 점수

    // 두 번째 지원자부터 검사
    for (let i = 1; i < n; i++) {
        if (arr[i][1] < bestSecondScore) {
            ans++;  // 더 나은 2차 점수를 가진 사람을 선발
            bestSecondScore = arr[i][1];  // 최소 2차 점수 업데이트
        }
    }

    console.log(ans);  
    idx += n + 1;  
}
