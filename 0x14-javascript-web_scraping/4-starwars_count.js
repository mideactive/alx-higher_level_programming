#!/usr/bin/node
// prints the number of movies where the character "Wedge Antilles" is present

const apiUrl = process.argv[2];
const charToSearch = 18;
const request = require('request');

request.get(apiUrl, (err, response, body) => {
  if (err === null) {
    const data = JSON.parse(body);
    let films = data.results;
    films = films.filter(
      film => film.characters.find(
        character => character.match(charToSearch)
      )
    );
    console.log(films.length);
  } else {
    console.log(err);
  }
});
