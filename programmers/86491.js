function solution(sizes) {
  let [maxWidth, maxHeight] = [0, 0];
  sizes.forEach(([width, height]) => {
    if (width < height) {
      [width, height] = [height, width];
    }

    maxWidth = Math.max(maxWidth, width);
    maxHeight = Math.max(maxHeight, height);
  });

  return maxWidth * maxHeight;
}

console.log(
  solution([
    [60, 50],
    [30, 70],
    [60, 30],
    [80, 40],
  ])
);

console.log(
  solution([
    [10, 7],
    [12, 3],
    [8, 15],
    [14, 7],
    [5, 15],
  ])
);
