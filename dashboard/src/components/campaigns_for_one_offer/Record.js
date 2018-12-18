//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.campaignName = this.props.campaign.campaignName;
    this.volID = this.props.campaign.campaignID;
    this.clicks = this.props.campaign.clicks;
    this.cost = this.props.campaign.cost;
    this.revenue = this.props.campaign.revenue;
    this.profit = this.props.campaign.profit;
    this.conversions = this.props.campaign.conversions;
    this.cvr = this.props.campaign.cvr;
    this.epc = this.props.campaign.epc;
    this.cpa = this.props.campaign.cpa;
    this.state = {};
  }

  render() {
    return (
      <tr>
        <td>
          {this.campaignName}
          {this.campaignName != 'summary' && (
            <div>
              <div className="rowLink">
                <Link
                  to={{
                    pathname: `/offersforonecampaign/${this.volID}/${
                      this.campaignName
                    }/`,
                  }}
                  target="_blank">
                  offers
                </Link>
              </div>
            </div>
          )}
        </td>
        <td>{this.clicks}</td>
        <td>${this.cost}</td>
        <td>${this.revenue}</td>
        <td>${this.profit}</td>
        <td>{this.conversions}</td>
        <td>{this.cvr}%</td>
        <td>${this.epc}</td>
        <td>${this.cpa}</td>
      </tr>
    );
  }
}

export default Record;
