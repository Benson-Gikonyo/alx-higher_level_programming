#!/usr/bin/node

function factorial (num) {
  if (num === 0) {
    return 1;
  }
  return num * factorial(num - 1);
}

let arg1 = Number(process.argv[2]);

if (isNaN(arg1) || arg1 < 0) {
  arg1 = 0;
}
console.log(factorial(arg1));
