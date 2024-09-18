const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim();

const m = input.split('-');

function sum(arr) {
    return arr.reduce((acc, cur) => acc + cur, 0);
}

// 첫 번째 그룹은 무조건 더하고, 나머지는 뺍니다.
let result = sum(m[0].split('+').map(Number));  
for (let i = 1; i < m.length; i++) {  // 첫 번째 그룹은 이미 더했으니, 나머지 그룹은 뺌
    const x = sum(m[i].split('+').map(Number));
    result -= x;
}

console.log(result);