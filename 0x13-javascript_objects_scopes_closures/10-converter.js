#!/usr/bin/node

exports.converter = function (base) {
  return parseInt(arguments[0], base);
};
