//@format
import React, {Component} from 'react';
import Record from './Record';

class Records extends Component {
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
            <th>C Widget</th>
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
            <Record key={widgetRecord.mgid_id} widgetRecord={widgetRecord} />
          ))}
        </tbody>
      </table>
    );
  }

  render() {
    return (
      <div>
        {this.props.loading && <div className="loader" />}
        {this.props.error && <p>no widgets found</p>}
        {this.props.widgetRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
