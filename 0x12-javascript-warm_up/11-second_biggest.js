#!/usr/bin/node

if (process.argv[2] === undefined || process.argv[3] === undefined) {
    console.log(0);
} else {
    const myArr = process.argv.slice();
    myArr.shift();
    myArr.shift();
    console.log(myArr.sort((a, b) => a - b)[myArr.length - 2]);
}