#!/usr/bin/node
const request = require('axios');

const url = process.argv[2];
if (!url) {
  console.error('Usage: node 2-statuscode.js <URL>');
} else {
  request.get(url, (error, response) => {
    if (error) {
      console.error(error);
    } else {
      console.log(`code: ${response.statusCode}`);
    }
  });
}
