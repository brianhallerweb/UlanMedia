//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <tr>
        <td>
          {this.props.widgetRecord.widget_id}
          <div>
            <Link
              to={{
                pathname: `/widgets/parent/${this.props.widgetRecord.widget_id.match(
                  /^\d*/,
                )}`,
              }}
              target="_blank">
              all campaigns for parent widget
            </Link>
          </div>
          <div>
            <Link
              to={{
                pathname: `/widgets/child/${this.props.widgetRecord.widget_id}`,
              }}
              target="_blank">
              all campaigns for child widget
            </Link>
          </div>
        </td>
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
