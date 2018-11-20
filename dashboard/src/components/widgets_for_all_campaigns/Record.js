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
            <div className="rowLink">
              <Link
                to={{
                  pathname: `/widget/parent/${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}`,
                }}
                target="_blank">
                parent widget
              </Link>
            </div>
            <div className="rowLink">
              <Link
                to={{
                  pathname: `/widget/child/${
                    this.props.widgetRecord.widget_id
                  }`,
                }}
                target="_blank">
                child widget
              </Link>
            </div>
          </div>
        </td>
        <td>{this.props.widgetRecord.clicks}</td>
        <td>${this.props.widgetRecord.cost.toFixed(2)}</td>
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
