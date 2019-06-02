//@format
const {PythonShell} = require('python-shell');

function createCampaignsForOnePWidgetDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [
      req.body.pWidgetID,
      req.body.dateRange,
      req.body.max_rec_bid,
      req.body.default_coeff,
    ],
  };
  PythonShell.run(
    'create_campaigns_for_one_p_widget_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createCampaignsForOnePWidgetDataset;
