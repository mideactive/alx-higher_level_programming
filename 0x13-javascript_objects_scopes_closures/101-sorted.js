#!/usr/bin/node
'use strict';

const dict = require('./101-data').dict;

const usrId = {};

for (const uId in dict) {
  const occurrence = dict[uId];

  if (occurrence in usrId) {
    usrId[occurrence].push(uId);
  } else {
    usrId[occurrence] = [uId];
  }
}
console.log(usrId);
