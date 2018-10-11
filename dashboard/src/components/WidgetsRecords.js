//@format
import React, {Component} from 'react';
import WidgetRecord from './WidgetRecord';

class WidgetsRecords extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }
  createTable() {
    return (
      <table>
        <thead>
          <tr>
            <th>Campaign</th>
            <th>Widget ID</th>
            <th>Clicks</th>
            <th>Cost</th>
            <th>Revenue</th>
            <th>Profit</th>
            <th>Leads</th>
            <th>Lead CPA</th>
            <th>Sales</th>
            <th>Sale CPA</th>
            <th>Status</th>
            <th>Global Status</th>
          </tr>
        </thead>
        <tbody>
          {this.props.widgetRecords.map(widgetRecord => (
            <WidgetRecord key={widgetRecord.name} widgetRecord={widgetRecord} />
          ))}
        </tbody>
      </table>
    );
  }

  render() {
    return (
      <div>
        {!this.props.datasetCreated && <p>data sets loading...</p>}
        {this.props.error && <p>no widgets found</p>}
        {this.props.widgetRecords.length > 0 && this.createTable()}
      </div>
    );
  }
}

export default WidgetsRecords;
