const express = require('express');
const app = express();

app.use(express.static(__dirname + ''));

//  To use python script
var PythonShell = require('python-shell');

const port = 8080
app.listen(port, function() {
    console.log('Listening on '+ port);
});

app.get("/", function (req, res) {
    res.send("Hello World!");
});

app.get('/keystroke', function(req, res) {
    res.sendFile(__dirname + '/keystroke.html');
});

app.get('/keystroke/:country', function(req, res) {
    var options = {
        mode: 'json',
        pythonPath:'',  
        pythonOptions:['-u'],
        scriptPath:'',
        args: [req.query.country]
    };
    PythonShell.PythonShell.run('./pythonScript/prePopulate.py', options, function(err, results) {
        if(err) throw err;
        res.status(200).send(results[0]);
    });
});