#!/usr/bin/node

const num = Number(process.argv[2]);

if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let x = 0; x < num; x++) {
    console.log('C is fun');
  }
}
