#!/usr/bin/node
// write a file. Handle errors.

const fs = require('fs');

const fileToWrite = process.argv[2];
const content = process.argv[3];

fs.writeFile(fileToWrite, content, { flag: 'a+' }, err => {
  if (err) {
    console.error(err);
  }
});
