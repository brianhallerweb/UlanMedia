//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';
import ExternalLink from '../utilities/ExternalLink';

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
          {this.countryName}
          <div>
            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/campaignsforonecountry/${this.countryName}/`}
              target={'_blank'}
              label={'campaigns'}
            />

            <ExternalLink
              className={'rowLink'}
              href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_58c65a87-77bb-4959-908d-b402a3f4407a/report/country-code,custom-variable-1,campaign?dateRange=last-30-days&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=countryName&columns=customVariable1&columns=campaignName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&columns=campaignId&columns=cpa&filter=${
                this.countryName
              }&limit=1000&reportType=tree&include=ALL&reportDataType=0&tagsGrouping=country-code&valueFiltersGrouping=country-code&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`}
              target={'_blank'}
              label={'widgets'}
            />
          </div>
        </td>
        {this.stylizeClassificationText(this.classification)}
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
