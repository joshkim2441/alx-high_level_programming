#!/usr/bin/node
// Print the title of a Star Wars movie
// matching the given integer

const request = require('request');
const endPoint = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request({ url: endPoint, methods: 'GET' }, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    console.log(body && JSON.parse(body).title);
  }
});
