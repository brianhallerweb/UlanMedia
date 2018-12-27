//@format
const mongoose = require('mongoose');

const pWidgetsForAllCampaignsTrainingData = new mongoose.Schema({
  pWidgetID: {
    type: String,
  },
  clicks: {
    type: Number,
  },
  cost: {
    type: Number,
  },
  revenue: {
    type: Number,
  },
  profit: {
    type: Number,
  },
  leads: {
    type: Number,
  },
  leadCPA: {
    type: Number,
  },
  leadCVR: {
    type: Number,
  },
  sales: {
    type: Number,
  },
  saleCPA: {
    type: Number,
  },
  globalStatusDecision: {
    type: String,
  },
});

const PWidgetsForAllCampaignsTrainingData = mongoose.model(
  'PWidgetsForAllCampaignsTrainingData',
  pWidgetsForAllCampaignsTrainingData,
);

module.exports = PWidgetsForAllCampaignsTrainingData;
