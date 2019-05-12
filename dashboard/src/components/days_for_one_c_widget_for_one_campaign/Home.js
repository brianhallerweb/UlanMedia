//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      cWidgetID: this.props.match.params.cWidgetID,
      volID: this.props.match.params.volID,
      name: this.props.match.params.name,
      volRequestDates: '',
      dayRecords: [],
      loading: false,
      authenticated: true,
    };
  }

  componentDidMount() {
    this.setState({loading: true});

    fetch('/api/createDaysForOneCWidgetForOneCampaignDataset', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        cWidgetID: this.state.cWidgetID,
        volID: this.state.volID,
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
        fetch('/api/createDaysForOneCWidgetForOneCampaignReport', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            cWidgetID: this.state.cWidgetID,
            volID: this.state.volID,
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
          dayRecords: records,
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
          cWidgetID={this.state.cWidgetID}
          name={this.state.name}
          volRequestDates={this.state.volRequestDates}
        />
        <GlobalNavBar />
        <div style={{marginBottom: 10}}>
          *Remember the Cost, Clicks, CPC, CPL, Lead CVR, CPS, and ROI are not
          highly accurate, they're just estimates based on Voluum's daily
          averaged CPC evenly distributed across received clicks....instead of
          being based on MGID's variable CPC actual charged clicks.
        </div>
        <Records
          loading={this.state.loading}
          dayRecords={this.state.dayRecords}
        />
      </div>
    );
  }
}

export default Home;
