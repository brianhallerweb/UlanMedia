//@format
const {PythonShell} = require('python-shell');

function createWidgetsForOneDomainForAllCampaignsReport(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [req.body.dateRange, req.body.domain],
  };
  PythonShell.run(
    'create_widgets_for_one_domain_for_all_campaigns_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createWidgetsForOneDomainForAllCampaignsReport;
