//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';
import ExternalLink from '../utilities/ExternalLink';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {clicked: false};
  }

  componentDidMount() {
    if (
      this.props.campaignRecord.status === 'excluded' ||
      this.props.campaignRecord.status === 'inactive'
    ) {
      this.setState({clicked: true});
    }
  }

  addRowLinks() {
    return (
      <div>
        <InternalLink
          className={'rowLink'}
          stopPropagation={true}
          to={`/pwidgetsforonecampaign/${this.props.campaignRecord.vol_id}/${
            this.props.campaignRecord.name
          }/
              `}
          target={'_blank'}
          label={'p_widgets'}
        />

        <ExternalLink
          className={'rowLink'}
          href={`https://dashboard.mgid.com/advertisers/campaign-quality-analysis/id/${
            this.props.campaignRecord.mgid_id
          }?search=${this.props.campaignRecord.widget_id}`}
          target={'_blank'}
          label={'mgid'}
        />

        <ExternalLink
          className={'rowLink'}
          href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_9a96a80f-83fd-4721-b245-5d2d82077632/report/country-code?dateRange=custom-date&chart=0&columns=offerName&columns=offerId&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&limit=100&reportType=&include=ALL&reportDataType=0&tagsGrouping=offer&valueFiltersGrouping=offer&from=${
            this.props.volRequestStartDate
          }T00:00:00Z&to=${
            this.props.volRequestEndDate
          }T00:00:00Z&filter1=campaign&filter1Value=${
            this.props.campaignRecord.vol_id
          }&filter2=custom-variable-1&filter2Value=${
            this.props.campaignRecord.widget_id
          }`}
          target={'_blank'}
          label={'countries'}
        />

        <ExternalLink
          className={'rowLink'}
          href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_024fdcf6-6333-46d7-87dc-ade02e7b2f80/report/language?dateRange=custom-date&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=countryName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=100&reportType=&include=ALL&reportDataType=0&tagsGrouping=language&valueFiltersGrouping=language&from=${
            this.props.volRequestStartDate
          }T00:00:00Z&to=${
            this.props.volRequestEndDate
          }T00:00:00Z&filter1=campaign&filter1Value=${
            this.props.campaignRecord.vol_id
          }&filter2=custom-variable-1&filter2Value=${
            this.props.campaignRecord.widget_id
          }`}
          target={'_blank'}
          label={'languages'}
        />

        <ExternalLink
          className={'rowLink'}
          href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_32154ab0-b614-4ac5-b017-6d5a18447bc5/report/month?dateRange=custom-date&sortKey=month&sortDirection=desc&page=1&chart=0&columns=month&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=table&include=ALL&reportDataType=0&tagsGrouping=month&valueFiltersGrouping=month&from=${
            this.props.volRequestStartDate
          }T00:00:00Z&to=${
            this.props.volRequestEndDate
          }T00:00:00Z&filter1=campaign&filter1Value=${
            this.props.campaignRecord.vol_id
          }&filter2=custom-variable-1&filter2Value=${
            this.props.campaignRecord.widget_id
          }`}
          target={'_blank'}
          label={'months'}
        />

        <ExternalLink
          className={'rowLink'}
          href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_32154ab0-b614-4ac5-b017-6d5a18447bc5/report/day?dateRange=custom-date&sortKey=day&sortDirection=desc&page=1&chart=0&columns=day&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=table&include=ALL&reportDataType=0&tagsGrouping=day&valueFiltersGrouping=day&from=${
            this.props.volRequestStartDate
          }T00:00:00Z&to=${
            this.props.volRequestEndDate
          }T00:00:00Z&filter1=campaign&filter1Value=${
            this.props.campaignRecord.vol_id
          }&filter2=custom-variable-1&filter2Value=${
            this.props.campaignRecord.widget_id
          }`}
          target={'_blank'}
          label={'days'}
        />

        <InternalLink
          className={'rowLink'}
          to={`/excludecampaignforonecwidgetconfirmation/${
            this.props.campaignRecord.widget_id
          }/${this.props.campaignRecord.mgid_id}`}
          target={'_blank'}
          label={'exclude'}
        />
      </div>
    );
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

  outlineRow(hovered, isBadAndIncluded) {
    if (isBadAndIncluded) {
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
          backgroundColor: this.colorizeRow(
            this.props.campaignRecord.classification,
          ),
          outlineStyle: 'solid',
          outlineColor: this.outlineRow(
            this.state.hovered,
            this.props.campaignRecord.is_bad_and_included,
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
          {this.props.campaignRecord.name}
          {this.props.campaignRecord.name !== 'summary' && this.addRowLinks()}
        </td>
        {this.stylizeClassificationText(
          this.props.campaignRecord.classification,
        )}
        <td>${this.props.campaignRecord.cost}</td>
        <td>${this.props.campaignRecord.revenue}</td>
        <td>${this.props.campaignRecord.profit}</td>
        <td>{this.props.campaignRecord.clicks}</td>
        <td>${this.props.campaignRecord.cpc}</td>
        <td>${this.props.campaignRecord.epc}</td>
        <td>${this.props.campaignRecord.mpc}</td>
        <td>{this.props.campaignRecord.leads}</td>
        <td>${this.props.campaignRecord.cpl}</td>
        <td>${this.props.campaignRecord.epl}</td>
        <td>${this.props.campaignRecord.mpl}</td>
        <td>{this.props.campaignRecord.sales}</td>
        <td>${this.props.campaignRecord.cps}</td>
        <td>${this.props.campaignRecord.eps}</td>
        <td>${this.props.campaignRecord.mps}</td>
        <td>{this.props.campaignRecord.status}</td>
      </tr>
    );
  }
}

export default Record;
