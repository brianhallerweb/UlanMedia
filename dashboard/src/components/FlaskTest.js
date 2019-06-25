//@format
import React, {Component} from 'react';
import {Redirect} from 'react-router-dom';

class FlaskTest extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dateRange: 'yesterday',
      c1: false,
      c1Value: 'wait',
      c2: true,
      c2Value: 20,
      c3: false,
      c3Value: 100,
      c4: false,
      c5: false,
      c6: false,
      c6Value: 30,
      c7: false,
      c7Value: 30,
      c8: false,
      c8Value: 30,
      c9: false,
      c9Value: 30,
      c10: false,
      c10Value: 30,
      c11: false,
      c11Value: 30,
      c12: false,
      c12Value: 30,
      c13: false,
      c13Value: 30,
      c14: false,
      c14Value: 0,
      c15: false,
      c15Value: 0,
      c16: true,
      c16Value: 0,
      c17: false,
      c17Value: 0,
      c18: false,
      c18Value: 0,
      c19: false,
      c19Value: 0,
      c20: false,
      c20Value: 0,
      c21: false,
      c21Value: 0,
      c22: false,
      c22Value: 30,
      c23: false,
      c23Value: 30,
      c24: false,
      c24Value: 30,
      c25: false,
      c25Value: 30,
      c26: false,
      c26Value: 30,
      c27: false,
      c27Value: 30,
    };
  }

  componentDidMount() {
    fetch('/jsonapi/test', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
        c1Value: this.state.c1Value,
        c2Value: this.state.c2Value,
        c3Value: this.state.c3Value,
        c6Value: this.state.c6Value,
        c7Value: this.state.c7Value,
        c8Value: this.state.c8Value,
        c9Value: this.state.c9Value,
        c10Value: this.state.c10Value,
        c11Value: this.state.c11Value,
        c12Value: this.state.c12Value,
        c13Value: this.state.c13Value,
        c14Value: this.state.c14Value,
        c15Value: this.state.c15Value,
        c16Value: this.state.c16Value,
        c17Value: this.state.c17Value,
        c18Value: this.state.c18Value,
        c19Value: this.state.c19Value,
        c20Value: this.state.c20Value,
        c21Value: this.state.c21Value,
        c22Value: this.state.c22Value,
        c23Value: this.state.c23Value,
        c24Value: this.state.c24Value,
        c25Value: this.state.c25Value,
        c26Value: this.state.c26Value,
        c27Value: this.state.c27Value,
        c1: this.state.c1,
        c2: this.state.c2,
        c3: this.state.c3,
        c4: this.state.c4,
        c5: this.state.c5,
        c6: this.state.c6,
        c7: this.state.c7,
        c8: this.state.c8,
        c9: this.state.c9,
        c10: this.state.c10,
        c11: this.state.c11,
        c12: this.state.c12,
        c13: this.state.c13,
        c14: this.state.c14,
        c15: this.state.c15,
        c16: this.state.c16,
        c17: this.state.c17,
        c18: this.state.c18,
        c19: this.state.c19,
        c20: this.state.c20,
        c21: this.state.c21,
        c22: this.state.c22,
        c23: this.state.c23,
        c24: this.state.c24,
        c25: this.state.c25,
        c26: this.state.c26,
        c27: this.state.c27,
      }),
    })
      .then(res => {
        return res.json();
      })
      .then(res => {
        console.log(res);
      })
      .catch(err => console.log(err));
  }

  render() {
    return <div>this is the flask test page. Look in the console</div>;
  }
}

export default FlaskTest;
