const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0].split(' ')[0]);
let k = Number(input[0].split(' ')[1]);
const coin = input.slice(1);

let result = 0;
for (let i = n - 1; i >= 0; i--) {
    result += parseInt(k / coin[i], 10);  // 동전 개수를 정수로 계산
    k %= coin[i];  // 남은 금액을 갱신
    
}

console.log(result);
