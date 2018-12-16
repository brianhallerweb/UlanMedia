//@format
const {PythonShell} = require('python-shell');

function createCampaignsForOneOfferDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.dateRange, req.body.offerID],
  };
  PythonShell.run(
    'create_campaigns_for_one_offer_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createCampaignsForOneOfferDataset;
