#!/usr/bin/node

exports.esrever = function (list) {
  const revArr = [];
  if (list === undefined || list.length === 0) {
    return;
  } else {
    for (let num = list.length - 1; num >= 0; num--) {
      revArr.push(list[num]);
    }
  }
  return revArr;
};
