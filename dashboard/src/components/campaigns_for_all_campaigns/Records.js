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
            <th>Clicks</th>
            <th>Cost</th>
            <th>Revenue</th>
            <th>Profit</th>
            <th>Leads</th>
            <th>Lead CPA</th>
            <th>Max Lead CPA</th>
            <th>Lead CVR</th>
            <th>Sales</th>
            <th>Sale CPA</th>
            <th>Max Sale CPA</th>
            <th>EPC</th>
          </tr>
        </thead>
        <tbody>
          {this.props.campaignsRecords.map(campaignRecord => (
            <Record key={campaignRecord.name} campaign={campaignRecord} />
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
        {this.props.campaignsRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
