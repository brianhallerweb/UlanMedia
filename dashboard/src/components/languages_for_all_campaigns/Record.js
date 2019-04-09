//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.languageName = this.props.language.language_name;
    this.classification = this.props.language.classification;
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
          {this.languageName}
          <div>
            <div className="rowLink">
              <Link
                to={{
                  pathname: `/campaignsforonelanguage/${this.languageName}/`,
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
        <td>{this.cvr}%</td>
        <td>{this.roi}%</td>
      </tr>
    );
  }
}

export default Record;
