//@format
require('../../config/config');
require('./db/mongoose');

const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const {PythonShell} = require('python-shell');

const fs = require('fs');
const addToList = require('./addToList');

const login = require('./controllers/user_controllers/login');
const logout = require('./controllers/user_controllers/logout');

const createGprsForEachPOfferDataset = require('./controllers/data_acquisition_controllers/create_gprs_for_each_p_offer_dataset');

const createDaysForOneOfferForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_days_for_one_offer_for_all_campaigns_dataset');
const createMonthsForOneOfferForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_months_for_one_offer_for_all_campaigns_dataset');
const createDaysForOneAdForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_days_for_one_ad_for_all_campaigns_dataset');
const createMonthsForOneAdForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_months_for_one_ad_for_all_campaigns_dataset');
const createDaysForOneCountryForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_days_for_one_country_for_all_campaigns_dataset');
const createMonthsForOneCountryForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_months_for_one_country_for_all_campaigns_dataset');
const createMonthsForOneCWidgetForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_months_for_one_c_widget_for_all_campaigns_dataset');
const createDaysForOneAdForOneCampaignDataset = require('./controllers/data_acquisition_controllers/create_days_for_one_ad_for_one_campaign_dataset');
const createMonthsForOneAdForOneCampaignDataset = require('./controllers/data_acquisition_controllers/create_months_for_one_ad_for_one_campaign_dataset');
const createMonthsForOneCWidgetForOneCampaignDataset = require('./controllers/data_acquisition_controllers/create_months_for_one_c_widget_for_one_campaign_dataset');
const createDaysForOneCWidgetForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_days_for_one_c_widget_for_all_campaigns_dataset');
const createDaysForOneCWidgetForOneCampaignDataset = require('./controllers/data_acquisition_controllers/create_days_for_one_c_widget_for_one_campaign_dataset');
const createDaysForOneCampaignReport = require('./controllers/data_analysis_controllers/create_days_for_one_campaign_report');
const createDaysForOneOfferForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_days_for_one_offer_for_all_campaigns_report');
const createMonthsForOneOfferForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_months_for_one_offer_for_all_campaigns_report');
const createDaysForOneAdForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_days_for_one_ad_for_all_campaigns_report');
const createMonthsForOneAdForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_months_for_one_ad_for_all_campaigns_report');
const createDaysForOneCountryForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_days_for_one_country_for_all_campaigns_report');
const createMonthsForOneCountryForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_months_for_one_country_for_all_campaigns_report');
const createMonthsForOneCWidgetForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_months_for_one_c_widget_for_all_campaigns_report');
const createDaysForOneAdForOneCampaignReport = require('./controllers/data_analysis_controllers/create_days_for_one_ad_for_one_campaign_report');
const createMonthsForOneAdForOneCampaignReport = require('./controllers/data_analysis_controllers/create_months_for_one_ad_for_one_campaign_report');
const createMonthsForOneCWidgetForOneCampaignReport = require('./controllers/data_analysis_controllers/create_months_for_one_c_widget_for_one_campaign_report');
const createDaysForOneCWidgetForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_days_for_one_c_widget_for_all_campaigns_report');
const createDaysForOneCWidgetForOneCampaignReport = require('./controllers/data_analysis_controllers/create_days_for_one_c_widget_for_one_campaign_report');

const authenticate = require('./middleware/authenticate');
const User = require('./models/user');

///////////// Middleware /////////////////
app.use(bodyParser.json());

//---------------------------------------
//////// User routes //////////////
app.post('/api/users/login', login);

app.delete('/api/users/logout', authenticate, logout);
//---------------------------------------

//////// Campaign sets route //////////////
app.get('/api/readcampaignsets', (req, res) => {
  fs.readFile('../../campaign_sets/campaign_sets.json', 'utf8', (err, data) => {
    if (err) {
      throw Error(err);
    }
    res.send(data);
  });
});
//---------------------------------------

//////// exclude routes //////////////

app.post('/api/excludecampaignforoneporcwidget', authenticate, (req, res) => {
  const pythonOptions = {
    pythonPath: '/usr/bin/python3',
    pythonOptions: ['-u'],
    scriptPath: '../../scripts/misc/',
    args: [],
  };
  for (let arg in req.body) {
    pythonOptions.args.push(req.body[arg]);
  }
  PythonShell.run(
    'exclude_campaign_for_one_p_or_c_widget.py',
    pythonOptions,
    (err, results) => {
      if (err) throw err;
      res.send(results[0]);
    },
  );
});

//---------------------------------------

//////// widget list routes //////////////
app.get('/api/readwhitelist', (req, res) => {
  fs.readFile('../../widget_lists/whitelist.txt', 'utf8', (err, data) => {
    if (err) {
      throw Error(err);
    }
    const pWidgets = data.trim().split('\n');
    res.json(pWidgets);
  });
});

app.get('/api/readgreylist', (req, res) => {
  fs.readFile('../../widget_lists/greylist.txt', 'utf8', (err, data) => {
    if (err) {
      throw Error(err);
    }
    const pWidgets = data.trim().split('\n');
    res.json(pWidgets);
  });
});

