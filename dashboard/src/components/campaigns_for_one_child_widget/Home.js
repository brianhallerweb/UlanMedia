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
      widgetID: this.props.match.params.widgetID,
      widgetRecords: [],
      dateRange: 'ninety',
      precondition: 0,
      precondition2: 'all',
      error: false,
      authenticated: true,
      loading: false,
      c1: false,
      c2: false,
    };
  }

  selectDateRange(dateRange) {
    this.setState({dateRange: dateRange});
  }

  toggleCondition(condition) {
    this.setState({[condition]: !this.state[condition]});
  }

  selectPrecondition(num) {
    this.setState({precondition: num});
  }

  selectPrecondition2(toInclude) {
    this.setState({precondition2: toInclude});
  }

  submitForm() {
    this.setState({loading: true});

    fetch(`/records/createCampaignsForOneChildWidgetDataset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        widgetID: this.state.widgetID,
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
      .then(() =>
        fetch(`/records/campaignsForOneChildWidget`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            dateRange: this.state.dateRange,
            widgetID: this.state.widgetID,
            precondition: this.state.precondition,
            precondition2: this.state.precondition2,
            c1: this.state.c1,
            c2: this.state.c2,
          }),
        }),
      )
      .then(res => res.json())
      .then(records => {
        let error;
        records.length ? (error = false) : (error = true);
        this.setState({widgetRecords: records, error, loading: false});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <Title ID={this.props.match.params.widgetID} />
        <GlobalNavBar />
        <NavBar
          dateRange={this.state.dateRange}
          selectDateRange={this.selectDateRange.bind(this)}
          selectPrecondition={this.selectPrecondition.bind(this)}
          selectPrecondition2={this.selectPrecondition2.bind(this)}
          toggleCondition={this.toggleCondition.bind(this)}
          precondition={this.state.precondition}
          precondition2={this.state.precondition2}
          c1={this.state.c1}
          c2={this.state.c2}
          loading={this.state.loading}
          submitForm={this.submitForm.bind(this)}
        />
        <p>
          (this report may take up to 30 sec because it has to generate the data
          before displaying the report)
        </p>
        <Records
          error={this.state.error}
          loading={this.state.loading}
          widgetRecords={this.state.widgetRecords}
        />
      </div>
    );
  }
}

export default Home;
