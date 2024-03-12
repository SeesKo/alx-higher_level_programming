#!/usr/bin/node
const fs = require('fs');

// Check if correct number of arguments provided
if (process.argv.length !== 5) {
  console.error('Usage: node concat.js <file1> <file2> <destination>');
  process.exit(1);
}

// Get file paths from command line arguments
const [, , file1, file2, destination] = process.argv;

// Read content of the first file
fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    process.exit(1);
  }

  // Read content of the second file
  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
      process.exit(1);
    }

    // Concatenate content of the two files
    const concatenatedContent = data1.trim() + '\n' + data2.trim() + '\n';

    // Write the concatenated content to the destination file
    fs.writeFile(destination, concatenatedContent, 'utf8', (err) => {
      if (err) {
        process.exit(1);
      }
    });
  });
});
