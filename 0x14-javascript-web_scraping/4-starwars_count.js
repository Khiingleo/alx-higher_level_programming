#!/usr/bin/node

const url = process.argv[2];
const request = require('request');

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    let num = 0;
    const movie = JSON.parse(body).results;
    for (const i in movie) {
      const chars = movie[i].characters;
      for (const chr in chars) {
        if (chars[chr].includes('18')) {
          num++;
        }
      }
    }
    console.log(num);
  } else {
    console.log('Code: ' + response.statusCode);
  }
});
