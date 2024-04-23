#!/usr/bin/node
// Writes a string to a file

const fs = require('fs');

// The first argument is the file path
const filePath = process.argv[2];

// The second argument is the string to write
const content = process.argv[3];
fs.writeFile(filePath, content, 'utf8',
  function (err) {
    if (err) {
      // If an error occurred during writing,
      // print the error object
      console.log(err);
    } else {
      console.log('File written successfully!');
    }
  });
