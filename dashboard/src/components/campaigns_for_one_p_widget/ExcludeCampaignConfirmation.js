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
      successResponse: false,
      successMessage: '',
      errorResponse: false,
      errorMessage: '',
    };
  }

  confirmExcludeCampaign() {
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
        return res.json();
      })
      .then(res => {
        if (res.id === Number(this.state.mgidCampaignID)) {
          this.setState({
            successResponse: true,
            successMessage: `Campaign ${res.id} successfully excluded`,
          });
        } else {
          this.setState({
            errorResponse: true,
            errorMessage: `There was an error. Campaign ${
              this.state.mgidCampaignID
            } was not excluded.`,
          });
          throw Error(
            `There was an error. Campaign ${
              this.state.mgidCampaignID
            } was not excluded.`,
          );
        }
      })
      .catch(err => {
        console.log(err);
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
        {this.state.successResponse && (
          <div>
            <p style={{color: 'green'}}>{this.state.successMessage}</p>
            <div style={{marginTop: 10}}>
              <button onClick={() => close()}>close tab</button>
            </div>
          </div>
        )}
        {this.state.errorResponse && (
          <div>
            <p style={{color: 'red'}}>{this.state.errorMessage}</p>
            <div style={{marginTop: 10}}>
              <button onClick={() => close()}>close tab</button>
            </div>
          </div>
        )}
      </div>
    );
  }
}

export default ExcludeCampaignConfirmation;
