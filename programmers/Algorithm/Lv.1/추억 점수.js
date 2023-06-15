function solution(name, yearning, photo) {
  var answer = [];
  const yearningHashMap = {};
  name.forEach((n, index) => {
    yearningHashMap[n] = yearning[index];
  });
  const mapKeys = Object.keys(yearningHashMap);
  photo.forEach((photoArr) => {
    let score = 0;
    photoArr.forEach((p) => {
      if (mapKeys.includes(p)) {
        score += yearningHashMap[p];
      }
    });
    answer.push(score);
  });

  return answer;
}

const result = solution(
  ["may", "kein", "kain", "radi"],
  [5, 10, 1, 3],
  [
    ["may", "kein", "kain", "radi"],
    ["may", "kein", "brin", "deny"],
    ["kon", "kain", "may", "coni"],
  ]
);

console.log(result);
