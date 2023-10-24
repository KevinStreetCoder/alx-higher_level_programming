#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
    } else if (response.statusCode === 200) {
        const movieData = JSON.parse(body);
        console.log("Characters in the movie:");
        movieData.characters.forEach((characterUrl) => {
            request(characterUrl, (error, response, characterBody) => {
                if (error) {
                    console.error(error);
                } else if (response.statusCode === 200) {
                    const characterData = JSON.parse(characterBody);
                    console.log(characterData.name);
                } else {
                    console.error(`Failed to fetch character with status code: ${response.statusCode}`);
                }
            });
        });
    } else {
        console.error(`Request failed with status code: ${response.statusCode}`);
    }
});
