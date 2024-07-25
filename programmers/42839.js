// https://school.programmers.co.kr/learn/courses/30/lessons/42839

// 모든 가능한 순열을 생성하는 함수

// 소수인지 확인하는 함수
function isPrime(num) {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
}

function solution(numbers) {
  const nums = numbers.split("");
  const permutations = new Set();

  function getPermutations(arr, fixed) {
    if (arr.length > 0) {
      for (let i = 0; i < arr.length; i++) {
        const newFixed = fixed + arr[i];
        const copyArr = [...arr];
        copyArr.splice(i, 1);
        permutations.add(Number(newFixed));
        getPermutations(copyArr, newFixed);
      }
    }
  }

  // 순열 생성
  getPermutations(nums, "");

  // 소수 개수 세기
  return [...permutations].filter(isPrime).length;
}

console.log(solution("17")); // 3
console.log(solution("011")); // 2
