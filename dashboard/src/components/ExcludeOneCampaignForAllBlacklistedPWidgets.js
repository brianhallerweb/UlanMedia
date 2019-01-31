//@format
import React, {Component} from 'react';
import Logout from './Logout';
import {Redirect} from 'react-router-dom';

class ExcludeOneCampaignForAllBlacklistedPWidgets extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      blacklistedPWidgets: [],
      mgidID: this.props.match.params.mgidID,
      campaignName: '',
    };
  }

  componentDidMount() {
    this.findCampaignName();
    this.getBlacklistedPWidgets();
  }

  findCampaignName() {
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
      .then(campaigns => {
        for (let campaign of campaigns) {
          if (campaign.mgid_id === this.state.mgidID) {
            this.setState({campaignName: campaign.name});
          }
        }
      })
      .catch(err => console.log(err));
  }

  getBlacklistedPWidgets() {
    fetch('/api/readblacklist')
      .then(res => {
        if (!res.ok) {
          throw Error(res.statusText);
        }
        return res.json();
      })
      .then(blacklistedPWidgets => this.setState({blacklistedPWidgets}))
      .catch(err => console.log(err));
  }

  excludeOneCampaign(pWidgetID, mgidID) {
    return new Promise((resolve, reject) => {
      fetch(`/api/excludecampaign`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'x-auth': localStorage.getItem('token'),
        },
        body: JSON.stringify({
          pWidgetID,
          mgidID,
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

  async excludeCampaign() {
    for (let pWidgetID of this.state.blacklistedPWidgets) {
      const result = await this.excludeOneCampaign(
        pWidgetID,
        this.state.mgidID,
      );
      if (result.id === Number(this.state.mgidID)) {
        console.log(
          `campaign ${this.state.mgidID} excluded from p widget ${pWidgetID}`,
        );
      } else {
        console.log(
          `ERROR: campaign ${
            this.state.mgidID
          } failed to be excluded from p widget ${pWidgetID}. The next line will show the error`,
        );
        console.log(result);
      }
    }
    console.log('END OF EXCLUDE SCRIPT');
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <p>
          Are you sure you want to exclude campaign {this.state.campaignName}{' '}
          from all blacklisted p widgets?
        </p>
        <div>
          <button
            disabled={!this.state.blacklistedPWidgets.length > 0}
            onClick={() => this.excludeCampaign()}>
            Yes, confirm exclutions
          </button>
        </div>
        <div>
          <p>Look in browser console for feedback</p>
        </div>
      </div>
    );
  }
}

export default ExcludeOneCampaignForAllBlacklistedPWidgets;
