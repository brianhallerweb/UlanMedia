//@format
const {PythonShell} = require('python-shell');

function createMonthsForOnePWidgetForOneCampaignReport(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [req.body.pWidgetID, req.body.volID],
  };
  PythonShell.run(
    'create_months_for_one_p_widget_for_one_campaign_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createMonthsForOnePWidgetForOneCampaignReport;
