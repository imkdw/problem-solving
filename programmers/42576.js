function solution(participant, completion) {
  const participantCount = {};
  participant.forEach((item) => {
    if (item in participantCount) {
      participantCount[item]++;
    } else {
      participantCount[item] = 1;
    }
  });

  completion.forEach((item) => {
    if (item in participantCount) {
      participantCount[item]--;
    }
  });

  const result = Object.entries(participantCount).find((item) => item[1] > 0);
  return result[0];
}

console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"]));
console.log(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]));
console.log(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]));
