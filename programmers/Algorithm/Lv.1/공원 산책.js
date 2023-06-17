function solution(park, routes) {
  const H = park.length;
  const W = park[0].length;
  let currentPos = [0, 0];

  for (let i = 0; i < routes.length; i++) {
    const [direction, distance] = routes[i].split(" ");
    const dx = direction === "E" ? 1 : direction === "W" ? -1 : 0;
    const dy = direction === "S" ? 1 : direction === "N" ? -1 : 0;

    for (let j = 0; j < distance; j++) {
      const newX = currentPos[0] + dx;
      const newY = currentPos[1] + dy;

      if (newX < 0 || newX >= H || newY < 0 || newY >= W) {
        // Out of park bounds, ignore the command
        break;
      }

      if (park[newX][newY] === "X") {
        // Obstacle encountered, ignore the command
        break;
      }

      currentPos = [newX, newY];
    }
  }

  return currentPos;
}

const result = solution(["SOO", "OOO", "OOO"], ["E 2", "S 2", "W 1"]);
const result2 = solution(["SOO", "OXX", "OOO"], ["E 2", "S 2", "W 1"]);
const result3 = solution(["OSO", "OOO", "OXO", "OOO"], ["E 2", "S 3", "W 1"]);
console.log(result);
console.log(result2);
console.log(result3);
