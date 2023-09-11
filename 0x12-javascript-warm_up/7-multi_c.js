#!/usr/bin/node

const arg = parseInt(process.argv[2], 10);

if (!isNaN(arg)) {
  for (let i = arg; i > 0; i--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurences');
}
