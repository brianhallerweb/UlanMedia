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
      offerID: this.props.match.params.offerID,
      dateRange: 'ninety',
      volRequestDates: '',
      error: false,
      authenticated: true,
      loading: false,
      campaignRecords: [],
    };
  }

  selectDateRange(dateRange) {
    this.setState({dateRange: dateRange});
  }

  submitForm() {
    this.setState({loading: true, volRequestDates: ''});

    fetch(`/api/createCampaignsForOneOfferDataset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        offerID: this.state.offerID,
        dateRange: this.state.dateRange,
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
      .then(file => {
        this.setState({
          volRequestDates: `${file.metadata.vol_start_date} to ${
            file.metadata.vol_end_date
          }`,
        });
      })
      .then(() =>
        fetch('/api/createCampaignsForOneOfferReport', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            dateRange: this.state.dateRange,
            offerID: this.state.offerID,
          }),
        }),
      )
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
        this.setState({campaignRecords: records, error, loading: false});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <Title
          offerID={this.state.offerID}
          volRequestDates={this.state.volRequestDates}
        />
        <GlobalNavBar />
        <NavBar
          dateRange={this.state.dateRange}
          selectDateRange={this.selectDateRange.bind(this)}
          submitForm={this.submitForm.bind(this)}
          loading={this.state.loading}
        />
        <Records
          error={this.state.error}
          loading={this.state.loading}
          campaignRecords={this.state.campaignRecords}
        />
      </div>
    );
  }
}

export default Home;