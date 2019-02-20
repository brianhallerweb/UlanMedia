//@format
import React, {Component} from 'react';
import Logout from './Logout';
import {Redirect} from 'react-router-dom';

class UpdateAllData extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
      loading: false,
    };
  }

  confirmUpdateAllData() {
    console.log('test function ran. I will add the real function soon.');
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <p>Are you sure you want to update all data?</p>
        <div>
          <button onClick={() => this.confirmUpdateAllData()}>Yes</button>
        </div>
        <p style={{fontSize: 12}}>
          This process will take about 30 minutes. Look in browser console for
          feedback (ctrl+shift+j)
        </p>
        {this.state.loading && <div className="loader" />}
      </div>
    );
  }
}

export default UpdateAllData;
