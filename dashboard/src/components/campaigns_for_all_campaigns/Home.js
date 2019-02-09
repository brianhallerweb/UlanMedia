//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dateRange: 'thirty',
      volRequestDates: '',
      mgidRequestDates: '',
      c1: false,
      c2: false,
      c3: false,
      error: false,
      authenticated: true,
      loading: false,
      campaignsRecords: [],
    };
  }

  componentDidMount() {
    this.submitForm();
  }

  selectDateRange(dateRange) {
    let precondition;
    if (dateRange === 'yesterday' || dateRange === 'seven') {
      precondition = 0.25;
    } else if (dateRange === 'thirty') {
      precondition = 0.5;
    } else if (dateRange === 'ninety') {
      precondition = 1;
    } else if (dateRange === 'oneeighty') {
      precondition = 2;
    }

    this.setState({dateRange: dateRange, precondition: precondition});
  }

  toggleCondition(condition) {
    this.setState({[condition]: !this.state[condition]});
  }

  submitForm() {
    this.setState({loading: true, mgidRequestDates: '', volRequestDates: ''});

    fetch('/api/createCampaignsForAllCampaignsReport', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
        c1: this.state.c1,
        c2: this.state.c2,
        c3: this.state.c3,
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
      .then(records => {
        let error;
        records.length ? (error = false) : (error = true);
        this.setState({
          campaignsRecords: records,
          error,
          loading: false,
          volRequestDates: `${records[0]['vol_start_date']} to ${
            records[0]['vol_end_date']
          }`,
          mgidRequestDates: `${records[0]['mgid_start_date']} to ${
            records[0]['mgid_end_date']
          }`,
        });
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <Title
          volRequestDates={this.state.volRequestDates}
          mgidRequestDates={this.state.mgidRequestDates}
        />
        <GlobalNavBar />
        <div style={{marginBottom: 10}}>
          <a
            style={{fontSize: 12}}
            href="https://github.com/brianhallerweb/UlanMedia/raw/master/full_dashboard_map.jpg"
            target="_blank">
            flowchart
          </a>
        </div>
        <NavBar
          selectDateRange={this.selectDateRange.bind(this)}
          dateRange={this.state.dateRange}
          toggleCondition={this.toggleCondition.bind(this)}
          c1={this.state.c1}
          c2={this.state.c2}
          c3={this.state.c3}
          submitForm={this.submitForm.bind(this)}
          loading={this.state.loading}
        />
        <Records
          error={this.state.error}
          loading={this.state.loading}
          campaignsRecords={this.state.campaignsRecords}
        />
      </div>
    );
  }
}

export default Home;
