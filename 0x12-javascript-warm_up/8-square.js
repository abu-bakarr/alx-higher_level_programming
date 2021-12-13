#!/usr/bin/node

if (process.argv[2] === undefined || isNaN(Number(process.argv[2]))) {
    console.log('Missing size');
} else {
    for (let i = 0; i < parseInt(process.argv[2]); i++) {
        let tmp = 'X';
        for (let j = 0; j < parseInt(process.argv[2]) - 1; j++) {
            tmp += 'X';
        }
        console.log(tmp);
    }
}