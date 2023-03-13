#!/usr/bin/node
const cnt = process.argv.length;
console.log(cnt === 2 ? 'No argument' : cnt === 3 ? 'Argument found' : 'Arguments found');
