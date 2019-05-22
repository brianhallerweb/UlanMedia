//@format
const {PythonShell} = require('python-shell');

function createDaysForOneCountryForAllCampaignsReport(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_analysis_scripts/',
    args: [req.body.countryName],
  };
  PythonShell.run(
    'create_days_for_one_country_for_all_campaigns_report.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createDaysForOneCountryForAllCampaignsReport;
