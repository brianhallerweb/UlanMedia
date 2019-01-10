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
              pathname: `/campaignsforonepwidget/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}`,
            }}
            target="_blank">
            campaigns
          </Link>
        </div>

        <div className="rowLink">
          <Link
            to={{
              pathname: `/cwidgetsforonepwidget/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}`,
            }}
            target="_blank">
            c widgets
          </Link>
        </div>

        <div className="rowLink">
          <a
            href={`http://ulanmedia.com/mgid/exclude-widgets-form.php?campaignIDs=${
              this.props.mgidid
            }&widgetIDs=${this.props.widgetRecord.widget_id.match(/^\d*/)}`}
            target="_blank">
            exclude
          </a>
        </div>

        <div className="rowLink">
          <a
            href={`https://dashboard.mgid.com/advertisers/campaign-quality-analysis/id/${
              this.props.mgidid
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
	{this.props.widgetRecord.widget_id}
          {this.props.widgetRecord.widget_id !== 'summary' && this.addRowLinks()}
	</td>
        <td>{this.props.widgetRecord.clicks}</td>
        <td>${this.props.widgetRecord.cost}</td>
        <td>${this.props.widgetRecord.revenue}</td>
        <td>${this.props.widgetRecord.profit}</td>
        <td>{this.props.widgetRecord.leads}</td>
        <td>${this.props.widgetRecord.lead_cpa}</td>
        <td>{this.props.widgetRecord.lead_cvr}%</td>
        <td>{this.props.widgetRecord.sales}</td>
        <td>${this.props.widgetRecord.sale_cpa}</td>
        <td>{this.props.widgetRecord.status}</td>
        <td>{this.props.widgetRecord.global_status}</td>
      </tr>
    );
  }
}

export default Record;
