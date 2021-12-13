#!/usr/bin/node

function add(a, b) {
    let res = parseInt(a) + parseInt(b);
    return (res);
}

console.log(add(process.argv[2], process.argv[3]));