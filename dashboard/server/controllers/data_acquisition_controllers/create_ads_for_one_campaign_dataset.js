//@format
const {PythonShell} = require('python-shell');

function createAdsForOneCampaignDataset(req, res) {
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
}

module.exports = createAdsForOneCampaignDataset;
