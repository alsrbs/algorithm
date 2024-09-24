const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let [n, k] = input[0].split(" ").map(Number);

// k개의 숫자를 사용할 때 최소 필요한 합
const sumOfFirstKNumbers = (k * (k + 1)) / 2;

if (sumOfFirstKNumbers > n) {
    console.log(-1);
} else {
    console.log((n - sumOfFirstKNumbers) % k === 0 ? k - 1 : k);
}
