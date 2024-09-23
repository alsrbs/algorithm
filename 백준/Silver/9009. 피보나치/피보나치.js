const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

// 피보나치 수열 미리 계산
const Fibonacci = [0, 1];

// 필요한 범위까지만 계산
for (let i = 2; i < 50; i++) {
    Fibonacci.push(Fibonacci[i - 1] + Fibonacci[i - 2]); 
}

const t = Number(input[0]);
for (let i = 1; i <= t; i++) {
    let n = Number(input[i]);
    const result = [];
    
    // 가장 큰 피보나치 수부터 시작
    for (let idx = Fibonacci.length - 1; idx > 0; idx--) {
        if (Fibonacci[idx] <= n) {
            result.push(Fibonacci[idx]);
            n -= Fibonacci[idx];
        }
    }

    // 결과를 오름차순으로 출력하기 위해 정렬
    console.log(result.reverse().join(" "));    
}