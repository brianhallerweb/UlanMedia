//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.campaignID = this.props.country.campaign_id;
    this.campaignName = this.props.country.campaign_name;
    this.clicks = this.props.country.clicks;
    this.cost = this.props.country.cost;
    this.revenue = this.props.country.revenue;
    this.profit = this.props.country.profit;
    this.conversions = this.props.country.conversions;
    this.cvr = this.props.country.cvr;
    this.epc = this.props.country.epc;
    this.cpa = this.props.country.cpa;
    this.cpc = this.props.country.cpc;
    this.epa = this.props.country.epa;
    this.roi = this.props.country.roi;
    this.state = {};
  }

  render() {
    return (
      <tr
        style={
          this.classification === 'bad' ? {backgroundColor: '#f7d9d9'} : null
        }>
        <td>
          {this.campaignName}
          {this.campaignName !== 'summary' && (
            <div>
              <div className="rowLink">
                <Link
                  to={{
                    pathname: `/countriesforonecampaign/${this.campaignID}/`,
                  }}
                  target="_blank">
                  countries
                </Link>
              </div>
            </div>
          )}
        </td>
        <td>${this.cost}</td>
        <td>${this.revenue}</td>
        <td>${this.profit}</td>
        <td>{this.clicks}</td>
        <td>${this.cpc}</td>
        <td>${this.epc}</td>
        <td>{this.conversions}</td>
        <td>${this.cpa}</td>
        <td>${this.epa}</td>
        <td>{this.cvr}%</td>
        <td>{this.roi}%</td>
      </tr>
    );
  }
}

export default Record;