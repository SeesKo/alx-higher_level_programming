#!/usr/bin/node
const fs = require('fs');

// Check if correct number of arguments is provided
if (process.argv.length !== 5) {
  console.error('Usage: node concat.js <file1> <file2> <destination>');
  process.exit(1);
}

const [, , file1, file2, destination] = process.argv;

// Read the content of file1
fs.readFile(file1, 'utf8', (err, data1) => {
  if (err) {
    console.error(`Error reading file ${file1}:`, err);
    process.exit(1);
  }

  // Read the content of file2
  fs.readFile(file2, 'utf8', (err, data2) => {
    if (err) {
      console.error(`Error reading file ${file2}:`, err);
      process.exit(1);
    }

    // Concatenate data1 and data2
    const concatenatedData = data1.trim() + '\n' + data2.trim();

    // Write concatenated content to the destination file
    fs.writeFile(destination, concatenatedData, (err) => {
      if (err) {
        console.error(`Error writing to file ${destination}:`, err);
        process.exit(1);
      }
      console.log(concatenatedData);
    });
  });
});
