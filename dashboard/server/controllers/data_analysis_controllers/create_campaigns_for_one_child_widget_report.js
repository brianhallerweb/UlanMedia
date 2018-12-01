//@format
const {PythonShell} = require('python-shell');

function createCampaignsForOneChildWidgetReport(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [
      req.body.dateRange,
      req.body.widgetID,
      req.body.precondition,
      req.body.precondition2,
      req.body.c1,
      req.body.c2,
    ],
  };
  PythonShell.run(
    'create_campaigns_for_one_child_widget_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createCampaignsForOneChildWidgetReport;
