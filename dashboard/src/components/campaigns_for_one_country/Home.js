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
      countryName: this.props.match.params.countryName,
      volRequestDates: '',
      c1: false,
      c1Value: 20,
      c2: false,
      c2Value: 50,
      error: false,
      authenticated: true,
      loading: false,
      countriesRecords: [],
    };
  }

  componentDidMount() {
    this.submitForm();
  }

  toggleCondition(condition) {
    this.setState({[condition]: !this.state[condition]});
  }

  setConditionValue(condition, conditionValue) {
    this.setState({[condition]: conditionValue});
  }

  submitForm() {
    this.setState({loading: true, volRequestDates: ''});

    fetch(`/api/createCampaignsForOneCountryDataset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({countryName: this.state.countryName}),
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
        fetch('/api/createCampaignsForOneCountryReport', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            countryName: this.state.countryName,
            c1Value: this.state.c1Value,
            c2Value: this.state.c2Value,
            c1: this.state.c1,
            c2: this.state.c2,
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
        this.setState({
          countriesRecords: records,
          error,
          loading: false,
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
          countryName={this.state.countryName}
        />
        <GlobalNavBar />
        <NavBar
          toggleCondition={this.toggleCondition.bind(this)}
          setConditionValue={this.setConditionValue.bind(this)}
          c1={this.state.c1}
          c1Value={this.state.c1Value}
          c2={this.state.c2}
          c2Value={this.state.c2Value}
          submitForm={this.submitForm.bind(this)}
          loading={this.state.loading}
        />
        <Records
          error={this.state.error}
          loading={this.state.loading}
          countriesRecords={this.state.countriesRecords}
        />
      </div>
    );
  }
}

export default Home;