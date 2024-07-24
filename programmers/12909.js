function solution(s) {
  const stack = [];

  let isSuccess = false;
  for (const char of s) {
    if (char === "(") {
      stack.push(char);
      isSuccess = false;
      continue;
    }

    if (char === ")") {
      if (stack.length === 0) {
        return false;
      }

      stack.pop();
      isSuccess = true;
    }
  }

  if (stack.length) {
    return false;
  }

  return isSuccess;
}

console.log(solution("()()"));
console.log(solution("(())()"));
console.log(solution(")()("));
console.log(solution("(()("));
