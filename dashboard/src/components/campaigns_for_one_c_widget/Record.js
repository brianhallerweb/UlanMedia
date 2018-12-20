//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {};
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
          <a
            href={`http://ulanmedia.com/mgid/exclude-widgets-form.php?campaignIDs=${
              this.props.campaignRecord.mgid_id
            }&widgetIDs=${this.props.campaignRecord.widget_id.match(/^\d*/)}`}
            target="_blank">
            exclude
          </a>
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
      <tr>
        <td>
          {this.props.campaignRecord.name}
          {this.props.campaignRecord.name !== 'summary' && this.addRowLinks()}
        </td>
        <td>{this.props.campaignRecord.widget_id}</td>
        <td>{this.props.campaignRecord.clicks}</td>
        <td>${this.props.campaignRecord.cost}</td>
        <td>${this.props.campaignRecord.revenue}</td>
        <td>${this.props.campaignRecord.profit}</td>
        <td>{this.props.campaignRecord.leads}</td>
        <td>${this.props.campaignRecord.lead_cpa}</td>
        <td>{this.props.campaignRecord.lead_cvr}%</td>
        <td>{this.props.campaignRecord.sales}</td>
        <td>${this.props.campaignRecord.sale_cpa}</td>
        <td>{this.props.campaignRecord.status}</td>
        <td>{this.props.campaignRecord.global_status}</td>
      </tr>
    );
  }
}

export default Record;
