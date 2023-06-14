#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cn = 0;

  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      cn++;
    }
  }
  return cn;
};
