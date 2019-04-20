//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.campaignName = this.props.campaign.campaign_name;
    this.volID = this.props.campaign.campaign_id;
    this.clicks = this.props.campaign.clicks;
    this.cost = this.props.campaign.cost;
    this.revenue = this.props.campaign.revenue;
    this.profit = this.props.campaign.profit;
    this.conversions = this.props.campaign.conversions;
    this.cvr = this.props.campaign.cvr;
    this.epc = this.props.campaign.epc;
    this.cpa = this.props.campaign.cpa;
    this.cpc = this.props.campaign.cpc;
    this.epa = this.props.campaign.epa;
    this.state = {};
  }

  outlineRow(hovered) {
    if (hovered) {
      return 'black';
    } else {
      return 'transparent';
    }
  }

  render() {
    return (
      <tr
        style={{
          outlineStyle: 'solid',
          outlineColor: this.outlineRow(this.state.hovered),
        }}
        className={this.state.clicked && 'clicked'}
        onMouseEnter={e => {
          this.setState({hovered: !this.state.hovered});
        }}
        onMouseLeave={e => {
          this.setState({hovered: !this.state.hovered});
        }}
        onClick={e => {
          this.setState({clicked: !this.state.clicked});
        }}>
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
      </tr>
    );
  }
}

export default Record;
