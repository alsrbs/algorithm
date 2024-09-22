const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const arr = input[1].split(" ").map(Number);

let flot = Array(Math.max(...arr) + 1).fill(0); 

for (let i = 0; i < n; i++) {
    if (flot[arr[i]] > 0) {
        flot[arr[i]] -= 1;
        flot[arr[i] - 1] += 1;
    } else {
        flot[arr[i] - 1] += 1;
    }
}

let totalOperations = 0;
for (let i = 0; i < flot.length; i++) {
    totalOperations += flot[i];
}

console.log(totalOperations);