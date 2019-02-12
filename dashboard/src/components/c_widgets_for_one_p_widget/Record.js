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
          {this.props.widgetRecord.widget_id !== 'summary' && (
            <div>
              <div className="rowLink">
                <Link
                  to={{
                    pathname: `/campaignsforonecwidget/${
                      this.props.widgetRecord.widget_id
                    }/`,
                  }}
                  target="_blank">
                  campaigns
                </Link>
              </div>
            </div>
          )}
        </td>
        <td>${this.props.widgetRecord.cost}</td>
        <td>${this.props.widgetRecord.revenue}</td>
        <td>${this.props.widgetRecord.profit}</td>
        <td>{this.props.widgetRecord.clicks}</td>
        <td>${this.props.widgetRecord.cpc}</td>
        <td>${this.props.widgetRecord.epc}</td>
        <td>{this.props.widgetRecord.leads}</td>
        <td>${this.props.widgetRecord.cpl}</td>
        <td>${this.props.widgetRecord.epl}</td>
        <td>{this.props.widgetRecord.lead_cvr}%</td>
        <td>{this.props.widgetRecord.sales}</td>
        <td>${this.props.widgetRecord.cps}</td>
        <td>${this.props.widgetRecord.eps}</td>
      </tr>
    );
  }
}

export default Record;
