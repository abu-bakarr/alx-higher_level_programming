#!/usr/bin/node


const process = require('process');
const request = require('request');
const args = process.argv;
const peopleId = args[2];
const apiUrl = `https://swapi-api.hbtn.io/api/people/${peopleId}`;
const options = { json: true };

request(apiUrl, options, function(error, response, body) {
    if (error) {
        console.error(error);
        return;
    }
    const casting = body.characters;
    for (const cast in casting) {
        request(casting[cast], options, function(error, response, body) {
            if (error) {
                console.error(error);
            } else {
                console.log(body.name);
            }
        });
    }
});