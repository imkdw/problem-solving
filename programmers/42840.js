// https://school.programmers.co.kr/learn/courses/30/lessons/42840

function solution(answers) {
  const patterns = [
    [1, 2, 3, 4, 5],
    [2, 1, 2, 3, 2, 4, 2, 5],
    [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],
  ];

  const scores = patterns.map((pattern, index) => {
    return answers.reduce((score, answer, index) => {
      return score + (answer === pattern[index % pattern.length] ? 1 : 0);
    }, 0);
  });

  const maxScore = Math.max(...scores);
  return scores.reduce((result, score, index) => {
    if (score === maxScore) {
      result.push(index + 1);
    }

    return result;
  }, []);
}

console.log(solution([1, 2, 3, 4, 5]));
console.log(solution([1, 3, 2, 4, 2]));
