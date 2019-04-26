//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.name = this.props.campaign.name;
    this.volID = this.props.campaign.vol_id;
    this.cost = this.props.campaign.cost;
    this.revenue = this.props.campaign.revenue;
    this.profit = this.props.campaign.profit;
    this.clicks = this.props.campaign.clicks;
    this.cpc = this.props.campaign.cpc;
    this.epc = this.props.campaign.epc;
    this.conversions = this.props.campaign.conversions;
    this.cpa = this.props.campaign.cpa;
    this.epa = this.props.campaign.epa;
    this.cvr = this.props.campaign.cvr;
    this.roi = this.props.campaign.roi;
    this.imps = this.props.campaign.imps;
    this.ctr = this.props.campaign.ctr;
    this.ppi = this.props.campaign.ppi;
    this.state = {clicked: false, hovered: false};
  }

  addRowLinks() {
    return (
      <div>
        <InternalLink
          className={'rowLink'}
	                  stopPropagation={true}

          to={`/adsforonecampaign/${this.volID}/${this.name}/`}
          target={'_blank'}
          label={'ads'}
        />
      </div>
    );
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
          {this.name}
          {this.name !== 'summary' && this.addRowLinks()}
        </td>
        <td>${this.cost}</td>
        <td>${this.revenue}</td>
        <td>${this.profit}</td>
        <td>{this.imps}</td>
        <td>${this.ppi}</td>
        <td>{this.clicks}</td>
        <td>{this.ctr}%</td>
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
