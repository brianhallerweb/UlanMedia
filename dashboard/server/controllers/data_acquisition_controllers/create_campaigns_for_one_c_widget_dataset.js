//@format
const {PythonShell} = require('python-shell');

function createCampaignsForOneCWidgetDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.widgetID, req.body.dateRange, req.body.max_rec_bid],
  };
  PythonShell.run(
    'create_campaigns_for_one_c_widget_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createCampaignsForOneCWidgetDataset;
