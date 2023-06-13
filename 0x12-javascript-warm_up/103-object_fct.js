#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};

console.log(myObject);

Object.defineProperty(myObject, 'incr', {
  value: function () {
    this.value++;
  },
  enumerable: false,
  writable: false
});

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);

myObject.incr();
console.log(myObject);
