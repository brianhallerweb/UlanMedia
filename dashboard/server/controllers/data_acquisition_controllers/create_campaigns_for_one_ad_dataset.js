//@format
const {PythonShell} = require('python-shell');

function createCampaignsForOneAdDataset(req, res) {
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
}

module.exports = createCampaignsForOneAdDataset;
