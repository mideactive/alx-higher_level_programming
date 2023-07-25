#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: node 101-starwars_characters.js <movie-id>');
} else {
  const url = `https://swapi.dev/api/films/${movieId}/`;
  request(url, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const charactersUrls = JSON.parse(body).characters;
      printCharacters(charactersUrls, 0);
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }
  });
}

function printCharacters (charactersUrls, index) {
  if (index >= charactersUrls.length) {
    return;
  }

  const characterUrl = charactersUrls[index];
  request(characterUrl, function (error, response, body) {
    if (!error && response.statusCode === 200) {
      const characterName = JSON.parse(body).name;
      console.log(characterName);
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }

    // Recursively call printCharacters for the next character
    printCharacters(charactersUrls, index + 1);
  });
}
