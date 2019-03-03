//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';
import checkForBadAndIncludedCampaigns from './checkForBadAndIncludedCampaigns';

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
      cWidgetClassification: '',
      goodCampaignsCount: '',
      badCampaignsCount: '',
      waitCampaignsCount: '',
      badAndIncludedCampaignsCount: 0,
      c1: false,
      c1Value: 'all',
      c2: false,
      c2Value: 10,
      c3: false,
      c3Value: 10,
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

  submitForm() {
    this.setState({loading: true, mgidRequestDates: '', volRequestDates: ''});

    fetch(`/api/createCampaignsForOneCWidgetDataset`, {
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
      .then(res => res.json())
      .then(file => {
        this.setState({
          volRequestDates: `${file.metadata.vol_start_date} to ${
            file.metadata.vol_end_date
          }`,
          mgidRequestDates: `${file.metadata.mgid_start_date} to ${
            file.metadata.mgid_end_date
          }`,
          cWidgetClassification: file.metadata.c_widget_classification,
          goodCampaignsCount: file.metadata.good_campaigns_count,
          badCampaignsCount: file.metadata.bad_campaigns_count,
          waitCampaignsCount: file.metadata.wait_campaigns_count,
        });
      })
      .then(() =>
        fetch(`/api/createCampaignsForOneCWidgetReport`, {
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
            c1: this.state.c1,
            c2: this.state.c2,
            c3: this.state.c3,
          }),
        }),
      )
      .then(res => res.json())
      .then(records => {
        if (records.length) {
          records[0][
            'classification'
          ] = this.state.cWidgetClassification.toUpperCase();
        }
        let badAndIncludedCampaignsCount = checkForBadAndIncludedCampaigns(
          records,
        );

        let error;
        records.length ? (error = false) : (error = true);
        this.setState({
          campaignRecords: records,
          badAndIncludedCampaignsCount,
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
          loading={this.state.loading}
          submitForm={this.submitForm.bind(this)}
        />
        {this.state.requestDates && <p>{this.state.requestDates}</p>}
        {this.state.cWidgetClassification && (
          <div>
            <div>
              c widget is good in {this.state.goodCampaignsCount} campaigns
            </div>
            <div>
              c widget is bad in {this.state.badCampaignsCount} campaigns
            </div>
            <div>
              c widget is wait in {this.state.waitCampaignsCount} campaigns
            </div>
            <div>
              c widget is {this.state.cWidgetClassification.toUpperCase()}{' '}
              overall
            </div>
          </div>
        )}
        {this.state.badAndIncludedCampaignsCount !== 0 && (
          <div style={{color: 'red'}}>
            {this.state.badAndIncludedCampaignsCount} campaigns need to be
            excluded from the c widget
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
