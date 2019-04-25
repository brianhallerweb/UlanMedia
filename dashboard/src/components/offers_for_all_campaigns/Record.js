//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.offerID = this.props.offer.offer_id;
    this.flowRule = this.props.offer.flow_rule;
    this.volWeight = this.props.offer.vol_weight;
    this.recWeight = this.props.offer.rec_weight;
    this.classification = this.props.offer.classification;
    this.roiScore = this.props.offer.roi_score;
    this.cvrScore = this.props.offer.cvr_score;
    this.gpr = this.props.offer.gpr;
    this.totalScore = this.props.offer.total_score;
    this.offerName = this.props.offer.offer_name;
    this.clicks = this.props.offer.clicks;
    this.cost = this.props.offer.cost;
    this.revenue = this.props.offer.revenue;
    this.profit = this.props.offer.profit;
    this.conversions = this.props.offer.conversions;
    this.cvr = this.props.offer.cvr;
    this.epc = this.props.offer.epc;
    this.cpa = this.props.offer.cpa;
    this.epa = this.props.offer.epa;
    this.cpc = this.props.offer.cpc;
    this.hasMismatchVolWeightAndRecWeight = this.props.offer.has_mismatch_vol_weight_and_rec_weight;
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

  outlineRow(hovered, hasMismatchVolWeightAndRecWeight) {
    if (hasMismatchVolWeightAndRecWeight) {
      return 'red';
    } else if (hovered) {
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
          outlineColor: this.outlineRow(
            this.state.hovered,
            this.hasMismatchVolWeightAndRecWeight,
          ),
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
          {this.offerName}
          <div>
            <InternalLink
              className={'rowLink'}
              to={`/campaignsforoneoffer/${this.offerID}/${this.offerName}`}
              target={'_blank'}
              label={'campaigns'}
            />
          </div>
        </td>
        <td>
          {this.flowRule}
          <div>
            <InternalLink
              className={'rowLink'}
              to={`/offersforoneflowrule/${this.flowRule}/
                  `}
              target={'_blank'}
              label={'offers'}
            />
          </div>
        </td>
        <td>{this.classification}</td>
        <td>
          {this.roiScore} + {this.cvrScore} + {this.gpr} = {this.totalScore}
        </td>
        <td>{this.volWeight}</td>
        <td>{this.recWeight}</td>
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
