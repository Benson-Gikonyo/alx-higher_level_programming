#!/usr/bin/node

const list = require('./100-data').list;
let num = 0;
const newArr = list.map((x) => x * num++);
console.log(list);
console.log(newArr);
