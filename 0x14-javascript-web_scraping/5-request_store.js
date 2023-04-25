#!/usr/bin/node
// gets the contents of a webpage and stores it in a file.

const request = require('request');
const process = require('process');
const fs = require('fs');
const apiUrl = process.argv[2];
const filePath = process.argv[3];

request.get(apiUrl, (err, response, body) => {
  if (err === null) {
    fs.writeFile(filePath, body, 'utf8', (fileError) => {
      if (fileError !== null) {
        console.log(fileError);
      }
    });
  } else {
    console.log(err);
  }
});
