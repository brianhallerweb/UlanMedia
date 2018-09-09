//@format
import React, {Component} from 'react';

class CampaignRecord extends Component {
  constructor(props) {
    super(props);
    this.clicks = this.props.campaign.clicks;
    this.cost = this.props.campaign.cost;
    this.revenue = this.props.campaign.revenue;
    this.profit = this.props.campaign.profit;
    this.leads = this.props.campaign.leads;
    this.lead_cpa = this.props.campaign.lead_cpa;
    this.max_lead_cpa = this.props.campaign.max_lead_cpa;
    this.sales = this.props.campaign.sales;
    this.sale_cpa = this.props.campaign.sale_cpa;
    this.max_sale_cpa = this.props.campaign.max_sale_cpa;
    this.epc = this.props.campaign.epc;
    this.state = {};
  }

  createTooltip(profit, maxSaleCPA, clicks, leads, cost, maxLeadCPA, leadCPA) {
    const textArr = [];
    if (clicks > 1000 && leads == 0) {
      textArr.push(
        `Campaign has more than 1000 clicks (${clicks}) but no leads (${leads}) --- (clicks > 1000 AND leads = 0)`,
      );
    }
    if (cost > 0.3 * maxSaleCPA && leadCPA > 2 * maxLeadCPA) {
      textArr.push(
        `Campaign cost (\$${cost}) is more than a third of maxSaleCPA (\$${0.3 *
          maxSaleCPA}) AND leadCPA (\$${leadCPA}) is more than 2x maxLeadCPA (\$${2 *
          maxLeadCPA}) --- (cost > 0.3*maxSaleCPA AND leadCPA > 2*maxLeadCPA)`,
      );
    }
    if (cost > 0.5 * maxSaleCPA && leadCPA > 1.5 * maxLeadCPA) {
      textArr.push(
        `Campaign cost (\$${cost}) is more than half of maxSaleCPA (\$${0.5 *
          maxSaleCPA}) AND leadCPA (\$${leadCPA}) is more than 1.5x maxLeadCPA (\$${1.5 *
          maxLeadCPA}) --- (cost > 0.5*maxSaleCPA AND leadCPA > 1.5*maxLeadCPA)`,
      );
    }
    if (cost > 2 * maxSaleCPA && leadCPA > maxLeadCPA) {
      textArr.push(
        `Campaign cost (\$${cost}) is more than 2x maxSaleCPA (\$${2 *
          maxSaleCPA}) AND leadCPA (\$${leadCPA}) is more than maxLeadCPA (\$${maxLeadCPA}) --- (cost > 2*maxSaleCPA AND leadCPA > maxLeadCPA)`,
      );
    }
    if (profit < -3 * maxSaleCPA) {
      textArr.push(
        `Campaign profit (\$${profit}) is less than -3x maxSaleCPA (\$${-3 *
          maxSaleCPA}) --- (profit < -3*maxSaleCPA)`,
      );
    }
    let toolTipText = '';
    for (let i = 0; i < textArr.length; i++) {
      toolTipText += `\u2022 ${textArr[i]}\n`;
    }
    return toolTipText;
  }

  render() {
    return (
      <tr>
        <td className="tooltip">
          {this.props.campaign.name}
          <span className="tooltiptext">
            {this.createTooltip(
              this.profit,
              this.max_sale_cpa,
              this.clicks,
              this.leads,
              this.cost,
              this.max_lead_cpa,
              this.lead_cpa,
            )}
          </span>
        </td>
        <td>{this.clicks}</td>
        <td>{this.cost}</td>
        <td>{this.revenue}</td>
        <td>{this.profit}</td>
        <td>{this.leads}</td>
        <td>{this.lead_cpa}</td>
        <td>{this.max_lead_cpa}</td>
        <td>{this.sales}</td>
        <td>{this.sale_cpa}</td>
        <td>{this.max_sale_cpa}</td>
        <td>{this.epc}</td>
      </tr>
    );
  }
}

export default CampaignRecord;
