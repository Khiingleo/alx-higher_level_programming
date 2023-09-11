#!/usr/bin/node

/*
 uses process.argv
 process.argv returns an array containing command-line arguments pased when
 the script was launched
 it contains; ['path to node', 'path to executable', 'arg1',... 'argn']
*/
if (process.argv.length === 2) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
