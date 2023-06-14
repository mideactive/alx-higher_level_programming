#!/usr/bin/node
let cn = 0;

exports.logMe = function (item) {
  console.log(cn + ': ' + item);
  cn++;
};
