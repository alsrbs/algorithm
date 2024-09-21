const fs = require("fs");

const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);
const roads = input[1].split(" ").map(Number);
const citys = input[2].split(" ").map(Number);

let current = BigInt(citys[0]);  // 첫 도시의 기름값
let result = BigInt(0);  // 결과도 BigInt로 초기화

for (let i = 0; i < n - 1; i++) {
    const cityPrice = BigInt(citys[i]);  // BigInt로 변환
    if (current > cityPrice) {  
        current = cityPrice;  // 더 저렴한 기름값으로 갱신
    }
    result += current * BigInt(roads[i]);  // 현재 기름값으로 해당 도로 비용 계산
}

console.log(result.toString());  // BigInt 값을 출력할 때는 .toString() 사용
