#!/usr/bin/env node
const fs = require('fs');
// Checking if correct number of arguments are provided
if (process.argv.length !== 5) {
  console.error('Usage: ./102-concat.js <file1> <file2> <output>');
  process.exit(1);
}
const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;
// Reading content of source files
const content1 = fs.readFileSync(sourceFile1, 'utf8').trim();
const content2 = fs.readFileSync(sourceFile2, 'utf8').trim();
// Concatenating content
const concatContent = content1 + '\n' + content2;
// Printing concatenated content
console.log(concatContent);
// Writing concatenated content to destination file
fs.writeFileSync(destinationFile, concatContent);
process.exit(0);
