//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  stylizeClassification(row) {
    if ((row === 'bad') | (row === 'half bad')) {
      return <td style={{color: 'red', fontWeight: 900}}>{row}</td>;
    } else if ((row === 'good') | (row === 'half good')) {
      return <td style={{color: 'green', fontWeight: 900}}>{row}</td>;
    } else {
      return <td>{row}</td>;
    }
  }

  addRowLinks() {
    return (
      <div>
        <div className="rowLink">
          <Link
            to={{
              pathname: `/pwidgetsforonecampaign/${
                this.props.campaignRecord.vol_id
              }/${this.props.campaignRecord.name}/
              `,
            }}
            target="_blank">
            p_widgets
          </Link>
        </div>

        <div className="rowLink">
          <a
            href={`https://dashboard.mgid.com/advertisers/campaign-quality-analysis/id/${
              this.props.campaignRecord.mgid_id
            }?search=${this.props.campaignRecord.widget_id}`}
            target="_blank">
            mgid
          </a>
        </div>

        <div className="rowLink">
          <a
            href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_32154ab0-b614-4ac5-b017-6d5a18447bc5/report/month?dateRange=custom-date&sortKey=month&sortDirection=desc&page=1&chart=0&columns=month&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=table&include=ALL&reportDataType=0&tagsGrouping=month&valueFiltersGrouping=month&from=${
              this.props.volRequestStartDate
            }T00:00:00Z&to=${
              this.props.volRequestEndDate
            }T00:00:00Z&filter1=campaign&filter1Value=${
              this.props.campaignRecord.vol_id
            }&filter2=custom-variable-1&filter2Value=${
              this.props.campaignRecord.widget_id
            }`}
            target="_blank">
            months
          </a>
        </div>

        <div className="rowLink">
          <a
            href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_32154ab0-b614-4ac5-b017-6d5a18447bc5/report/day?dateRange=custom-date&sortKey=day&sortDirection=desc&page=1&chart=0&columns=day&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=1000&reportType=table&include=ALL&reportDataType=0&tagsGrouping=day&valueFiltersGrouping=day&from=${
              this.props.volRequestStartDate
            }T00:00:00Z&to=${
              this.props.volRequestEndDate
            }T00:00:00Z&filter1=campaign&filter1Value=${
              this.props.campaignRecord.vol_id
            }&filter2=custom-variable-1&filter2Value=${
              this.props.campaignRecord.widget_id
            }`}
            target="_blank">
            days
          </a>
        </div>

        <div className="rowLink">
          <Link
            to={{
              pathname: `/excludecampaignforonecwidgetconfirmation/${
                this.props.campaignRecord.widget_id
              }/${this.props.campaignRecord.mgid_id}`,
            }}
            target="_blank">
            exclude
          </Link>
        </div>
      </div>
    );
  }

  render() {
    return (
      <tr
        style={
          this.props.campaignRecord.is_bad_and_included
            ? {backgroundColor: '#f7d9d9'}
            : null
        }>
        <td>
          {this.props.campaignRecord.name}
          {this.props.campaignRecord.name !== 'summary' && this.addRowLinks()}
        </td>
        {this.stylizeClassification(this.props.campaignRecord.classification)}
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
