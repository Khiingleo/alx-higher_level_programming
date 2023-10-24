#!/usr/bin/node

const url = process.argv[2];
const fileName = process.argv[3];

const request = require('request');
const fs = require('fs');

request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFile(fileName, body, 'utf-8', function (err) {
      if (err) throw err;
    });
  }
});
