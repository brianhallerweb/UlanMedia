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

app.post('/records/users/login', (req, res) => {
  // this conditional is my temporary way of validating the user password
  // I don't know the correct way to validate so, for now, I am just
  // checking that the password isn't too long.
  if (req.body.password.length > 15) {
    res.status(404).send('password too long');
  } else {
    User.findByCredentials(req.body.email, req.body.password)
      .then(user => {
        return user.generateAuthToken().then(token => {
          res.header('x-auth', token).send(user);
        });
      })
      .catch(err => {
        res.status(500).send(err);
      });
  }
});

app.delete('/records/users/logout', authenticate, (req, res) => {
  req.user
    .removeToken(req.token)
    .then(() => {
      res.status(200).send();
    })
    .catch(() => {
      res.status(500).send();
    });
});

////////////////////////////
// these are the routes that create data sets
// the others just create reports
app.post(
  '/records/createAdsForOneCampaignDataset',
  authenticate,
  (req, res) => {
    const pythonOptions = {
      pythonPath: '/usr/bin/python3',
      pythonOptions: ['-u'],
      scriptPath: '../../scripts/data_acquisition_scripts/',
      args: [req.body.volID, req.body.dateRange],
    };
    PythonShell.run(
      'create_ads_for_one_campaign_dataset.py',
      pythonOptions,
      (err, results) => {
        if (err) throw err;
        res.sendStatus(200);
      },
    );
  },
);

app.post(
  '/records/createCampaignsForOneAdDataset',
  authenticate,
  (req, res) => {
    const pythonOptions = {
      pythonPath: '/usr/bin/python3',
      pythonOptions: ['-u'],
      scriptPath: '../../scripts/data_acquisition_scripts/',
      args: [req.body.adImage, req.body.dateRange],
    };
    PythonShell.run(
      'create_campaigns_for_one_ad_dataset.py',
      pythonOptions,
      (err, results) => {
        if (err) throw err;
        res.sendStatus(200);
      },
    );
  },
);

app.post(
  '/records/createCampaignsForOneTotalWidgetDataset',
  authenticate,
  (req, res) => {
    const pythonOptions = {
      pythonPath: '/usr/bin/python3',
      pythonOptions: ['-u'],
      scriptPath: '../../scripts/data_acquisition_scripts/',
      args: [req.body.widgetID, req.body.dateRange],
    };
    PythonShell.run(
      'create_campaigns_for_one_total_widget_dataset.py',
      pythonOptions,
      (err, results) => {
        if (err) throw err;
        res.sendStatus(200);
      },
    );
  },
);

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
//
app.post('/records/adsForOneCampaign', authenticate, (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [req.body.dateRange, req.body.volID, req.body.precondition],
  };
  PythonShell.run(
    'create_ads_for_one_campaign_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records/campaignsForOneTotalWidget', authenticate, (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [
      req.body.dateRange,
      req.body.widgetID,
      req.body.precondition,
      req.body.precondition2,
      req.body.c1,
      req.body.c2,
    ],
  };
  PythonShell.run(
    'create_campaigns_for_one_total_widget_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records/campaignsForOneParentWidget', authenticate, (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [
      req.body.dateRange,
      req.body.widgetID,
      req.body.precondition,
      req.body.precondition2,
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
      req.body.precondition2,
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

app.post('/records/adsForAllCampaigns', authenticate, (req, res) => {
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
    'create_ads_for_all_campaigns_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

app.post('/records/campaignsForOneAd', authenticate, (req, res) => {
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
    'create_campaigns_for_one_ad_report.py',
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
