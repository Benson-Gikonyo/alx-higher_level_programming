#!/usr/bin/node

const argArr = [];
const len = process.argv.length;

if (len === 2 || len === 3) {
  console.log(0);
} else {
  for (let idx = 2; idx < len; idx++) {
    argArr.push(Number(process.argv[idx]));
  }

  console.log(argArr);

  argArr.sort((a, b) => b - a);

  console.log(argArr[1]);
}
