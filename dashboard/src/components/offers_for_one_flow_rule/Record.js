//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.offerID = this.props.offer.offer_id;
    this.flowRule = this.props.offer.flow_rule;
    this.offerName = this.props.offer.offer_name;
    this.cost = this.props.offer.cost;
    this.revenue = this.props.offer.revenue;
    this.profit = this.props.offer.profit;
    this.clicks = this.props.offer.clicks;
    this.cpc = this.props.offer.cpc;
    this.epc = this.props.offer.epc;
    this.conversions = this.props.offer.conversions;
    this.cpa = this.props.offer.cpa;
    this.epa = this.props.offer.epa;
    this.cvr = this.props.offer.cvr;
    this.state = {};
  }

  render() {
    return (
      <tr>
        <td>
          {this.offerName}
          {this.offerName != 'summary' && (
            <div>
              <div className="rowLink">
                <Link
                  to={{
                    pathname: `/campaignsforoneoffer/${this.offerID}/${this
                      .offerName +
                      ' ' +
                      this.flowRule}`,
                  }}
                  target="_blank">
                  campaigns
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
