//@format
import React, {Component} from 'react';
import Logout from './Logout';
import {Redirect} from 'react-router-dom';

class UpdateAllData extends Component {
  constructor(props) {
    super(props);
    this.state = {
      authenticated: true,
    };
  }

  render() {
    return (
      <div>
        {!this.state.authenticated && <Redirect to="/" />}
        <Logout />
        <p>Are you sure you want to update all data?</p>
        <div>
          <button>
            <a href="http://scripts.brianhaller.net">Yes</a>
          </button>
        </div>
      </div>
    );
  }
}

export default UpdateAllData;
