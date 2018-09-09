//@format
const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const {PythonShell} = require('python-shell');

app.use(bodyParser.json());
const pythonOptions = {
  pythonPath: '/usr/bin/python3',
  pythonOptions: ['-u'],
  scriptPath: '../../scripts/data_analysis_scripts/by_campaigns_scripts/',
};

app.post('/records', (req, res) => {
  pythonOptions['args'] = [];
  for (let arg in req.body) {
    pythonOptions['args'].push(req.body[arg]);
  }
  PythonShell.run(
    'create_by_campaigns_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.use(express.static('../public'));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.listen('3000', () => {
  console.log(`dashboard running on port 3000...`);
});
