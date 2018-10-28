//@format
import React, {Component} from 'react';
import Logout from '../Logout';
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
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        volid: this.props.match.params.volid,
      }),
    })
      .then(res => {
        if (!res.ok) {
          if (res.status == 401) {
            //the case when a token is in the browser but it doesn't
            //match what it is in the database. This can happen when the
            //token is manipulated in the browser or if the tokens are
            //deleted from the database without the user logging out.
            localStorage.removeItem('token');
            this.setState({authenticated: false});
          }
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
        <Logout />
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
