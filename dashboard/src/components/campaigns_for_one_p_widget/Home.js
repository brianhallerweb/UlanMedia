//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';
import {Link} from 'react-router-dom';
import checkForBadAndIncludedCampaigns from './checkForBadAndIncludedCampaigns';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pWidgetID: this.props.match.params.pWidgetID,
      campaignRecords: [],
      dateRange: 'oneeighty',
      error: false,
      authenticated: true,
      loading: false,
      volRequestStartDate: '',
      volRequestEndDate: '',
      volRequestDates: '',
      mgidRequestDates: '',
      pWidgetClassification: '',
      pWidgetGlobalStatus: '',
      pWidgetHasMismatchClassificationAndGlobalStatus: '',
      goodCampaignsCount: '',
      badCampaignsCount: '',
      notYetCampaignsCount: '',
      badAndIncludedCampaignsCount: 0,
      c1: false,
      c1Value: 'not yet',
      c2: false,
      c2Value: 'all',
      c3: false,
      c3Value: 10,
      c4: false,
      c4Value: 10,
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
    this.setState({
      loading: true,
      classification: '',
      mgidRequestDates: '',
      volRequestDates: '',
    });

    fetch(`/api/createCampaignsForOnePWidgetDataset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
        pWidgetID: this.state.pWidgetID,
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
          volRequestStartDate: file.metadata.vol_start_date,
          volRequestEndDate: file.metadata.vol_end_date,
          volRequestDates: `${file.metadata.vol_start_date} to ${
            file.metadata.vol_end_date
          }`,
          mgidRequestDates: `${file.metadata.mgid_start_date} to ${
            file.metadata.mgid_end_date
          }`,
          pWidgetClassification: file.metadata.p_widget_classification,
          pWidgetGlobalStatus: file.metadata.p_widget_global_status,
          pWidgetHasMismatchClassificationAndGlobalStatus:
            file.metadata
              .p_widget_has_mismatch_classification_and_global_status,
          goodCampaignsCount: file.metadata.good_campaigns_count,
          badCampaignsCount: file.metadata.bad_campaigns_count,
          notYetCampaignsCount: file.metadata.not_yet_campaigns_count,
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
            pWidgetID: this.state.pWidgetID,
            c1Value: this.state.c1Value,
            c2Value: this.state.c2Value,
            c3Value: this.state.c3Value,
            c4Value: this.state.c4Value,
            c1: this.state.c1,
            c2: this.state.c2,
            c3: this.state.c3,
            c4: this.state.c4,
          }),
        }),
      )
      .then(res => res.json())
      .then(records => {
        //3/13 I removed this because I think it is cleaner
        //It gives the p widget classification in the summary row
        //if (records.length) {
        //records[0][
        //'classification'
        //] = this.state.pWidgetClassification.toUpperCase();
        //}
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
          ID={this.state.pWidgetID}
          mgidRequestDates={this.state.mgidRequestDates}
          volRequestDates={this.state.volRequestDates}
        />
        <GlobalNavBar />
        <div style={{marginBottom: 10}}>
          <a
            style={{fontSize: 12}}
            href="https://drive.google.com/file/d/1lTcfx6Vm72_NBLBkRFteKFbR9rxXhDbS/view?usp=sharing"
            target="_blank">
            flowchart
          </a>
        </div>
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
          loading={this.state.loading}
          submitForm={this.submitForm.bind(this)}
        />
        {this.state.requestDates && <p>{this.state.requestDates}</p>}
        {this.state.pWidgetClassification && (
          <div>
            <div>
              p widget is good in {this.state.goodCampaignsCount} campaigns
            </div>
            <div>
              p widget is bad in {this.state.badCampaignsCount} campaigns
            </div>
            <div>
              p widget is not yet in {this.state.notYetCampaignsCount} campaigns
            </div>
            <div>
              p widget classification is{' '}
              {this.state.pWidgetClassification === 'not yet' ? (
                'NOT YET'
              ) : (
                <Link
                  to={{
                    pathname: `/listpwidgetconfirmation/${
                      this.state.pWidgetID
                    }/${this.state.pWidgetClassification}`,
                  }}>
                  {this.state.pWidgetClassification.toUpperCase()}
                </Link>
              )}
            </div>
            <div>
              p widget global status is {this.state.pWidgetGlobalStatus}
            </div>
          </div>
        )}
        {this.state.pWidgetHasMismatchClassificationAndGlobalStatus &&
          !this.state.loading && (
            <div style={{color: 'red', marginTop: 10}}>
              p widget has a mismatched classfication and global status
            </div>
          )}
        {this.state.badAndIncludedCampaignsCount !== 0 &&
          !this.state.loading && (
            <div style={{color: 'red', marginTop: 10}}>
              {this.state.badAndIncludedCampaignsCount} campaigns need to be
              excluded from the p widget
            </div>
          )}
        <Records
          error={this.state.error}
          loading={this.state.loading}
          campaignRecords={this.state.campaignRecords}
          volRequestStartDate={this.state.volRequestStartDate}
          volRequestEndDate={this.state.volRequestEndDate}
        />
      </div>
    );
  }
}

export default Home;
