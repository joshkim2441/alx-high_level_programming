#!/usr/bin/node
// Display the status code of a GET request

const request = require('request');
const argv = process.argv;
// The first argument is the URL to request (GET)
let url = argv[2];

request.get(url).on('response', function (response) {
        // The status code is printed like this: code: <status code>
    console.log(`code: ${response.statusCode}`);
});
