#!/usr/bin/node
// Print the title of a Star Wars movie
// matching the given integer

const request = require('request');
const argv = process.argv;
let url = 'http://swapi.co/api/films/';

request(url + argv[2], function (err, res, body) {
    if (err) {
        console.log(err);
    } else {
        try {
            let json = JSON.parse(body);
            console.log(json.title);
        } catch (e) {
            console.error('Error parsing JSON:', e);
        }
    }
});
