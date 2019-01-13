//@format

function classifyPWidget(pWidgetID) {
   fetch(`/api/createCampaignsForOnePWidgetDataset`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'x-auth': localStorage.getItem('token'),
    },
    body: JSON.stringify({
      dateRange: 'oneeighty',
      widgetID: pWidgetID,
    }),
  })
    .then(res => {
      if (!res.ok) {
        throw Error(res.statusText);
      }
      return res;
    })
    .then(() =>
      fetch(`/api/createCampaignsForOnePWidgetReport`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-auth': localStorage.getItem('token'),
        },
        body: JSON.stringify({
          dateRange: 'oneeighty',
          widgetID: pWidgetID,
          c1Value: 0,
          c2Value: 0,
          c3Value: 0,
          c4Value: 0,
          c5Value: 0,
          c6Value1: 0,
          c6Value2: 0,
          c1: false,
          c2: false,
          c3: false,
          c4: false,
          c5: false,
          c6: false,
        }),
      }),
    )
    .then(res => res.json())
    .then(records => {
      console.log(makeFinalClassification(pWidgetID, records));
    })
    .catch(err => console.log(err));
}

////////////////////////////////
//helper functions
//
function makeFinalClassification(pWidgetID, campaignRecords) {
  const totals = calculateCampaignsTotals(campaignRecords);
  const campaignsCount = totals.campaignsCount;
  const goodCampaignsCount = totals.goodCampaignsCount;
  const badCampaignsCount = totals.badCampaignsCount;
  const waitCampaignsCount = totals.waitCampaignsCount;
  const totalProfit = totals.totalProfit;

  return finalJudgement(
    pWidgetID,
    campaignsCount,
    goodCampaignsCount,
    badCampaignsCount,
    waitCampaignsCount,
    totalProfit,
  );
}

function calculateCampaignsTotals(campaignRecords) {
  let campaignsCount = 0;
  let goodCampaignsCount = 0;
  let badCampaignsCount = 0;
  let waitCampaignsCount = 0;
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
    } else if (
      campaign.name !== 'summary' &&
      campaign.lead_cvr > 0.25 &&
      (campaign.leads >= 3 || campaign.sales >= 1)
    ) {
      goodCampaignsCount += 1;
    } else {
      waitCampaignsCount += 1;
    }
  }
  return {
    campaignsCount,
    goodCampaignsCount,
    badCampaignsCount,
    waitCampaignsCount,
    totalProfit,
  };
}

function finalJudgement(
  pWidgetID,
  campaignsCount,
  goodCampaignsCount,
  badCampaignsCount,
  waitCampaignsCount,
  totalProfit,
) {
  if (goodCampaignsCount >= 3 && badCampaignsCount === 0) {
    return `${pWidgetID} is WHITE`;
  } else if (goodCampaignsCount > 0 && badCampaignsCount > 0) {
    return `${pWidgetID} is GREY`;
  } else if (goodCampaignsCount === 0 && badCampaignsCount >= 3) {
    return `${pWidgetID} is BLACK`;
  } else if (
    goodCampaignsCount === 0 &&
    badCampaignsCount > 0 &&
    totalProfit <= -60
  ) {
    return `${pWidgetID} is BLACK`;
  } else {
    return `${pWidgetID} is wait`;
  }
}

export {classifyPWidget};
