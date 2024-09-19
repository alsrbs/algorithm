const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split(" ");

let a = Number(input[0]);
let b = Number(input[1]);

let result = 1;

while (b > a) {
    if (b % 2 === 0) {
        b /= 2;  // b가 짝수이면 2로 나누기
    } else {
        if (String(b).slice(-1) === '1') {
            b = Number(String(b).slice(0, -1));  // 마지막 자리가 1일 때 제거
        } else {
            break;  // 더 이상 연산이 불가능한 경우
        }
    }
    result += 1;
}

if (b === a) {
    console.log(result);
} else {
    console.log(-1);
}
