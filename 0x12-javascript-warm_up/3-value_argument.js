#!/usr/bin/node
// Check if any arguments were passed
if (process.argv.length > 2) {
  // Print the first argument
  console.log(process.argv[2]);
} else {
  // No arguments passed, print "No argument"
  console.log("No argument");
}
