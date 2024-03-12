#!/usr/bin/node
const fs = require('fs');
// Check if correct number of arguments provided
if (process.argv.length !== 5) {
  console.error('Usage: node concat.js <file1> <file2> <destination>');
  process.exit(1);
}
// Get file paths from command line arguments
const [, , file1, file2, destination] = process.argv;

try {
  // Read content of the first file synchronously
  const data1 = fs.readFileSync(file1, 'utf8');

  // Read content of the second file synchronously
  const data2 = fs.readFileSync(file2, 'utf8');

  // Concatenate content of the two files
  const concatenatedContent = data1.trim() + '\n' + data2.trim() + '\n';

  // Write the concatenated content to the destination file synchronously
  fs.writeFileSync(destination, concatenatedContent, 'utf8');
} catch (err) {
  console.error(`Error: ${err}`);
  process.exit(1);
}
