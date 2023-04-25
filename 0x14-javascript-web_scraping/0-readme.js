#!/usr/bin/node
// read and print a file
const fs = require('fs');
const fileToRead = process.argv[2];

fs.readFile(fileToRead, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
