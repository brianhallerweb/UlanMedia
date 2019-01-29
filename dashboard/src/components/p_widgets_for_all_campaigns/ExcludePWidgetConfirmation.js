//@format
import React, {Component} from 'react';
import Logout from '../Logout';
import {Redirect} from 'react-router-dom';

class ExcludePWidgetConfirmation extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      campaigns: [],
      pWidgetID: this.props.match.params.pWidgetID,
      loading: false,
      showMessages: false,
      messages: [],
    };
  }

  componentDidMount() {
    this.getCampaigns();
  }

  getCampaigns() {
    fetch(`/api/getcampaignsets`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
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
      .then(campaigns => this.setState({campaigns}))
      .catch(err => console.log(err));
  }

  updateOneExcludedPWidgetsList(mgidCampaignID) {
    return new Promise((resolve, reject) => {
      fetch(`/api/updateoneexcludedpwidgetslist`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-auth': localStorage.getItem('token'),
        },
        body: JSON.stringify({
          mgidCampaignID,
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
          resolve(res);
        })
        .catch(err => reject(err));
    });
  }

  excludeOneCampaign(pWidgetID, mgidCampaignID) {
    return new Promise((resolve, reject) => {
      fetch(`/api/excludecampaign`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-auth': localStorage.getItem('token'),
        },
        body: JSON.stringify({
          pWidgetID,
          mgidCampaignID,
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
          resolve(res);
        })
        .catch(err => reject(err));
    });
  }

  //excludeAllCampaigns is the important function on this page. It is what
  //excludes each campaign from a p widget, one by one. All the other
  //code on this page either helps this function or it is just for
  //displaying feedback messages.
  async excludeAllCampaigns() {
    // This function is async because I wanted to slow down the requests
    // to mgid. It excludes each campaign, one at a time.
    this.setState({loading: true});
    for (let campaign of this.state.campaigns) {
      //exclude one campaign and then update the list of excluded p
      //widgets for that campaign
      const excluded = await this.excludeOneCampaign(
        this.state.pWidgetID,
        campaign.mgid_id,
      );
      const updated = await this.updateOneExcludedPWidgetsList(
        campaign.mgid_id,
      );

      this.setState({
        showMessages: true,
        messages: this.state.messages.concat(excluded),
      });
      this.setState({
        messages: this.state.messages.concat(updated),
      });
    }

    // This is just stuff for feedback messages on the web app.
    this.setState({loading: false, showMessages: false});
    if (this.state.errorCount > 0) {
      this.setState({
        finalResultMessage:
          'Failed, something went wrong. You need to investigate further because some campaigns were not excluded or some lists of excluded p widgets were not updated. Remember that some campaigns may have been successfully excluded.',
      });
    } else {
      this.setState({
        finalResultMessage:
          'Successfully excluded all campaigns and updated all excluded p widgets lists. The new "excluded" campaign status will be immediately reflected on the web app.',
      });
    }
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <p>
          Are you sure you want to exclude all campaigns from p widget{' '}
          {this.state.pWidgetID}?
        </p>
        <div>
          <button
            disabled={!this.state.campaigns.length > 0}
            onClick={() => this.excludeAllCampaigns()}>
            Yes, confirm exclution
          </button>
        </div>
        {this.state.loading && (
          <div style={{margin: 10}}>
            <div className="loader" />
            <div>This will take a 5-10 minutes...</div>
          </div>
        )}
        {this.state.showMessages && (
          <div>
            {this.state.messages.map(message => {
              if (typeof message === 'string') {
                return (
                  <p
                    key={message}
                    style={{color: 'green', margin: 0, fontSize: 14}}>
                    {message}
                  </p>
                );
              }
              if (message.id) {
                return (
                  <p
                    key={message.id}
                    style={{color: 'green', margin: 0, fontSize: 14}}>
                    campaign {message.id} successfully excluded
                  </p>
                );
              } else {
                this.setState({errorCount: this.state.errorCount + 1});
                return (
                  <li style={{color: 'red'}}>error excluding a campaign</li>
                );
              }
            })}
          </div>
        )}
        {this.state.messages.length === this.state.campaigns.length * 2 &&
          this.state.messages.length > 0 && (
            <div>
              <div style={{marginTop: 10, color: 'green'}}>
                {this.state.finalResultMessage}
              </div>
              <div style={{marginTop: 10}}>
                <button onClick={() => close()}>close tab</button>
              </div>
            </div>
          )}
      </div>
    );
  }
}

export default ExcludePWidgetConfirmation;
