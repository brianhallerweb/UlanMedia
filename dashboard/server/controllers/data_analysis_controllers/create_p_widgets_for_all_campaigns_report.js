//@format
const {PythonShell} = require('python-shell');

function createPWidgetsForAllCampaignsReport(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [],
  };
  for (let arg in req.body) {
    pythonOptions.args.push(req.body[arg]);
  }
  PythonShell.run(
    'create_p_widgets_for_all_campaigns_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createPWidgetsForAllCampaignsReport;
