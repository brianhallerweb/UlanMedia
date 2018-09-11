//@format
import React, {Component} from 'react';
import CampaignByDay from './CampaignByDay';

class CampaignByDays extends Component {
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
        name: this.props.match.params.name,
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
        <h3>{this.props.match.params.name}</h3>
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
              <CampaignByDay key={dayRecord.day} dayRecord={dayRecord} />
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}

export default CampaignByDays;
