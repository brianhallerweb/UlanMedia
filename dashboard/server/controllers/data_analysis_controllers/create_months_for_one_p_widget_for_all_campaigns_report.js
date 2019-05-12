//@format
const {PythonShell} = require('python-shell');

function createMonthsForOnePWidgetForAllCampaignsReport(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [req.body.pWidgetID],
  };
  PythonShell.run(
    'create_months_for_one_p_widget_for_all_campaigns_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createMonthsForOnePWidgetForAllCampaignsReport;
