// https://school.programmers.co.kr/learn/courses/30/lessons/42748

function solution(array, commands) {
  const result = [];
  commands.forEach((command) => {
    const slicedArray = array.slice(command[0] - 1, command[1]).sort((a, b) => a - b);
    result.push(slicedArray[command[2] - 1]);
  });
  return result;
}

console.log(
  solution(
    [1, 5, 2, 6, 3, 7, 4],
    [
      [2, 5, 3],
      [4, 4, 1],
      [1, 7, 3],
    ]
  )
);
