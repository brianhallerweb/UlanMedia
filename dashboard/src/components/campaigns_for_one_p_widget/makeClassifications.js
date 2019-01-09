//@format

function makeClassifications(c1, c2, c3, c4, c5, c6, campaignRecords) {
  addCampaignClassifications(campaignRecords);

  const stopClassificationMessage = isCheckboxChecked(c1, c2, c3, c4, c5, c6);
  if (stopClassificationMessage) {
    return stopClassificationMessage;
  }

  const totals = calculateCampaignsTotals(campaignRecords);
  const campaignsCount = totals.campaignsCount;
  const goodCampaignsCount = totals.goodCampaignsCount;
  const badCampaignsCount = totals.badCampaignsCount;
  const totalProfit = totals.totalProfit;

  return classifyPWidget(
    campaignsCount,
    goodCampaignsCount,
    badCampaignsCount,
    totalProfit,
  );
}

//////////////////////////////////////////////////////
///////////////////////////////////////////////////
///////////////////////////////////////////////////
///////////////////////////////////////////////////
///////////////////////////////////////////////////
///////////////////////////////////////////////////
///////////////////////////////////////////////////

// helper functions

function addCampaignClassifications(campaignRecords) {
  for (let campaign of campaignRecords) {
    if (campaign.name === 'summary') {
      continue;
    }
    if (campaign.lead_cvr >= 0.25) {
      if (campaign.leads >= 3) {
        campaign.classification = 'good';
        continue;
      } else {
        if (campaign.sales >= 1) {
          campaign.classification = 'good';
          continue;
        } else {
          campaign.classification = 'wait';
          continue;
        }
      }
    } else {
      if (campaign.cost < 30 && campaign.clicks < 700) {
        campaign.classification = 'wait';
        continue;
      } else {
        campaign.classification = 'bad';
        continue;
      }
    }
  }
}

function isCheckboxChecked(c1, c2, c3, c4, c5, c6) {
  if (c1 || c2 || c3 || c3 || c4 || c5 || c6) {
    return 'all checkboxes must be unchecked to classify the p widget';
  }
}

function calculateCampaignsTotals(campaignRecords) {
  let campaignsCount = 0;
  let goodCampaignsCount = 0;
  let badCampaignsCount = 0;
  let totalProfit = 0;
  for (let campaign of campaignRecords) {
    if (campaign.name === 'summary') {
      totalProfit = campaign.profit;
    }

    if (campaign.name !== 'summary') {
      campaignsCount += 1;
    }

    if (
      campaign.name !== 'summary' &&
      campaign.lead_cvr < 0.25 &&
      (campaign.cost >= 30 || campaign.clicks >= 700)
    ) {
      badCampaignsCount += 1;
    }

    if (
      campaign.name !== 'summary' &&
      campaign.lead_cvr > 0.25 &&
      (campaign.leads >= 3 || campaign.sales >= 1)
    ) {
      goodCampaignsCount += 1;
    }
  }
  return {campaignsCount, goodCampaignsCount, badCampaignsCount, totalProfit};
}

function classifyPWidget(
  campaignsCount,
  goodCampaignsCount,
  badCampaignsCount,
  totalProfit,
) {
  if (goodCampaignsCount >= 3 && badCampaignsCount === 0) {
    return `According to the current flow chart\n\np widget is WHITE\n\np widget is good in ${goodCampaignsCount} campaigns\np widget is bad in ${badCampaignsCount} campaigns\n\nINCLUDE the it in all campaigns`;
  } else if (goodCampaignsCount > 0 && badCampaignsCount > 0) {
    return `According to the current flow chart\n\np widget is GREY\n\np widget is good in ${goodCampaignsCount} campaigns\np widget is bad in ${badCampaignsCount} campaigns\n\nEXCLUDE it in bad campaigns`;
  } else if (goodCampaignsCount === 0 && badCampaignsCount >= 3) {
    return `According to the the current flow chart\n\np widget is BLACK\n\np widget is good in ${goodCampaignsCount} campaigns\np widget is bad in ${badCampaignsCount} campaigns\n\nEXCLUDE it in all campaigns`;
  } else if (
    goodCampaignsCount === 0 &&
    badCampaignsCount > 0 &&
    totalProfit <= -60
  ) {
    return `According to the current flow chart\n\np widget is BLACK\n\np widget is good in ${goodCampaignsCount} campaigns\np widget is bad in ${badCampaignsCount} campaigns\np widget has a total loss of ${-1 *
      totalProfit}\n\nEXCLUDE it in all campaigns`;
  } else {
    return `According to the current flow chart\n\np widget is WAIT\n\nWAIT in all campaigns`;
  }
}

export default makeClassifications;
