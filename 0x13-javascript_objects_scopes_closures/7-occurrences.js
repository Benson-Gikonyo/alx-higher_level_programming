#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let nbOccurences = 0;

  if (list === undefined || searchElement === undefined || list.length === 0) {
    return nbOccurences;
  } else {
    for (const item of list) {
      if (item === searchElement) {
        nbOccurences++;
      }
    }
  }

  return nbOccurences;
};
