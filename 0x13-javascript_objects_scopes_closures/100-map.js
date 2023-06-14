#!/usr/bin/node
'use strict';

const list = require('./100-data').list;
console.log(list);
const nList = list.map((value, index) => value * index);
console.log(nList);
