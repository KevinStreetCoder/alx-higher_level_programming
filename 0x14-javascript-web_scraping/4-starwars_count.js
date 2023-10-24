#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
    } else if (response.statusCode === 200) {
        const filmsData = JSON.parse(body);
        const characterId = 18; // Wedge Antilles character ID
        const moviesWithWedgeAntilles = filmsData.results.filter((movie) =>
            movie.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)
        );

        console.log(moviesWithWedgeAntilles.length);
    } else {
        console.error(`Request failed with status code: ${response.statusCode}`);
    }
});
