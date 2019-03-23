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
            p widgets
          </Link>
        </div>
        <div className="rowLink">
          <Link
            to={{
              pathname: `/excludecampaignforonepwidgetconfirmation/${this.props.campaignRecord.widget_id.match(
                /^\d*/,
              )}/${this.props.campaignRecord.mgid_id}`,
            }}
            target="_blank">
            exclude
          </Link>
        </div>
        <div className="rowLink">
          <a
            href={`https://dashboard.mgid.com/advertisers/campaign-quality-analysis/id/${
              this.props.campaignRecord.mgid_id
            }?search=${this.props.campaignRecord.widget_id.match(/^\d*/)}`}
            target="_blank">
            mgid
          </a>
        </div>

        <div className="rowLink">
          <a
            href={`https://panel-api.voluum.com/report?from=${
              this.props.volRequestStartDate
            }T00:00:00Z&to=${
              this.props.volRequestEndDate
            }T00:00:00Z&tz=America%2FLos_Angeles&filter=${
              this.props.campaignRecord.widget_id
            }&conversionTimeMode=VISIT&sort=month&direction=desc&columns=month&columns=customVariable1&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&groupBy=month&groupBy=custom-variable-1&offset=0&limit=1000&include=ACTIVE&filter1=campaign&filter1Value=${
              this.props.campaignRecord.vol_id
            }`}
            target="_blank">
            months
          </a>
        </div>

        <div className="rowLink">
          <a
            href={`https://panel-api.voluum.com/report?from=${
              this.props.volRequestStartDate
            }T00:00:00Z&to=${
              this.props.volRequestEndDate
            }T00:00:00Z&tz=America%2FLos_Angeles&filter=${
              this.props.campaignRecord.widget_id
            }&conversionTimeMode=VISIT&sort=month&direction=desc&columns=month&columns=customVariable1&columns=visits&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&groupBy=month&groupBy=custom-variable-1&offset=0&limit=1000&include=ACTIVE&filter1=campaign&filter1Value=${
              this.props.campaignRecord.vol_id
            }`}
            target="_blank">
            days
          </a>
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
