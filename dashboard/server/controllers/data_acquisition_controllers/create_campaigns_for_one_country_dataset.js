//@format
const {PythonShell} = require('python-shell');

function createCampaignsForOneCountryDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.countryName],
  };
  PythonShell.run(
    'create_campaigns_for_one_country_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createCampaignsForOneCountryDataset;
