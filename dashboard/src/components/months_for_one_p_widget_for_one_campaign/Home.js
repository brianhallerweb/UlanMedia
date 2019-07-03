//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import Title from './Title';
import Links from './Links';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';
import {Redirect} from 'react-router-dom';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      pWidgetID: this.props.match.params.pWidgetID,
      volID: this.props.match.params.volID,
      mgidID: this.props.match.params.volID,
      name: this.props.match.params.name,
      volRequestDates: '',
      monthRecords: [],
      loading: false,
      authenticated: true,
    };
  }

  componentDidMount() {
    this.setState({loading: true});

    fetch('/jsonapi/createMonthsForOnePWidgetForOneCampaignDataset', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        pWidgetID: this.state.pWidgetID,
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
        fetch('/jsonapi/createMonthsForOnePWidgetForOneCampaignReport', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            pWidgetID: this.state.pWidgetID,
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
          monthRecords: records,
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
          pWidgetID={this.state.pWidgetID}
          name={this.state.name}
          volRequestDates={this.state.volRequestDates}
        />
        <GlobalNavBar />
        <div style={{marginBottom: 10}}>
          *Remember the Cost, Clicks, Profit, CPC, CPL, Lead CVR, CPS, and ROI
          are not highly accurate, they're just estimates based on Voluum's
          daily averaged CPC evenly distributed across received
          clicks....instead of being based on MGID's variable CPC actual charged
          clicks.
        </div>
        <Links
          pWidgetID={this.state.pWidgetID}
          volID={this.state.volID}
          mgidID={this.state.mgidID}
          name={this.state.name}
        />
        <Records
          loading={this.state.loading}
          monthRecords={this.state.monthRecords}
        />
      </div>
    );
  }
}

export default Home;
