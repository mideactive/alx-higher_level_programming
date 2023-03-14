#!/usr/bin/node
const dict = require('./text_files/101-data.js').dict;
const newDict = {};
for (const key in dict) {
  if (newDict[dict[key]] === undefined) {
    newDict[dict[key]] = [key];
  } else {
    newDict[dict[key]].push(key);
  }
}
console.log(newDict);
