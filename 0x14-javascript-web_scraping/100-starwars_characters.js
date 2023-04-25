#!/usr/bin/node
// prints all characters of a Star Wars movie:
const request = require('request');
const process = require('process');
const filmId = process.argv[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request.get(apiUrl, (err, response, body) => {
  if (err === null) {
    const film = JSON.parse(body);
    const characters = film.characters;
    characters.forEach((character) => {
      request.get(character, (charError, response, body) => {
        if (err === null) {
          const characterInfo = JSON.parse(body);
          console.log(characterInfo.name);
        } else {
          console.log(charError);
        }
      });
    });
  } else {
    console.log(err);
  }
});
