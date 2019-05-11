//@format
const {PythonShell} = require('python-shell');

function createDaysForOnePWidgetForOneCampaignDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.pWidgetID, req.body.volID],
  };
  PythonShell.run(
    'create_days_for_one_p_widget_for_one_campaign_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createDaysForOnePWidgetForOneCampaignDataset;
