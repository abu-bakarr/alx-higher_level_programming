#!/usr/bin/node

function myFunc(x) {
    if (x === 0) {
        return 1;
    }
    return x * myFunc(x - 1);
}
if (process.argv[2] === undefined || isNaN(Number(process.argv[2]))) {
    console.log(myFunc(0));
} else {
    console.log(myFunc(parseInt(process.argv[2])));
}