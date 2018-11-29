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
        <td>${this.props.widgetRecord.profit.toFixed(2)}</td>
        <td>{this.props.widgetRecord.leads}</td>
        <td>${this.props.widgetRecord.lead_cpa.toFixed(2)}</td>
        <td>{this.props.widgetRecord.sales}</td>
        <td>${this.props.widgetRecord.sale_cpa.toFixed(2)}</td>
        <td>{this.props.widgetRecord.status}</td>
        <td>{this.props.widgetRecord.global_status}</td>
      </tr>
    );
  }
}

export default Record;
