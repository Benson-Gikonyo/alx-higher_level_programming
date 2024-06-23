#!/usr/bin/node

const oldSquare = require('./5-square');

class Square extends oldSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let sq = '';
    for (let num1 = 0; num1 < this.size; num1++) {
      for (let num2 = 0; num2 < this.size; num2++) {
        sq += c;
      }
      if (num1 === this.size - 1) {
        continue;
      } else {
        sq += '\n';
      }
    }
    console.log(sq);
  }
}

module.exports = Square;
