//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.image = this.props.ad.image;
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
	    {this.image}
	    <div>
              <div className="rowLink">
                <Link
                  to={{
                    pathname: `/ad/${this.image}/`,
                  }}
                  target="_blank">
                  ad 
                </Link>
              </div>
	    </div>
	</td>
        <td>{this.clicks}</td>
        <td>${this.cost.toFixed(2)}</td>
        <td>${this.revenue}</td>
        <td>${this.profit.toFixed(2)}</td>
        <td>{this.conversions}</td>
        <td>{this.cvr.toFixed(2)}%</td>
        <td>${this.epc.toFixed(3)}</td>
        <td>${this.cpa.toFixed(2)}</td>
      </tr>
    );
  }
}

export default Record;
