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
    this.roi = this.props.ad.roi;
    this.imps = this.props.ad.imps;
    this.ctr = this.props.ad.ctr;
    this.ppi = this.props.ad.ppi;
    this.globalRank = this.props.ad.global_rank;
    this.globalRankOrder = this.props.ad.global_rank_order;
    this.state = {clicked: false, hovered: false};
  }

  stylizeClassificationText(row) {
    if ((row === 'bad') | (row === 'half bad')) {
      return <td style={{color: 'red', fontWeight: 900}}>{row}</td>;
    } else if ((row === 'good') | (row === 'half good')) {
      return <td style={{color: 'green', fontWeight: 900}}>{row}</td>;
    } else {
      return <td>{row}</td>;
    }
  }

  colorizeRow(classification) {
    if (classification === 'good') {
      //green
      return '#eafcea';
    } else if (classification === 'half good') {
      //light green
      return '#edfcea';
    } else if (classification === 'bad') {
      //red
      return '#f7d9d9';
    } else if (classification === 'half bad') {
      //light red
      return '#f7d9e1';
    } else if (classification === 'not yet') {
      //light grey
      return '#fafafa';
    }
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
          backgroundColor: this.colorizeRow(this.classification),
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
          {this.image}
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
        </td>
        <td>
          {this.globalRankOrder} ({this.globalRank})
        </td>
        {this.stylizeClassificationText(this.classification)}
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
