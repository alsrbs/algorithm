const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

for (let i = 1; i <= input[0]; i++) {
  let [n, st] = input[i].split(' ')
  let result = ''
  st.split('').forEach((s) => {
    result += s.repeat(n)
  })
  console.log(result)
}