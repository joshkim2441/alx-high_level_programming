#!/usr/bin/node
const x = Math.floor(Number(process.argv[2]));
if (!isNaN(x)) {
  // Argument can be converted to an integer
	for (let i = 0; i < x; i++) {
		console.log("C is fun");
	}
} else {
  // Argumnet cannot be converted to an integer
	console.log("Missing number of ocurrences");
}
