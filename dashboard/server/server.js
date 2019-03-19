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

const createAdsForOneCampaignDataset = require('./controllers/data_acquisition_controllers/create_ads_for_one_campaign_dataset');
const createCampaignsForOneAdDataset = require('./controllers/data_acquisition_controllers/create_campaigns_for_one_ad_dataset');
const createCampaignsForOneOfferDataset = require('./controllers/data_acquisition_controllers/create_campaigns_for_one_offer_dataset');
const createCampaignsForOnePWidgetDataset = require('./controllers/data_acquisition_controllers/create_campaigns_for_one_p_widget_dataset');
const createCampaignsForOneCWidgetDataset = require('./controllers/data_acquisition_controllers/create_campaigns_for_one_c_widget_dataset');
const createPWidgetsForOneCampaignDataset = require('./controllers/data_acquisition_controllers/create_p_widgets_for_one_campaign_dataset');
const createPWidgetsForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_p_widgets_for_all_campaigns_dataset');
const createCWidgetsForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_c_widgets_for_all_campaigns_dataset');
const createCWidgetsForOnePWidgetDataset = require('./controllers/data_acquisition_controllers/create_c_widgets_for_one_p_widget_dataset');
const createAdsForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_ads_for_all_campaigns_dataset');
const createOffersForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_offers_for_all_campaigns_dataset');
const createOffersForOneCampaignDataset = require('./controllers/data_acquisition_controllers/create_offers_for_one_campaign_dataset');
const createOffersForOneFlowRuleDataset = require('./controllers/data_acquisition_controllers/create_offers_for_one_flow_rule_dataset');
const createAdsForOneCampaignReport = require('./controllers/data_analysis_controllers/create_ads_for_one_campaign_report');
const createCampaignsForOneOfferReport = require('./controllers/data_analysis_controllers/create_campaigns_for_one_offer_report');
const createCampaignsForOnePWidgetReport = require('./controllers/data_analysis_controllers/create_campaigns_for_one_p_widget_report');
const createCampaignsForOneCWidgetReport = require('./controllers/data_analysis_controllers/create_campaigns_for_one_c_widget_report');
const createPWidgetsForOneCampaignReport = require('./controllers/data_analysis_controllers/create_p_widgets_for_one_campaign_report');
const createCWidgetsForOnePWidgetReport = require('./controllers/data_analysis_controllers/create_c_widgets_for_one_p_widget_report');
const createPWidgetsForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_p_widgets_for_all_campaigns_report');
const createCWidgetsForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_c_widgets_for_all_campaigns_report');
const createDaysForOneCampaignReport = require('./controllers/data_analysis_controllers/create_days_for_one_campaign_report');
const createCampaignsForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_campaigns_for_all_campaigns_report');
const createAdsForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_ads_for_all_campaigns_report');
const createOffersForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_offers_for_all_campaigns_report');
const createOffersForOneCampaignReport = require('./controllers/data_analysis_controllers/create_offers_for_one_campaign_report');
const createOffersForOneFlowRuleReport = require('./controllers/data_analysis_controllers/create_offers_for_one_flow_rule_report');
const createCampaignsForOneAdReport = require('./controllers/data_analysis_controllers/create_campaigns_for_one_ad_report');

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

/////// Data Acquisition Routes /////
app.post(
  '/api/createAdsForOneCampaignDataset',
  authenticate,
  createAdsForOneCampaignDataset,
);

app.post(
  '/api/createAdsForAllCampaignsDataset',
  authenticate,
  createAdsForAllCampaignsDataset,
);

app.post(
  '/api/createOffersForAllCampaignsDataset',
  authenticate,
  createOffersForAllCampaignsDataset,
);

app.post(
  '/api/createOffersForOneCampaignDataset',
  authenticate,
  createOffersForOneCampaignDataset,
);

app.post(
  '/api/createOffersForOneFlowRuleDataset',
  authenticate,
  createOffersForOneFlowRuleDataset,
);

app.post(
  '/api/createPWidgetsForOneCampaignDataset',
  authenticate,
  createPWidgetsForOneCampaignDataset,
);

app.post(
  '/api/createPWidgetsForAllCampaignsDataset',
  authenticate,
  createPWidgetsForAllCampaignsDataset,
);

app.post(
  '/api/createCWidgetsForAllCampaignsDataset',
  authenticate,
  createCWidgetsForAllCampaignsDataset,
);

app.post(
  '/api/createCWidgetsForOnePWidgetDataset',
  authenticate,
  createCWidgetsForOnePWidgetDataset,
);

app.post(
  '/api/createCWidgetsForOneCWidgetDataset',
  authenticate,
  createCWidgetsForOnePWidgetDataset,
);

app.post(
  '/api/createCampaignsForOneAdDataset',
  authenticate,
  createCampaignsForOneAdDataset,
);

app.post(
  '/api/createCampaignsForOneOfferDataset',
  authenticate,
  createCampaignsForOneOfferDataset,
);

app.post(
  '/api/createCampaignsForOnePWidgetDataset',
  authenticate,
  createCampaignsForOnePWidgetDataset,
);

app.post(
  '/api/createCampaignsForOneCWidgetDataset',
  authenticate,
  createCampaignsForOneCWidgetDataset,
);

//---------------------------------------

/////// Data Analysis Routes ///////////
app.post(
  '/api/createAdsForOneCampaignReport',
  authenticate,
  createAdsForOneCampaignReport,
);

app.post(
  '/api/createCampaignsForOnePWidgetReport',
  authenticate,
  createCampaignsForOnePWidgetReport,
);

app.post(
  '/api/createCampaignsForOneCWidgetReport',
  authenticate,
  createCampaignsForOneCWidgetReport,
);

app.post(
  '/api/createPWidgetsForOneCampaignReport',
  authenticate,
  createPWidgetsForOneCampaignReport,
);

app.post(
  '/api/createCWidgetsForOnePWidgetReport',
  authenticate,
  createCWidgetsForOnePWidgetReport,
);

app.post(
  '/api/createPWidgetsForAllCampaignsReport',
  authenticate,
  createPWidgetsForAllCampaignsReport,
);

app.post(
  '/api/createCWidgetsForAllCampaignsReport',
  authenticate,
  createCWidgetsForAllCampaignsReport,
);

app.post(
  '/api/createDaysForOneCampaignReport',
  authenticate,
  createDaysForOneCampaignReport,
);

app.post(
  '/api/createCampaignsForAllCampaignsReport',
  authenticate,
  createCampaignsForAllCampaignsReport,
);

app.post(
  '/api/createCampaignsForOneOfferReport',
  authenticate,
  createCampaignsForOneOfferReport,
);

app.post(
  '/api/createAdsForAllCampaignsReport',
  authenticate,
  createAdsForAllCampaignsReport,
);

app.post(
  '/api/createOffersForAllCampaignsReport',
  authenticate,
  createOffersForAllCampaignsReport,
);

app.post(
  '/api/createOffersForOneCampaignReport',
  authenticate,
  createOffersForOneCampaignReport,
);

app.post(
  '/api/createOffersForOneFlowRuleReport',
  authenticate,
  createOffersForOneFlowRuleReport,
);

app.post(
  '/api/createCampaignsForOneAdReport',
  authenticate,
  createCampaignsForOneAdReport,
);
//--------------------------------------------

app.use(express.static('../public'));

app.get('*', (req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

app.listen(process.env.PORT, () => {
  console.log(`dashboard server running on port ${process.env.PORT}`);
});
