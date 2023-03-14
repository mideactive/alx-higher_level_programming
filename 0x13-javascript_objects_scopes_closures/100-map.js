#!/usr/bin/node
'use strict';

const list = require('./text_files/100-data.js').list;
console.log(list);
const newList = list.map((x, index) => x * index);
console.log(newList);
