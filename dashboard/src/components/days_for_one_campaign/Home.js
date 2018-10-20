//@format
import React, {Component} from 'react';
import Title from './Title';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      campaignID: this.props.match.params.widgetID,
      dayRecords: [],
      loading: false,
    };
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
      <div>
        <Title dayRecords={this.state.dayRecords} />
        <GlobalNavBar />
        <Records
          loading={this.state.loading}
          dayRecords={this.state.dayRecords}
        />
      </div>
    );
  }
}

export default Home;
