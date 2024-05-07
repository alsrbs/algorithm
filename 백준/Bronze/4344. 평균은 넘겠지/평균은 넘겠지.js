const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

for (let i = 1; i <= input[0]; i++) {
  let data = input[i].split(' ').map(Number)
  let [l, nums] = [data[0], data.slice(1)]
  let sum = nums.reduce((acc, curr) => acc + curr, 0);
  let mean = sum/l

  let c = 0
  for (let j = 0; j <= l; j++) {
    if (mean < nums[j]) {
      c ++
    }
  }

  console.log((c/l*100).toFixed(3) + '%')
}