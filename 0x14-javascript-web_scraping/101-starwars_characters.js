#!/usr/bin/node

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;
const request = require('request');

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    body = JSON.parse(body);
    const chars = body.characters;
    printChars(chars, 0);
  }
});

function printChars (characters, index) {
  request(characters[index], function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const names = JSON.parse(body).name;
      console.log(names);
      if (index + 1 < characters.length) {
        printChars(characters, index + 1);
      }
    }
  });
}
