#!/usr/bin/node
const add = (a, b) => a + b;
const num1 = parseInt(process.argv[2]);
const num2 = parseInt(process.argv[3]);

const sum = add(num1, num2);
console.log(sum);
