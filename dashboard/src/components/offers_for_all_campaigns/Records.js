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
            <th>Offer Name</th>
            <th>Offer Flow</th>
            <th>Cost</th>
            <th>Revenue</th>
            <th>Profit</th>
            <th>Clicks</th>
            <th>CPC</th>
            <th>EPC</th>
            <th>Conversions</th>
            <th>CPA</th>
            <th>EPA</th>
            <th>CVR</th>
          </tr>
        </thead>
        <tbody>
          {this.props.offersRecords.map(offerRecord => (
            <Record key={offerRecord.offerID} offer={offerRecord} />
          ))}
        </tbody>
      </table>
    );
  }

  render() {
    return (
      <div>
        {this.props.loading && <div className="loader" />}
        {this.props.error && !this.props.loading && <p>no offers found</p>}
        {this.props.offersRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
