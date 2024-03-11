#!/usr/bin/node
function factorial (i) {
  if (isNaN(i) || i < 0) {
    return 1; // Factorial of NaN or negative numbers is 1
  }
  if (i === 0 || i === 1) {
    return 1; // Base case: factorial of 0 or 1 is 1
  } else {
    return i * factorial(i - 1); // Recursive case
  }
}
const arg = parseInt(process.argv[2]);
console.log(factorial(arg));
