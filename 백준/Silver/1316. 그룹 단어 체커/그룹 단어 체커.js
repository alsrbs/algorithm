const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

let cnt = 0;
for (let i = 1; i <= input[0]; i++) {
  
  let s = input[i].split('\r')[0];
  let st = s[0];
  let idx = 0;
  let dic = new Set();
  dic.add(s[0]);

  for (let j = 1; j <= s.length - 1; j++) {
    dic.add(s[j]);
    if (st[idx] !== s[j]) {
      st += s[j];
      idx++;
    }
  }

  if (dic.size === idx + 1) {
    cnt++;
  }
}

console.log(cnt);