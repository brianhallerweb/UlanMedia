//@format
const {PythonShell} = require('python-shell');

function createCampaignsForGoodPWidgetsDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [
      req.body.dateRange,
      req.body.max_recommended_bid,
      req.body.default_coefficient,
    ],
  };
  PythonShell.run(
    'create_campaigns_for_good_p_widgets_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createCampaignsForGoodPWidgetsDataset;
