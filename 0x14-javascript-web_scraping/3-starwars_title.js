#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;

const request = require('request');
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else if (response) {
    console.log('Code: ' + response.statusCode);
  } else {
    console.log('Error: ', error);
  }
});
