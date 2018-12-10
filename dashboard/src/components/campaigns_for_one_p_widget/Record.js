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
                this.props.widgetRecord.vol_id
              }/${this.props.widgetRecord.mgid_id}/${
                this.props.widgetRecord.max_lead_cpa
              }/${this.props.widgetRecord.name}/
              `,
            }}
            target="_blank">
            p widgets
          </Link>
        </div>

        <div className="rowLink">
          <a
            href={`http://ulanmedia.com/mgid/exclude-widgets-form.php?campaignIDs=${
              this.props.widgetRecord.mgid_id
            }&widgetIDs=${this.props.widgetRecord.widget_id.match(/^\d*/)}`}
            target="_blank">
            exclude
          </a>
        </div>

        <div className="rowLink">
          <a
            href={`https://dashboard.mgid.com/advertisers/campaign-quality-analysis/id/${
              this.props.widgetRecord.mgid_id
            }?search=${this.props.widgetRecord.widget_id.match(/^\d*/)}`}
            target="_blank">
            mgid
          </a>
        </div>
      </div>
    );
  }

  render() {
    console.log(this.props.widgetRecord);
    return (
      <tr>
        <td>
          {this.props.widgetRecord.name}
          {this.props.widgetRecord.name !== 'summary' && this.addRowLinks()}
        </td>
        <td>{this.props.widgetRecord.widget_id}</td>
        <td>{this.props.widgetRecord.clicks}</td>
        <td>${this.props.widgetRecord.cost}</td>
        <td>${this.props.widgetRecord.revenue}</td>
        <td>${this.props.widgetRecord.profit}</td>
        <td>{this.props.widgetRecord.leads}</td>
        <td>${this.props.widgetRecord.lead_cpa}</td>
        <td>{this.props.widgetRecord.sales}</td>
        <td>${this.props.widgetRecord.sale_cpa}</td>
        <td>{this.props.widgetRecord.status}</td>
        <td>{this.props.widgetRecord.global_status}</td>
      </tr>
    );
  }
}

export default Record;
