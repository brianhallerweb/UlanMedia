//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {badAndIncluded: false};
  }

  componentDidMount() {
    if (this.props.campaignRecord.badAndIncluded) {
      this.setState({badAndIncluded: true});
    }
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
              }/${this.props.campaignRecord.mgid_id}/${
                this.props.campaignRecord.max_lead_cpa
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
              pathname: `/excludecampaignconfirmation/${this.props.campaignRecord.widget_id.match(
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
      </div>
    );
  }

  render() {
    return (
      <tr
        style={this.state.badAndIncluded ? {backgroundColor: '#f08080'} : null}>
        <td>
          {this.props.campaignRecord.name}
          {this.props.campaignRecord.name !== 'summary' && this.addRowLinks()}
        </td>
        {this.stylizeClassification(this.props.campaignRecord.classification)}
        <td>{this.props.campaignRecord.clicks}</td>
        <td>${this.props.campaignRecord.cost}</td>
        <td>${this.props.campaignRecord.revenue}</td>
        <td>${this.props.campaignRecord.profit}</td>
        <td>{this.props.campaignRecord.leads}</td>
        <td>${this.props.campaignRecord.lead_cpa}</td>
        <td>${this.props.campaignRecord.max_lead_cpa}</td>
        <td>{this.props.campaignRecord.lead_cvr}%</td>
        <td>{this.props.campaignRecord.sales}</td>
        <td>${this.props.campaignRecord.sale_cpa}</td>
        <td>{this.props.campaignRecord.status}</td>
      </tr>
    );
  }
}

export default Record;
