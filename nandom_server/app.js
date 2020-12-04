const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');

const app = express();
app.use(bodyParser.json());

const idMovies = fs.readFileSync('./fdb').toString().split('\n');

app.get('/', (req, res) => {
    randomNumber = Math.floor(Math.random() * idMovies.length);
    res.redirect('https://www.netflix.com/watch/' + idMovies[randomNumber]);
    res.status(200).send('OK');
})

app.listen(8080, () => {
    console.log('Listening on port 8080');
})