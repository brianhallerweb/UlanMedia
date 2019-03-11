//@format
const {PythonShell} = require('python-shell');

function createOffersForAllFlowRulesDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.dateRange],
  };
  PythonShell.run(
    'create_offers_for_all_flow_rules_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
}

module.exports = createOffersForAllFlowRulesDataset;
