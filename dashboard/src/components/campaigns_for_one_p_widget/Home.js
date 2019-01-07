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
      campaignRecords: [],
      dateRange: 'oneeighty',
      volRequestDates: '',
      mgidRequestDates: '',
      error: false,
      authenticated: true,
      loading: false,
      c1: false,
      c1Value: 'all',
      c2: false,
      c2Value: 'not yet listed',
      c3: false,
      c3Value: 10,
      c4: false,
      c4Value: 10,
      c5: false,
      c5Value: 0.25,
      c6: false,
      c6Value1: 700,
      c6Value2: 30,
      needsReview: false,
      campaignsCount: 0,
      goodCampaignsCount: 0,
      badCampaignsCount: 0,
    };
  }

  componentDidMount() {
    this.submitForm();
  }

  selectDateRange(dateRange) {
    this.setState({dateRange: dateRange});
  }

  toggleCondition(condition) {
    this.setState({[condition]: !this.state[condition]});
  }

  setConditionValue(condition, conditionValue) {
    this.setState({[condition]: conditionValue});
  }

  isNeedsReview() {
    if (
      this.state.c1 ||
      this.state.c2 ||
      this.state.c3 ||
      this.state.c3 ||
      this.state.c4 ||
      this.state.c5 ||
      this.state.c6
    ) {
      return this.setState({needsReview: false});
    }

    let campaignsCount = 0;
    let goodCampaignsCount = 0;
    let badCampaignsCount = 0;
    for (let campaign of this.state.campaignRecords) {
      if (campaign.name !== 'summary') {
        campaignsCount += 1;
      }

      if (
        campaign.name !== 'summary' &&
        campaign.lead_cvr < 0.25 &&
        (campaign.cost >= 30 || campaign.clicks >= 700)
      ) {
        badCampaignsCount += 1;
      }

      if (
        campaign.name !== 'summary' &&
        campaign.lead_cvr > 0.25 &&
        (campaign.leads >= 3 || campaign.sales >= 1)
      ) {
        goodCampaignsCount += 1;
      }
    }

    if (
      (goodCampaignsCount >= 3 && badCampaignsCount === 0) ||
      (goodCampaignsCount > 0 && badCampaignsCount > 0) ||
      (goodCampaignsCount === 0 && badCampaignsCount >= 3) ||
      (badCampaignsCount >= 1 && goodCampaignsCount === 0)
    ) {
      this.setState({
        campaignsCount,
        goodCampaignsCount,
        badCampaignsCount,
        needsReview: true,
      });
    }
  }

  submitForm() {
    this.setState({loading: true, mgidRequestDates: '', volRequestDates: ''});

    fetch(`/api/createCampaignsForOnePWidgetDataset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
        widgetID: this.state.widgetID,
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
          mgidRequestDates: `${file.metadata.mgid_start_date} to ${
            file.metadata.mgid_end_date
          }`,
        });
      })
      .then(() =>
        fetch(`/api/createCampaignsForOnePWidgetReport`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            dateRange: this.state.dateRange,
            widgetID: this.state.widgetID,
            c1Value: this.state.c1Value,
            c2Value: this.state.c2Value,
            c3Value: this.state.c3Value,
            c4Value: this.state.c4Value,
            c5Value: this.state.c5Value,
            c6Value1: this.state.c6Value1,
            c6Value2: this.state.c6Value2,
            c1: this.state.c1,
            c2: this.state.c2,
            c3: this.state.c3,
            c4: this.state.c4,
            c5: this.state.c5,
            c6: this.state.c6,
          }),
        }),
      )
      .then(res => res.json())
      .then(records => {
        let error;
        records.length ? (error = false) : (error = true);
        this.setState({campaignRecords: records, error, loading: false});
      })
      .then(() => this.isNeedsReview())
      .catch(err => console.log(err));
  }

  render() {
    console.log(this.state.needsReview);
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <Title
          ID={this.props.match.params.widgetID}
          mgidRequestDates={this.state.mgidRequestDates}
          volRequestDates={this.state.volRequestDates}
        />
        <GlobalNavBar />
        <NavBar
          dateRange={this.state.dateRange}
          selectDateRange={this.selectDateRange.bind(this)}
          toggleCondition={this.toggleCondition.bind(this)}
          setConditionValue={this.setConditionValue.bind(this)}
          c1={this.state.c1}
          c1Value={this.state.c1Value}
          c2={this.state.c2}
          c2Value={this.state.c2Value}
          c3={this.state.c3}
          c3Value={this.state.c3Value}
          c4={this.state.c4}
          c4Value={this.state.c4Value}
          c5={this.state.c5}
          c5Value={this.state.c5Value}
          c6={this.state.c6}
          c6Value1={this.state.c6Value1}
          c6Value2={this.state.c6Value2}
          loading={this.state.loading}
          submitForm={this.submitForm.bind(this)}
        />
        {this.state.requestDates && <p>{this.state.requestDates}</p>}
        {this.state.needsReview && (
          <div>
            <p>total campaigns: {this.state.campaignsCount}</p>
            <p>good campaigns: {this.state.goodCampaignsCount}</p>
            <p>bad campaigns: {this.state.badCampaignsCount}</p>
            <p style={{color: 'red'}}>NEEDS REVIEW</p>
          </div>
        )}
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
