//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import {Redirect} from 'react-router-dom';

class ExcludeCampaignConfirmation extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      pWidgetID: this.props.match.params.pWidgetID,
      mgidCampaignID: this.props.match.params.mgidCampaignID,
      loading: false,
      successResponse: false,
      successMessage1: '',
      successMessage2: '',
      errorResponse: false,
      errorMessage: '',
    };
  }

  confirmExcludeCampaign() {
    this.setState({loading: true});
    fetch(`/api/excludecampaign`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        pWidgetID: this.state.pWidgetID,
        mgidCampaignID: this.state.mgidCampaignID,
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
      .then(res => {
        if (res.id === Number(this.state.mgidCampaignID)) {
          console.log(`Campaign ${res.id} successfully excluded`);
        } else {
          throw Error(
            `There was an error. Campaign ${
              this.state.mgidCampaignID
            } was not excluded.`,
          );
        }
      })
      .then(() =>
        fetch(`/api/updateoneexcludedpwidgetslist`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'x-auth': localStorage.getItem('token'),
          },
          body: JSON.stringify({
            mgidCampaignID: this.state.mgidCampaignID,
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
      })
      .then(() => {
        console.log(
          `Campaign ${this.state.mgidCampaignID} status updated to "excluded"`,
        );
        this.setState({
          loading: false,
        });
      })
      .catch(err => {
        console.log(err);
        this.setState({
          loading: false,
        });
      });
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <p>
          Are you sure you want to exclude campaign {this.state.mgidCampaignID}{' '}
          from p widget {this.state.pWidgetID}?
        </p>
        <div>
          <button onClick={() => this.confirmExcludeCampaign()}>
            Yes, confirm exclution
          </button>
        </div>
        <p style={{fontSize: 12}}>
          Look in browser console for feedback (ctrl+shift+j)
        </p>
        {this.state.loading && <div className="loader" />}
      </div>
    );
  }
}

export default ExcludeCampaignConfirmation;
