//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.campaignID = this.props.language.campaign_id;
    this.campaignName = this.props.language.campaign_name;
    this.clicks = this.props.language.clicks;
    this.cost = this.props.language.cost;
    this.revenue = this.props.language.revenue;
    this.profit = this.props.language.profit;
    this.conversions = this.props.language.conversions;
    this.cvr = this.props.language.cvr;
    this.epc = this.props.language.epc;
    this.cpa = this.props.language.cpa;
    this.cpc = this.props.language.cpc;
    this.epa = this.props.language.epa;
    this.roi = this.props.language.roi;
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
                    pathname: `/languagesforonecampaign/${this.campaignID}/${
                      this.campaignName
                    }/`,
                  }}
                  target="_blank">
                  languages
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
