#!/usr/bin/node
const { dict } = require('./101-data');
const newDict = {};

Object.keys(dict).forEach(userId => {
  const occurrences = dict[userId];
  if (!newDict[occurrences]) {
    newDict[occurrences] = [];
  }
  newDict[occurrences].push(userId);
});

console.log(newDict);
