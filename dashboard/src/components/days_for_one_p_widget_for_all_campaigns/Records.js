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
              <th>Cost</th>
              <th>Revenue</th>
              <th>Profit</th>
              <th>Clicks</th>
              <th>CPC</th>
              <th>EPC</th>
              <th>Leads</th>
              <th>CPL</th>
              <th>EPL</th>
              <th>Lead CVR</th>
              <th>Sales</th>
              <th>CPS</th>
              <th>EPS</th>
              <th>ROI</th>
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
