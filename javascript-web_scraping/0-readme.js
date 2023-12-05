#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 3) {
  console.error('Usage: node 0-readme.js <file-path>');
  process.exit(1); // Exit with an error code
}

const filePath = process.argv[2];

// Read the content of the file in utf-8
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err); // Print the error object
  } else {
    console.log(data); // Print the content of the file
  }
});

