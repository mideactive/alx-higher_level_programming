#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const data = JSON.parse(body);
    const dictionary = {};

    data.forEach(function (result) {
      if (result.completed === true) {
        const userId = result.userId;
        dictionary[userId] = (dictionary[userId] || 0) + 1;
      }
    });

    console.log(dictionary);
  }
});
