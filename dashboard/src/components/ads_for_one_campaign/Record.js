//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.image = this.props.ad.image;
    this.classification = this.props.ad.classification;
    this.clicks = this.props.ad.clicks;
    this.cost = this.props.ad.cost;
    this.revenue = this.props.ad.revenue;
    this.profit = this.props.ad.profit;
    this.conversions = this.props.ad.conversions;
    this.cvr = this.props.ad.cvr;
    this.epc = this.props.ad.epc;
    this.cpa = this.props.ad.cpa;
    this.cpc = this.props.ad.cpc;
    this.epa = this.props.ad.epa;
    this.rank = this.props.ad.rank;
    this.finalRank = this.props.ad.final_rank;
    this.globalRank = this.props.ad.global_rank;
    this.state = {};
  }
  addRowLinks() {
    return (
      <div>
        <div className="rowLink">
          <Link
            to={{
              pathname: `/campaignsforonead/${this.image}/`,
            }}
            target="_blank">
            campaigns
          </Link>
        </div>
      </div>
    );
  }

  render() {
    return (
      <tr>
        <td>
          {this.image}
          {this.image !== 'summary' && this.addRowLinks()}
        </td>
        <td>{this.classification}</td>
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
        <td>{this.rank}</td>
        <td>{this.finalRank}</td>
        <td>{this.globalRank}</td>
      </tr>
    );
  }
}

export default Record;
