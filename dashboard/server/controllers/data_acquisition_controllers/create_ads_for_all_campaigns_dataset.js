//@format
const {PythonShell} = require('python-shell');

function createAdsForAllCampaignsDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.dateRange, req.body.precondition],
  };
  PythonShell.run(
    'create_ads_for_all_campaigns_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.sendStatus(200);
    },
  );
}

module.exports = createAdsForAllCampaignsDataset;
