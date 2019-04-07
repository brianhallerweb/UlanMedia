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
            <th>Country</th>
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
            <th>ROI</th>
          </tr>
        </thead>
        <tbody>
          {this.props.countriesRecords.map(countriesRecord => (
            <Record
              key={countriesRecord.country_name}
              country={countriesRecord}
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
        {this.props.countriesRecords.length > 0 &&
          !this.props.loading &&
          this.createTable()}
      </div>
    );
  }
}

export default Records;