app.get('/api/readblacklist', (req, res) => {
  fs.readFile('../../widget_lists/blacklist.txt', 'utf8', (err, data) => {
    if (err) {
      throw Error(err);
    }
    const pWidgets = data.trim().split('\n');
    res.json(pWidgets);
  });
});

app.post('/api/addtolist', authenticate, (req, res) => {
  res.json(addToList(req.body.widgetID, req.body.listType));
});

//---------------------------------------

//////// gprs for each p offer //////////////
app.post(
  '/api/createGprsForEachPOfferDataset',
  authenticate,
  createGprsForEachPOfferDataset,
);

//---------------------------------------

/////// Data Acquisition Routes /////

app.post(
  '/api/createDaysForOneOfferForAllCampaignsDataset',
  authenticate,
  createDaysForOneOfferForAllCampaignsDataset,
);

app.post(
  '/api/createMonthsForOneOfferForAllCampaignsDataset',
  authenticate,
  createMonthsForOneOfferForAllCampaignsDataset,
);

app.post(
  '/api/createDaysForOneAdForAllCampaignsDataset',
  authenticate,
  createDaysForOneAdForAllCampaignsDataset,
);

app.post(
  '/api/createMonthsForOneAdForAllCampaignsDataset',
  authenticate,
  createMonthsForOneAdForAllCampaignsDataset,
);

app.post(
  '/api/createDaysForOneCountryForAllCampaignsDataset',
  authenticate,
  createDaysForOneCountryForAllCampaignsDataset,
);

app.post(
  '/api/createMonthsForOneCountryForAllCampaignsDataset',
  authenticate,
  createMonthsForOneCountryForAllCampaignsDataset,
);

app.post(
  '/api/createMonthsForOneCWidgetForAllCampaignsDataset',
  authenticate,
  createMonthsForOneCWidgetForAllCampaignsDataset,
);

app.post(
  '/api/createDaysForOneAdForOneCampaignDataset',
  authenticate,
  createDaysForOneAdForOneCampaignDataset,
);

app.post(
  '/api/createMonthsForOneAdForOneCampaignDataset',
  authenticate,
  createMonthsForOneAdForOneCampaignDataset,
);

app.post(
  '/api/createMonthsForOneCWidgetForOneCampaignDataset',
  authenticate,
  createMonthsForOneCWidgetForOneCampaignDataset,
);

app.post(
  '/api/createDaysForOneCWidgetForAllCampaignsDataset',
  authenticate,
  createDaysForOneCWidgetForAllCampaignsDataset,
);

app.post(
  '/api/createDaysForOneCWidgetForOneCampaignDataset',
  authenticate,
  createDaysForOneCWidgetForOneCampaignDataset,
);

//---------------------------------------

/////// Data Analysis Routes ///////////
app.post(
  '/api/createDaysForOneOfferForAllCampaignsReport',
  authenticate,
  createDaysForOneOfferForAllCampaignsReport,
);

app.post(
  '/api/createMonthsForOneOfferForAllCampaignsReport',
  authenticate,
  createMonthsForOneOfferForAllCampaignsReport,
);

app.post(
  '/api/createDaysForOneAdForAllCampaignsReport',
  authenticate,
  createDaysForOneAdForAllCampaignsReport,
);

app.post(
  '/api/createMonthsForOneAdForAllCampaignsReport',
  authenticate,
  createMonthsForOneAdForAllCampaignsReport,
);

app.post(
  '/api/createDaysForOneCountryForAllCampaignsReport',
  authenticate,
  createDaysForOneCountryForAllCampaignsReport,
);

app.post(
  '/api/createMonthsForOneCountryForAllCampaignsReport',
  authenticate,
  createMonthsForOneCountryForAllCampaignsReport,
);

app.post(
  '/api/createMonthsForOneCWidgetForAllCampaignsReport',
  authenticate,
  createMonthsForOneCWidgetForAllCampaignsReport,
);

app.post(
  '/api/createDaysForOneAdForOneCampaignReport',
  authenticate,
  createDaysForOneAdForOneCampaignReport,
);

app.post(
  '/api/createMonthsForOneAdForOneCampaignReport',
  authenticate,
  createMonthsForOneAdForOneCampaignReport,
);

app.post(
  '/api/createMonthsForOneCWidgetForOneCampaignReport',
  authenticate,
  createMonthsForOneCWidgetForOneCampaignReport,
);

app.post(
  '/api/createDaysForOneCWidgetForAllCampaignsReport',
  authenticate,
  createDaysForOneCWidgetForAllCampaignsReport,
);

app.post(
  '/api/createDaysForOneCWidgetForOneCampaignReport',
  authenticate,
  createDaysForOneCWidgetForOneCampaignReport,
);

app.post(
  '/api/createDaysForOneCampaignReport',
  authenticate,
  createDaysForOneCampaignReport,
);

//--------------------------------------------

app.use(express.static('../public'));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.listen(process.env.PORT, () => {
  console.log(`dashboard server running on port ${process.env.PORT}`);
});
