//@format
const express = require('express');
const app = express();
const path = require('path');
const {PythonShell} = require('python-shell');

app.get('/records/yesterday', (req, res) => {
  const pyshell = new PythonShell(
    '../../scripts/data_analysis_scripts/create_yesterday_json.py',
  );

  pyshell.on('message', function(message) {
    res.send(message);
  });

  pyshell.end(function(err) {
    if (err) {
      throw err;
    }
  });
});

app.get('/records/7days', (req, res) => {
  const pyshell = new PythonShell(
    '../../scripts/data_analysis_scripts/create_seven_json.py',
  );

  pyshell.on('message', function(message) {
    res.send(message);
  });

  pyshell.end(function(err) {
    if (err) {
      throw err;
    }
  });
});

app.get('/records/30days', (req, res) => {
  const pyshell = new PythonShell(
    '../../scripts/data_analysis_scripts/create_thirty_json.py',
  );

  pyshell.on('message', function(message) {
    res.send(message);
  });

  pyshell.end(function(err) {
    if (err) {
      throw err;
    }
  });
});

app.get('/records/90days', (req, res) => {
  const pyshell = new PythonShell(
    '../../scripts/data_analysis_scripts/create_ninety_json.py',
  );

  pyshell.on('message', function(message) {
    res.send(message);
  });

  pyshell.end(function(err) {
    if (err) {
      throw err;
    }
  });
});

app.get('/records/180days', (req, res) => {
  const pyshell = new PythonShell(
    '../../scripts/data_analysis_scripts/create_oneeighty_json.py',
  );

  pyshell.on('message', function(message) {
    res.send(message);
  });

  pyshell.end(function(err) {
    if (err) {
      throw err;
    }
  });
});

app.use(express.static('../public'));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.listen('3000', () => {
  console.log(`dashboard running on port 3000...`);
});
