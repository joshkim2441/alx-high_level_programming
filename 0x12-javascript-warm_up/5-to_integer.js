#!/usr/bin/node
const dgt = Math.floor(Number(process.argv[2]));
console.log(isNaN(dgt) ? 'Not a number' : `My number: ${dgt}`);
