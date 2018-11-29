//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.name = this.props.ad.name;
    this.clicks = this.props.ad.clicks;
    this.cost = this.props.ad.cost;
    this.revenue = this.props.ad.revenue;
    this.profit = this.props.ad.profit;
    this.conversions = this.props.ad.conversions;
    this.cvr = this.props.ad.cvr;
    this.epc = this.props.ad.epc;
    this.cpa = this.props.ad.cpa;
    this.state = {};
  }

  render() {
    return (
      <tr>
        <td>
          {this.name}
          <div>
            <div className="rowLink">
              <Link
                to={{
                  pathname: `/test/`,
                }}
                target="_blank">
                ads
              </Link>
            </div>
          </div>
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
