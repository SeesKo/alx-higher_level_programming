#!/usr/bin/node
const fs = require('fs');
// Checking if correct number of arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: node concat.js <file1> <file2> <destination>');
  process.exit(1);
}
// Getting file paths from command line arguments
const [, , file1, file2, destination] = process.argv;

try {
  // Reading content of first file synchronously
  const data1 = fs.readFileSync(file1, 'utf8');
  // Reading content of second file synchronously
  const data2 = fs.readFileSync(file2, 'utf8');
  // Concatenating content of the two files
  const concatenatedContent = data1.trim() + '\n' + data2.trim() + '\n';
  // Writing concatenated content to destination file synchronously
  fs.writeFileSync(destination, concatenatedContent, 'utf8');
} catch (err) {
  console.error(`Error: ${err}`);
  process.exit(1);
}
