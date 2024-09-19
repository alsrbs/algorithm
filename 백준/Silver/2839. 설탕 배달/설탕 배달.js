const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString();

let n = Number(input);
let c = 0;

while (n >= 0) {
    if (n % 5 === 0) {
        console.log(n / 5 + c);
        return; // 결과를 출력한 후 종료
    }
    n -= 3;
    c += 1;
}

console.log(-1); // 조건을 만족하지 못한 경우
