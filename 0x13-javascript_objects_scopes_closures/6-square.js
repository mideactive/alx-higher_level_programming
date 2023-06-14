#!/usr/bin/node
const oSquare = require('./5-square.js');

module.exports = class Square extends oSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
};
