//@format
import React, {Component} from 'react';

const CampaignRecord = ({campaign}) => (
  <tr>
    <td>{campaign.name}</td>
    <td>{campaign.clicks}</td>
    <td>{campaign.cost}</td>
    <td>{campaign.revenue}</td>
    <td>{campaign.profit}</td>
    <td>{campaign.leads}</td>
    <td>{campaign.lead_cpa}</td>
    <td>{campaign.max_lead_cpa}</td>
    <td>{campaign.sales}</td>
    <td>{campaign.sale_cpa}</td>
    <td>{campaign.max_sale_cpa}</td>
    <td>{campaign.epc}</td>
    <td>{campaign.c1}</td>
    <td>{campaign.c2}</td>
    <td>{campaign.c3}</td>
    <td>{campaign.c4}</td>
    <td>{campaign.c5}</td>
  </tr>
);

export default CampaignRecord;
