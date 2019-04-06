//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.countryName = this.props.country.country_name;
    this.classification = this.props.country.classification;
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
          {this.countryName}
          <div>
            <div className="rowLink">
              <Link
                to={{
                  pathname: `/campaignsforonecountry/${this.countryName}/`,
                }}
                target="_blank">
                campaigns
              </Link>
            </div>
          </div>
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
        <td>{this.cvr}</td>
      </tr>
    );
  }
}

export default Record;
