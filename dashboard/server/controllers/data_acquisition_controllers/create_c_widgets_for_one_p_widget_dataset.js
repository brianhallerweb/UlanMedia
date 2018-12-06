//@format
const {PythonShell} = require('python-shell');

function createCWidgetsForOnePWidgetDataset(req, res) {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/data_acquisition_scripts/',
    args: [req.body.pWidgetID, req.body.dateRange],
  };
  PythonShell.run(
    'create_c_widgets_for_one_p_widget_dataset.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.sendStatus(200);
    },
  );
}

module.exports = createCWidgetsForOnePWidgetDataset;
