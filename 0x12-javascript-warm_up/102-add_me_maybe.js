#!/usr/bin/node
function addMeMaybe (number, theFunction) {
  const newN = number + 1;
  theFunction(newN);
}
module.exports = {
  addMeMaybe
};
