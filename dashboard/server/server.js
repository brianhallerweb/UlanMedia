//@format
const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const {PythonShell} = require('python-shell');

app.use(bodyParser.json());

////////////////////////////
// these are the only routes that create data sets
// The others just create reports
app.post('/records/createCampaignsForOneParentWidgetDataset', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.widgetID, req.body.dateRange],
  };
  PythonShell.run(
    'create_campaigns_for_one_parent_widget_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.sendStatus(200);
    },
  );
});

app.post('/records/createCampaignsForOneChildWidgetDataset', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.widgetID, req.body.dateRange],
  };
  PythonShell.run(
    'create_campaigns_for_one_child_widget_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.sendStatus(200);
    },
  );
});
///////////////////////////

app.post('/records/campaignsForOneParentWidget', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [
      req.body.dateRange,
      req.body.widgetID,
      req.body.precondition,
      req.body.c1,
      req.body.c2,
    ],
  };
  PythonShell.run(
    'create_campaigns_for_one_parent_widget_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records/campaignsForOneChildWidget', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [
      req.body.dateRange,
      req.body.widgetID,
      req.body.precondition,
      req.body.c1,
      req.body.c2,
    ],
  };
  PythonShell.run(
    'create_campaigns_for_one_child_widget_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records/widgetsForOneCampaign', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [],
  };
  for (let arg in req.body) {
    pythonOptions.args.push(req.body[arg]);
  }
  PythonShell.run(
    'create_widgets_for_one_campaign_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records/daysForOneCampaign', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [req.body.volid],
  };
  PythonShell.run(
    'create_days_for_one_campaign_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records/campaignsForAllCampaigns', (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [],
  };
  for (let arg in req.body) {
    pythonOptions.args.push(req.body[arg]);
  }
  PythonShell.run(
    'create_campaigns_for_all_campaigns_report.py',
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
