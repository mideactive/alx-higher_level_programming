#!/usr/bin/node
const list = require('./text_files/100-data.js').list;
console.log(list);
console.log(list.map((item, index) => item * index));
