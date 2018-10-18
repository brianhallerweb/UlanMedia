//@format
import React, {Component} from 'react';
import Record from './Record';

class Records extends Component {
  constructor(props) {
    super(props);
    this.state = {dayRecords: [], loading: false};
  }

  componentDidMount() {
    this.setState({loading: true});
    fetch('/records/daysForOneCampaign', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        volid: this.props.match.params.volid,
      }),
    })
      .then(res => {
        if (!res.ok) {
          throw Error(res.statusText);
        }
        return res;
      })
      .then(res => res.json())
      .then(dayRecords => {
        this.setState({dayRecords, loading: false});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div className={this.state.loading && 'loading'}>
        <h3>
          {this.state.dayRecords.length > 0 && this.state.dayRecords[0].name}
        </h3>
        {this.state.loading && <div className="loader" />}
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
            {this.state.dayRecords.map(dayRecord => (
              <Record key={dayRecord.day} dayRecord={dayRecord} />
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default Records;
