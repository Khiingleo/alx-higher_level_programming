#!/usr/bin/node

const arg = parseInt(process.argv[2], 10);

if (!isNaN(arg)) {
  console.log(`My number: ${arg}`);
} else {
  console.log('Not a number');
}
