#!/usr/bin/node
const args = process.argv[2];
const x = parseInt(args);
let i;

if (Number.isNaN(x)) {
  console.log('Missing number of occurrences');
} else {
  for (i = 0; i < x; i++) {
    console.log('C is fun');
  }
}
