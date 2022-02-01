const fs = require('fs');
const process = require('process');
const args = process.argv;

fs.readFile(args[2], 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log(data);
});