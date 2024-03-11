#!/usr/bin/node
// Define the factorial function recursively
const factorial = (n) => {
  return n === 0 || isNaN(n) ? 1 : n * factorial(n - 1);
}
// Compute the factorial using the factorial function
const num = parseInt(process.argv[2]);
const result = factorial(num);
console.log(result);
