#!/usr/bin/node

const size = Number(process.argv[2]);
let square = '';

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let len = 0; len < size; len++) {
    for (let wid = 0; wid < size; wid++) {
      square += 'X';
    }
    if (len === size - 1) {
      continue;
    } else {
      square += '\n';
    }
  }
  console.log(square);
}
