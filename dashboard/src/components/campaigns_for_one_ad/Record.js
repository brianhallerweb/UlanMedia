//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.name = this.props.campaign.name;
    this.volID = this.props.campaign.vol_id;
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

  addRowLinks() {
    return (
      <div>
        <div className="rowLink">
          <Link
            to={{
              pathname: `/adsforonecampaign/${this.volID}/${this.name}/`,
            }}
            target="_blank">
            ads
          </Link>
        </div>
      </div>
    );
  }

  render() {
    return (
      <tr>
        <td>
          {this.name}
          {this.name !== 'summary' && this.addRowLinks()}
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
