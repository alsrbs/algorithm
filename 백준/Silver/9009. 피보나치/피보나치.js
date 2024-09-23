const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const Fibonacci = [0, 1];
for (let i = 2; i < 50; i++) {
    Fibonacci.push(Fibonacci[i - 1] + Fibonacci[i - 2]); 
}

const t = Number(input[0]);
const arr = input.slice(1).map(Number);

for (let i = 0; i < t; i++) {
    let n = arr[i];

    const result = [];
    let idx = 49;
    while (n > 0 && idx > 0) {
        if (Fibonacci[idx] <= n) {
            result.push(Fibonacci[idx]);
            n -= Fibonacci[idx];
        }
        idx--;
    }

    result.sort((a, b) => a - b);

    console.log(result.join(" "));
}