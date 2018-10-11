//@format
import React, {Component} from 'react';
import CampaignByDayRecord from './CampaignByDayRecord';

class CampaignByDaysRecords extends Component {
  constructor(props) {
    super(props);
    this.state = {dayRecords: []};
  }

  componentDidMount() {
    fetch('/records/byday', {
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
        this.setState({dayRecords});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        <h3>
          {this.state.dayRecords.length > 0 && this.state.dayRecords[0].name}
        </h3>
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
              <CampaignByDayRecord key={dayRecord.day} dayRecord={dayRecord} />
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default CampaignByDaysRecords;
