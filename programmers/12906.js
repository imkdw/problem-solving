function solution(arr) {
  const result = [];

  for (let i = 0; i < arr.length; i++) {
    if (i === 0) {
      result.push(arr[i]);
      continue;
    }

    if (arr[i] !== arr[i - 1]) {
      result.push(arr[i]);
      continue;
    }

    if (arr[i] !== arr[i + 1] && arr[i] !== arr[i - 1]) {
      result.push(arr[i]);
      continue;
    }
  }

  return result;
}
