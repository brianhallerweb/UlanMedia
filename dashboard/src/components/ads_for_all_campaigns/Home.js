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
      dateRange: 'seven',
      precondition: 0,
      error: false,
      authenticated: true,
      loading: false,
      adsRecords: [],
    };
  }

  selectDateRange(dateRange) {
    this.setState({dateRange: dateRange, precondition: precondition});
  }

  selectPrecondition(num) {
    this.setState({precondition: num});
  }

  submitForm() {
    this.setState({loading: true});
    fetch('/records/adsForAllCampaigns', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
        precondition: this.state.precondition,
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
        this.setState({adsRecords: records, error, loading: false});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <Title />
        <GlobalNavBar />
        <NavBar
          selectDateRange={this.selectDateRange.bind(this)}
          selectPrecondition={this.selectPrecondition.bind(this)}
          precondition={this.state.precondition}
          c1={this.state.c1}
          submitForm={this.submitForm.bind(this)}
          loading={this.state.loading}
        />
        <Records
          error={this.state.error}
          loading={this.state.loading}
          adsRecords={this.state.adsRecords}
        />
      </div>
    );
  }
}

export default Home;
