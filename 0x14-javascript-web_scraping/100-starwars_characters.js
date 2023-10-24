#!/usr/bin/node

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + id;
const request = require('request');

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    body = JSON.parse(body);
    for (const i in body.characters) {
      request(body.characters[i], function (error, response, body) {
        if (!error && response.statusCode === 200) {
          const mybody = JSON.parse(body);
          console.log(mybody.name);
        }
      });
    }
  } else {
    console.log('Error: ', error);
  }
});
