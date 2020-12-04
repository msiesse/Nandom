const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const cors = require('cors');

const app = express();
app.use(bodyParser.json());

const idMovies = fs.readFileSync('./fdb').toString().split('\n');

app.get('/', cors(), (req, res) => {
    randomNumber = Math.floor(Math.random() * idMovies.length);
    res.status(200).send('https://www.netflix.com/watch/' + idMovies[randomNumber]);
})

app.listen(8080, () => {
    console.log('Listening on port 8080');
})