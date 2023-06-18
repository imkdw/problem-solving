function solution(park, routes) {
  // 공원을 2차원 배열로 변환
  const parkArr = [];
  park.forEach((p) => {
    const parkRow = [];
    p.split("").forEach((_) => {
      parkRow.push(_);
    });
    parkArr.push(parkRow);
  });

  // 시작점 좌표 구하기
  let posArr = [];
  parkArr.forEach((park, index) => {
    const width = index;
    park.forEach((p, index) => {
      if (p === "S") {
        posArr.push(width, index);
      }
    });
  });
  let [width, height] = [posArr[0], posArr[1]];
  console.log(width, height);

  // route대로 움직이기
  routes.forEach((route) => {
    const routeArr = route.split(" ");
    const [pos, len] = [routeArr[0], routeArr[1]];

    for (let i = 0; i < len; i++) {
      if (parkArr[height].length === width || parkArr[width].length === height) break;
      switch (pos) {
        case "N":
          if (parkArr[height - 1][width] === "X") break;
          height -= 1;
          break;
        case "E":
          if (parkArr[height][width + 1] === "X") break;
          width += 1;
          break;
        case "S":
          if (parkArr[height + 1][width] === "X") break;
          height += 1;
          break;
        case "W":
          if (parkArr[height][width - 1] === "X") break;
          width -= 1;
      }
    }
  });

  var answer = [height, width];
  return answer;
}

const result = solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]);
const result2 = solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]);
const result3 = solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]);
console.log(result);
console.log(result2);
console.log(result3);
