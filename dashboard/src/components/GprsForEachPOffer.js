//@format
import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';

class GprsForEachPOffer extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      loading: false,
      dateRange: this.props.match.params.dateRange,
      gprs: [],
    };
  }

  componentDidMount() {
    this.setState({loading: true});

    fetch(`/api/createGprsForEachPOfferDataset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
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
          gprs: file,
          loading: false,
        });
      });
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <table style={{width: '50%'}}>
          <thead>
            <tr>
              <th>P Offer</th>
              <th>GPR</th>
              <th>Profit</th>
              <th>Rank</th>
            </tr>
          </thead>
          <tbody>
            {this.state.gprs.map(gpr => (
              <tr key={gpr.p_offer_name}>
                <td>{gpr.p_offer_name}</td>
                <td>{gpr.gpr}</td>
                <td>${gpr.p_offer_profit}</td>
                <td>{gpr.p_offer_profit_rank}</td>
              </tr>
            ))}
          </tbody>
        </table>
        {this.state.gprs[0] && (
          <div style={{marginTop: 20}}>
            Formula: {this.state.gprs[0].formula}
          </div>
        )}
      </div>
    );
  }
}

export default GprsForEachPOffer;
