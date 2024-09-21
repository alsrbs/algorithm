const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const roads = input[1].split(" ").map(Number);
const citys = input[2].split(" ").map(Number);

let current = citys[0];
let result = citys[0] * roads[0];

for (let i = 1; i < n-1; i++) {
    if (current > citys[i]) {
        current = citys[i];
    } 
    result += current * roads[i];
}

console.log(result);