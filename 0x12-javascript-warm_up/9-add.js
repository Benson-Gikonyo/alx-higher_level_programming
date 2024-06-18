#!/usr/bin/node

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

const num1 = Number(process.argv[2]);
const num2 = Number(process.argv[3]);

if (isNaN(num1)) {
  console.log(NaN);
} else if (isNaN(num2)) {
  console.log(NaN);
} else {
  add(num1, num2);
}
