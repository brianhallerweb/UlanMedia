//@format
const {PythonShell} = require('python-shell');

function createPWidgetsForAllCampaignsDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.dateRange],
  };
  PythonShell.run(
    'create_p_widgets_for_all_campaigns_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createPWidgetsForAllCampaignsDataset;