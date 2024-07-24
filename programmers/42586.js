function solution(progresses, speeds) {
  const result = [];
  const days = [];

  progresses.forEach((item, index) => {
    const remainingWork = 100 - item;
    const daysNeeded = Math.ceil(remainingWork / speeds[index]);
    days.push(daysNeeded);
  });

  let count = 0;
  let maxDay = days[0];
  days.forEach((item) => {
    if (item > maxDay) {
      if (count > 0) {
        result.push(count);
      }
      count = 1;
      maxDay = item;
    } else {
      count++;
    }
  });

  if (count > 0) {
    result.push(count);
  }

  return result;
}

console.log(solution([93, 30, 55], [1, 30, 5]));
console.log(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]));
