//@format
const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const {PythonShell} = require('python-shell');

app.use(bodyParser.json());

// this is the only route that creates a data set
// The others just create reports
app.post('/records/createByWidgetsDataset', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.widgetID, req.body.dateRange],
  };
  PythonShell.run(
    'create_by_widgets_data_set.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.sendStatus(200);
    },
  );
});

app.post('/records/ByWidgets', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/by_widgets_scripts/',
    args: [
      req.body.dateRange,
      req.body.widgetID,
      req.body.precondition,
      req.body.c1,
      req.body.c2,
    ],
  };
  PythonShell.run(
    'create_by_widgets_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records/byCampaignByWidgets', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath:
      '../../scripts/data_analysis_scripts/by_campaigns_by_widgets_scripts/',
    args: [],
  };
  for (let arg in req.body) {
    pythonOptions.args.push(req.body[arg]);
  }
  PythonShell.run(
    'create_by_campaigns_by_widgets_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records/byday', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath:
      '../../scripts/data_analysis_scripts/by_campaigns_by_days_scripts/',
    args: [req.body.volid],
  };
  PythonShell.run(
    'create_by_campaigns_by_days_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/by_campaigns_scripts/',
    args: [],
  };
  for (let arg in req.body) {
    pythonOptions.args.push(req.body[arg]);
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
