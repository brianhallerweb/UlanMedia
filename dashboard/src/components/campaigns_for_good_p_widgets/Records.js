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
            <th>P Widget</th>
            <th>Current Bid</th>
            <th>Recommended Bid</th>
            <th>Current Coefficient</th>
            <th>Recommended Coefficient</th>
            <th>Cost</th>
            <th>Revenue</th>
            <th>Profit</th>
            <th>Clicks</th>
            <th>CPC</th>
            <th>EPC</th>
            <th>MPC</th>
            <th>Leads</th>
            <th>CPL</th>
            <th>EPL</th>
            <th>MPL</th>
            <th>Sales</th>
            <th>CPS</th>
            <th>EPS</th>
            <th>MPS</th>
            <th>Status</th>
            <th>Global Status</th>
          </tr>
        </thead>
        <tbody>
          {this.props.campaignRecords.map(campaignRecord => (
            <Record
              key={`${campaignRecord.name}${campaignRecord.widget_id}`}
              campaignRecord={campaignRecord}
            />
          ))}
        </tbody>
      </table>
    );
  }

  render() {
    return (
      <div>
        {this.props.loading && <div className="loader" />}
        {this.props.error && !this.props.loading && <p>no campaigns found</p>}
        {this.props.campaignRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
