const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);

let sum = 0;
for (let i = 1; i <= n; i++) {
    sum += i
    if (sum >= n){
        console.log(i - (sum > n ? 1 : 0));  // sum이 n보다 클 때만 i-1 출력
        return;
    }
}
