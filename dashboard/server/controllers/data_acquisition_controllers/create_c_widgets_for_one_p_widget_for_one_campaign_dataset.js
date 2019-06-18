//@format
const {PythonShell} = require('python-shell');

function createCWidgetsForOnePWidgetForOneCampaignDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [
      req.body.volID,
      req.body.pWidget,
      req.body.dateRange,
      req.body.maxRecBid,
    ],
  };
  PythonShell.run(
    'create_c_widgets_for_one_p_widget_for_one_campaign_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createCWidgetsForOnePWidgetForOneCampaignDataset;
