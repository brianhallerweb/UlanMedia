//@format
const {PythonShell} = require('python-shell');

function createPWidgetsForOneCampaignDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.volID, req.body.dateRange, req.body.max_rec_bid],
  };
  PythonShell.run(
    'create_p_widgets_for_one_campaign_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createPWidgetsForOneCampaignDataset;
