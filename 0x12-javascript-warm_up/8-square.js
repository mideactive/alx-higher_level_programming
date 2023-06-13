#!/usr/bin/node
const arg = process.argv[2];
const size = parseInt(arg);
let i;
let j;
let r;

if (Number.isNaN(size)) {
  console.log('Missing size');
} else {
  for (i = 0; i < size; i++) {
    r = '';
    for (j = 0; j < size; j++) {
      r += 'X';
    }
    console.log(r);
  }
}
