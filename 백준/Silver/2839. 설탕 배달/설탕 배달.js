const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString();

let n = Number(input);

let result = NaN;
let c = 0;
while (n >= 0) {
    if (n%5 === 0) {
        result = n / 5 + c;
        break; 
    }
    n -= 3;
    c += 1;
}

if (result) {
    console.log(result);
} else {
    console.log(-1);
}
