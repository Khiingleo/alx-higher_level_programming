#!/usr/bin/node

const fileName = process.argv[2];
const myString = process.argv[3];

const fs = require('fs');
fs.writeFile(fileName, myString, 'utf-8', (err) => {
  if (err) throw err;
});
