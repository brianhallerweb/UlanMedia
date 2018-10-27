//@format
require('../../config/config');
require('./db/mongoose');
const express = require('express');
const app = express();
const authenticate = require('./middleware/authenticate');
const path = require('path');
const bodyParser = require('body-parser');
const {PythonShell} = require('python-shell');
const User = require('./models/user');

app.use(bodyParser.json());

////////////////////////////////
//security stuff

// sign up
// I only used this route to create the michael@hallerweb.com
// user once. I did it through postman.
// It is not a route that is accessible through the web app
//app.post('/records/users', (req, res) => {
//  const user = new User({
//    email: req.body.email,
//    password: req.body.password,
//  });
//  user
//    .generateAuthToken()
//    .then(token => {
//      res.header('x-auth', token).json(user);
//    })
//    .catch(err => res.status(500).json(err));
//});

// login
app.post('/records/users/login', (req, res) => {
  User.findByCredentials(req.body.email, req.body.password)
    .then(user => {
      return user.generateAuthToken().then(token => {
        res.header('x-auth', token).send(user);
      });
    })
    .catch(err => {
      res.status(500).send(err);
    });
});

////////////////////////////
// these are the only routes that create data sets
// The others just create reports
app.post(
  '/records/createCampaignsForOneParentWidgetDataset',
  authenticate,
  (req, res) => {
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
  },
);

app.post(
  '/records/createCampaignsForOneChildWidgetDataset',
  authenticate,
  (req, res) => {
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
  },
);
///////////////////////////

app.post('/records/campaignsForOneParentWidget', authenticate, (req, res) => {
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

app.post('/records/campaignsForOneChildWidget', authenticate, (req, res) => {
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

app.post('/records/widgetsForOneCampaign', authenticate, (req, res) => {
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

app.post('/records/widgetsForAllCampaigns', authenticate, (req, res) => {
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
    'create_widgets_for_all_campaigns_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records/daysForOneCampaign', authenticate, (req, res) => {
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

app.post('/records/campaignsForAllCampaigns', authenticate, (req, res) => {
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

app.listen(process.env.PORT, () => {
  console.log(`dashboard server running on port ${process.env.PORT}`);
});
