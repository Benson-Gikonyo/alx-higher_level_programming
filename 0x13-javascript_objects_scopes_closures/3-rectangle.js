#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (w, h) {
    let rectangle = '';
    for (let num1 = 0; num1 < this.height; num1++) {
      for (let num2 = 0; num2 < this.width; num2++) {
        rectangle += 'X';
      }
      if (num1 === this.height - 1) {
        continue;
      } else {
        rectangle += '\n';
      }
    }
    console.log(rectangle);
  }
}

module.exports = Rectangle;
