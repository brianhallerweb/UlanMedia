//@format
const express = require('express');
const app = express();
const path = require('path');
const {PythonShell} = require('python-shell');

const pythonOptions = {
  pythonPath: '/usr/bin/python3',
  pythonOptions: ['-u'],
  scriptPath: '../../scripts/data_analysis_scripts/',
};

app.get('/records/yesterday', (req, res) => {
  PythonShell.run('create_yesterday_json.py', pythonOptions, (err, results) => {
    if (err) throw err;
    res.send(results[0]);
  });
});

app.get('/records/7days', (req, res) => {
  PythonShell.run('create_seven_json.py', pythonOptions, (err, results) => {
    if (err) throw err;
    res.send(results[0]);
  });
});

app.get('/records/30days', (req, res) => {
  PythonShell.run('create_thirty_json.py', pythonOptions, (err, results) => {
    if (err) throw err;
    res.send(results[0]);
  });
});

app.get('/records/90days', (req, res) => {
  PythonShell.run('create_ninety_json.py', pythonOptions, (err, results) => {
    if (err) throw err;
    res.send(results[0]);
  });
});

app.get('/records/180days', (req, res) => {
  PythonShell.run('create_oneeighty_json.py', pythonOptions, (err, results) => {
    if (err) throw err;
    res.send(results[0]);
  });
});

app.use(express.static('../public'));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.listen('3000', () => {
  console.log(`dashboard running on port 3000...`);
});
