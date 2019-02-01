//@format
import React, {Component} from 'react';
import Logout from './Logout';
import {Redirect} from 'react-router-dom';

class ExcludeOneCampaignForAllBlacklistedPWidgets extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      loading: false,
      blacklistedPWidgets: [],
      mgidCampaignID: '',
    };
  }

  componentDidMount() {
    this.getBlacklistedPWidgets();
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

  async excludeCampaign() {
    this.setState({loading: true});
    for (let pWidgetID of this.state.blacklistedPWidgets) {
      const result = await this.excludeOneCampaign(
        pWidgetID,
        this.state.mgidCampaignID,
      );
      if (!result.id) {
        if (result.errors[0] === '[ERROR_CAMPAIGN_DOES_NOT_EXIST]') {
          console.log(`campaign id error: ${result.errors[0]}`);
          break;
        }
      }
      if (result.id === Number(this.state.mgidCampaignID)) {
        console.log(
          `campaign ${
            this.state.mgidCampaignID
          } excluded from p widget ${pWidgetID}`,
        );
      } else {
        console.log(
          `ERROR: campaign ${
            this.state.mgidCampaignID
          } failed to be excluded from p widget ${pWidgetID}. The next line will show the error`,
        );
        console.log(result);
      }
    }
    this.setState({loading: false});
    console.log('END OF EXCLUDE SCRIPT');
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <h3>Exclude one campaign from all blacklisted p widgets</h3>
        <div>Enter mgid campain id to exclude:</div>
        <input
          style={{marginTop: 4, marginBottom: 6}}
          type="text"
          value={this.state.mgidCampaignID}
          onChange={e => this.setState({mgidCampaignID: e.target.value})}
        />
        <div>
          <button
            disabled={
              !this.state.blacklistedPWidgets.length > 0 ||
              !this.state.mgidCampaignID
            }
            onClick={() => this.excludeCampaign()}>
            confirm exclutions
          </button>
        </div>
        <div>
          <p style={{fontSize: 12}}>
            Look in browser console for feedback (ctrl+shift+j)
          </p>
        </div>
        {this.state.loading && <div className="loader" />}
      </div>
    );
  }
}

export default ExcludeOneCampaignForAllBlacklistedPWidgets;
