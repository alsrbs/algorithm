const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const arr = input.slice(1)[0].split(" ");

arr.sort((a, b) => a - b);

let result = 0;
let c = 0
for (let i = 0; i < arr.length; i++) {
    result += c + Number(arr[i]);
    c += Number(arr[i])
}

console.log(result)