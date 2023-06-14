function solution(players, callings) {
  // 플레이어 인덱스 저장용 해시맵
  const playersMap = {};
  players.forEach((player, index) => {
    playersMap[player] = index;
  });

  const result = callings.reduce((updatedPlayers, call) => {
    // 데이터 스왑처리 이후 해시맵에 인덱스도 업데이트 해줌
    const index = playersMap[call];
    const temp = updatedPlayers[index - 1];
    updatedPlayers[index - 1] = call;
    playersMap[call] = index - 1;
    updatedPlayers[index] = temp;
    playersMap[temp] = index;
    return updatedPlayers;
  }, players);

  return result;
}

const result = solution(["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]);
console.log(result);
