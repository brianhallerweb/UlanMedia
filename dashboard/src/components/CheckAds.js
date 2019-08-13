//@format
import React, {Component} from 'react';
import Logout from './Logout';
import {Redirect} from 'react-router-dom';

class CheckAds extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      loading: false,
    };
  }

  checkAds() {
    this.setState({loading: true});

    fetch(`/jsonapi/checkads`, {
      method: 'POST',
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
        return res;
      })
      .then(res => res.json())
      .then(file => {
        console.log('Check ads script complete. Check your email');
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
        <p>Are you sure you want to check ads? (feedback in console)</p>
        <div>
          <button
            onClick={() => {
              this.checkAds();
            }}>
            Yes
          </button>
        </div>
        {this.state.loading && <div className="loader" />}
      </div>
    );
  }
}

export default CheckAds;
