#!/usr/bin/node
const size = parseInt(process.argv[2]);

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < size; r++) {
    let line = '';
    for (let c = 0; c < size; c++) line += 'X';
    console.log(line);
  }
}
