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
            <th>Image</th>
            <th>Classification</th>
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
            <th>Local Rank</th>
            <th>Final Rank</th>
            <th>Global Rank</th>
          </tr>
        </thead>
        <tbody>
          {this.props.adsRecords.map(adRecord => (
            <Record key={adRecord.image} ad={adRecord} />
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
        {this.props.adsRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
