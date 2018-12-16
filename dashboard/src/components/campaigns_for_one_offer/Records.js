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
            <th>Conversions</th>
            <th>CVR</th>
            <th>EPC</th>
            <th>CPA</th>
          </tr>
        </thead>
        <tbody>
          {this.props.campaignRecords.map(campaignRecord => (
            <Record key={campaignRecord.campaignID} campaign={campaignRecord} />
          ))}
        </tbody>
      </table>
    );
  }

  render() {
    return (
      <div>
        {this.props.loading && <div className="loader" />}
        {this.props.error && !this.props.loading && <p>no ads found</p>}
        {this.props.campaignRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
