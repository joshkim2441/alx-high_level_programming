#!/usr/bin/node
// Display the status code of a GET request

const request = require('request');
const url = process.argv[2];
// The first argument is the URL to request (GET)

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
