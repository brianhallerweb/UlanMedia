//@format
require('../../config/config');
require('./db/mongoose');

const express = require('express');
const app = express();
const path = require('path');
const bodyParser = require('body-parser');
const {PythonShell} = require('python-shell');

const login = require('./controllers/user_controllers/login');
const logout = require('./controllers/user_controllers/logout');
const createAdsForOneCampaignDataset = require('./controllers/data_acquisition_controllers/create_ads_for_one_campaign_dataset');
const createCampaignsForOneAdDataset = require('./controllers/data_acquisition_controllers/create_campaigns_for_one_ad_dataset');
const createCampaignsForOneTotalWidgetDataset = require('./controllers/data_acquisition_controllers/create_campaigns_for_one_total_widget_dataset');
const createCampaignsForOneParentWidgetDataset = require('./controllers/data_acquisition_controllers/create_campaigns_for_one_parent_widget_dataset');
const createCampaignsForOneChildWidgetDataset = require('./controllers/data_acquisition_controllers/create_campaigns_for_one_child_widget_dataset');
const createAdsForAllCampaignsDataset = require('./controllers/data_acquisition_controllers/create_ads_for_all_campaigns_dataset');
const createAdsForOneCampaignReport = require('./controllers/data_analysis_controllers/create_ads_for_one_campaign_report');
const createCampaignsForOneTotalWidgetReport = require('./controllers/data_analysis_controllers/create_campaigns_for_one_total_widget_report');
const createCampaignsForOneParentWidgetReport = require('./controllers/data_analysis_controllers/create_campaigns_for_one_parent_widget_report');
const createCampaignsForOneChildWidgetReport = require('./controllers/data_analysis_controllers/create_campaigns_for_one_child_widget_report');
const createWidgetsForOneCampaignReport = require('./controllers/data_analysis_controllers/create_widgets_for_one_campaign_report');
const createWidgetsForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_widgets_for_all_campaigns_report');
const createDaysForOneCampaignReport = require('./controllers/data_analysis_controllers/create_days_for_one_campaign_report');
const createCampaignsForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_campaigns_for_all_campaigns_report');
const createAdsForAllCampaignsReport = require('./controllers/data_analysis_controllers/create_ads_for_all_campaigns_report');
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
  '/api/createCampaignsForOneAdDataset',
  authenticate,
  createCampaignsForOneAdDataset,
);

app.post(
  '/api/createCampaignsForOneTotalWidgetDataset',
  authenticate,
  createCampaignsForOneTotalWidgetDataset,
);

app.post(
  '/api/createCampaignsForOneParentWidgetDataset',
  authenticate,
  createCampaignsForOneParentWidgetDataset,
);

app.post(
  '/api/createCampaignsForOneChildWidgetDataset',
  authenticate,
  createCampaignsForOneChildWidgetDataset,
);
//---------------------------------------

/////// Data Analysis Routes ///////////
app.post(
  '/api/createAdsForOneCampaignReport',
  authenticate,
  createAdsForOneCampaignReport,
);

app.post(
  '/api/createCampaignsForOneTotalWidgetReport',
  authenticate,
  createCampaignsForOneTotalWidgetReport,
);

app.post(
  '/api/createCampaignsForOneParentWidgetReport',
  authenticate,
  createCampaignsForOneParentWidgetReport,
);

app.post(
  '/api/createCampaignsForOneChildWidgetReport',
  authenticate,
  createCampaignsForOneChildWidgetReport,
);

app.post(
  '/api/createWidgetsForOneCampaignReport',
  authenticate,
  createWidgetsForOneCampaignReport,
);

app.post(
  '/api/createWidgetsForAllCampaignsReport',
  authenticate,
  createWidgetsForAllCampaignsReport,
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
  '/api/createAdsForAllCampaignsReport',
  authenticate,
  createAdsForAllCampaignsReport,
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
