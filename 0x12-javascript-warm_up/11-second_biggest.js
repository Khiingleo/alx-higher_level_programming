#!/usr/bin/node

const args = process.argv.slice(2).map(Number); // converts args into numbers

if (args.length <= 1) {
  console.log(0);
} else {
  const sorted = args.sort((a, b) => b - a); // descending order
  console.log(sorted[1]);
}
