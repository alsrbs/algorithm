const fs = require('fs');
const input = fs.readFileSync("/dev/stdin").toString().split("\n");

const n = Number(input[0]);

function isPalindrome(str, left, right) {
    while (left < right) {
        if (str[left] !== str[right]) {
            return false; 
        }
        left++;
        right--;
    }
    return true; 
}

function canBePalindromeByRemovingOneChar(str) {
    let left = 0;
    let right = str.length - 1;

    while (left < right) {
        if (str[left] !== str[right]) {
            // 서로 다른 문자가 발견되면 한 문자 제거한 경우를 각각 확인
            if (isPalindrome(str, left + 1, right) || isPalindrome(str, left, right - 1)) {
                return 1; // 하나의 문자를 제거해서 회문이 될 수 있음
            } else {
                return 2; // 하나의 문자를 제거해도 회문이 될 수 없음
            }
        }
        left++;
        right--;
    }

    return 0; 
}

for (let i = 1; i <= n; i++) {
    const str = input[i].trim();
    const result = canBePalindromeByRemovingOneChar(str);
    console.log(result);
}
