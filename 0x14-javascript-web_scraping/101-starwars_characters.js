#!/usr/bin/node
 // JavaScript - Web scraping

const process = require('process');
const request = require('request');
const args = process.argv;
const movieID = args[2];
const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieID}/`;
const options = { json: true };

request(url, options, function(error, response, body) {
    if (error) {
        console.error(error);
        return;
    }
    const casting = body.characters;
    for (const i in casting) {
        request(casting[i], options, function(error, response, body) {
            if (error) {
                console.error(error);
            } else {
                console.log(body.name);
            }
        });
    }
});