// https://school.programmers.co.kr/learn/courses/30/lessons/161989

/**
 *
 * @param {number} n
 * @param {number} m
 * @param {number[]} section
 */
function solution(n, m, section) {
  let count = 0;
  let current = 0;

  for (const wall of section) {
    if (current < wall) {
      count += 1;
      current = wall + m - 1;
    }
  }

  return count;
}

console.log(solution(8, 4, [2, 3, 6]));
console.log(solution(5, 4, [1, 3]));
console.log(solution(4, 1, [1, 2, 3, 4]));
console.log(solution(20, 4, [2, 6, 10]));
