//@format
import React, {Component} from 'react';
import Record from './Record';

class Records extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div className={this.state.loading && 'loading'}>
        {this.props.loading && <div className="loader" />}
        <table>
          <thead>
            <tr>
              <th>Day</th>
              <th>Clicks</th>
              <th>Cost</th>
              <th>CPC</th>
              <th>Revenue</th>
              <th>Conversions</th>
              <th>Conversion CPA</th>
            </tr>
          </thead>
          <tbody>
            {this.props.dayRecords.map(dayRecord => (
              <Record key={dayRecord.day} dayRecord={dayRecord} />
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default Records;
