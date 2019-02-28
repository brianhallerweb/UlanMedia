//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.offerID = this.props.offer.offerID;
    this.offerFlow = this.props.offer.offerFlow;
    this.offerName = this.props.offer.offerName;
    this.clicks = this.props.offer.clicks;
    this.cost = this.props.offer.cost;
    this.revenue = this.props.offer.revenue;
    this.profit = this.props.offer.profit;
    this.conversions = this.props.offer.conversions;
    this.cvr = this.props.offer.cvr;
    this.epc = this.props.offer.epc;
    this.cpa = this.props.offer.cpa;
    this.cpc = this.props.offer.epc;
    this.epa = this.props.offer.cpa;
    this.state = {};
  }

  render() {
    return (
      <tr>
        <td>
          {this.offerFlow}
          {this.offerFlow != 'summary' && (
            <div>
              <div className="rowLink">
                <Link
                  to={{
                    pathname: `/campaignsforoneoffer/${this.offerID}/${this
                      .offerName +
                      ' ' +
                      this.offerFlow}`,
                  }}
                  target="_blank">
                  campaigns
                </Link>
              </div>
            </div>
          )}
        </td>
        <td>{this.offerName}</td>
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
