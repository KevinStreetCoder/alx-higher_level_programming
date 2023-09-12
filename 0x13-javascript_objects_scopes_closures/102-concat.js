#!/usr/bin/node
const fs = require('fs');
const fileA = process.argv[2];
const fileB = process.argv[3];
const destinationFile = process.argv[4];

fs.readFile(fileA, 'utf8', (errA, dataA) => {
  if (errA) throw errA;
  
  fs.readFile(fileB, 'utf8', (errB, dataB) => {
    if (errB) throw errB;
    
    const concatenatedData = dataA + dataB;
    
    fs.writeFile(destinationFile, concatenatedData, (errWrite) => {
      if (errWrite) throw errWrite;
      console.log('Concatenation complete.');
    });
  });
});
