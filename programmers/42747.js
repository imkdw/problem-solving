function solution(citations) {
  return citations.sort((a, b) => b - a).filter((item, index) => item >= index + 1).length;
}

console.log(solution([3, 0, 6, 1, 5]));
