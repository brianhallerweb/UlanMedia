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
      dateRange: 'oneeighty',
      volRequestStartDate: '',
      volRequestEndDate: '',
      volRequestDates: '',
      mgidRequestDates: '',
      c1: false,
      c1Value: 10,
      c2: false,
      c2Value: 100,
      c3: false,
      c4: false,
      c5: false,
      c6: false,
      c7: false,
      c8: false,
      c9: false,
      c9Value: 30,
      c10: false,
      c10Value: 30,
      c11: false,
      c11Value: 30,
      c12: false,
      c12Value: 30,
      c13: false,
      c13Value: 30,
      c14: false,
      c14Value: 30,
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

  setConditionValue(condition, conditionValue) {
    this.setState({[condition]: conditionValue});
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
        c1Value: this.state.c1Value,
        c2Value: this.state.c2Value,
        c9Value: this.state.c9Value,
        c10Value: this.state.c10Value,
        c11Value: this.state.c11Value,
        c12Value: this.state.c12Value,
        c13Value: this.state.c13Value,
        c14Value: this.state.c14Value,
        c1: this.state.c1,
        c2: this.state.c2,
        c3: this.state.c3,
        c4: this.state.c4,
        c5: this.state.c5,
        c6: this.state.c6,
        c7: this.state.c7,
        c8: this.state.c8,
        c9: this.state.c9,
        c10: this.state.c10,
        c11: this.state.c11,
        c12: this.state.c12,
        c13: this.state.c13,
        c14: this.state.c14,
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
        if (records.length) {
          this.setState({
            campaignsRecords: records,
            error: false,
            loading: false,
            volRequestStartDate: records[0]['vol_start_date'],
            volRequestEndDate: records[0]['vol_end_date'],
            volRequestDates: `${records[0]['vol_start_date']} to ${
              records[0]['vol_end_date']
            }`,
            mgidRequestDates: `${records[0]['mgid_start_date']} to ${
              records[0]['mgid_end_date']
            }`,
          });
        } else {
          this.setState({
            campaignsRecords: records,
            error: true,
            loading: false,
          });
        }
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
          setConditionValue={this.setConditionValue.bind(this)}
          c1={this.state.c1}
          c2={this.state.c2}
          c3={this.state.c3}
          c4={this.state.c4}
          c5={this.state.c5}
          c6={this.state.c6}
          c7={this.state.c7}
          c8={this.state.c8}
          c9={this.state.c9}
          c10={this.state.c10}
          c11={this.state.c11}
          c12={this.state.c12}
          c13={this.state.c13}
          c14={this.state.c14}
          c1Value={this.state.c1Value}
          c2Value={this.state.c2Value}
          c9Value={this.state.c9Value}
          c10Value={this.state.c10Value}
          c11Value={this.state.c11Value}
          c12Value={this.state.c12Value}
          c13Value={this.state.c13Value}
          c14Value={this.state.c14Value}
          submitForm={this.submitForm.bind(this)}
          loading={this.state.loading}
        />
        <Records
          error={this.state.error}
          loading={this.state.loading}
          campaignsRecords={this.state.campaignsRecords}
          volRequestStartDate={this.state.volRequestStartDate}
          volRequestEndDate={this.state.volRequestEndDate}
        />
      </div>
    );
  }
}

export default Home;
