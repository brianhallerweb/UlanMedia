//@format
const {PythonShell} = require('python-shell');

function createCampaignsForOneChildWidgetDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.widgetID, req.body.dateRange],
  };
  PythonShell.run(
    'create_campaigns_for_one_child_widget_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.sendStatus(200);
    },
  );
}

module.exports = createCampaignsForOneChildWidgetDataset;
