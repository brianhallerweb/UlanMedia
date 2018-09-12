//@format
import React, {Component} from 'react';
import Title from '../components/Title';
import NavBar from '../components/NavBar';
import CampaignsRecords from '../components/CampaignsRecords';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      dateRange: 'seven_by_campaigns_data',
      precondition: 0.25,
      c1: true,
      c2: true,
      c3: true,
      c4: true,
      c5: true,
      error: false,
      campaignsRecords: [],
    };
  }

  selectDateRange(dateRange) {
    let precondition;
    if (
      dateRange === 'yesterday_by_campaigns_data' ||
      dateRange === 'seven_by_campaigns_data'
    ) {
      precondition = 0.25;
    } else if (dateRange === 'thirty_by_campaigns_data') {
      precondition = 0.5;
    } else if (dateRange === 'ninety_by_campaigns_data') {
      precondition = 1;
    } else if (dateRange === 'oneeighty_by_campaigns_data') {
      precondition = 2;
    }

    this.setState({dateRange: dateRange, precondition: precondition});
  }

  toggleCondition(condition) {
    this.setState({[condition]: !this.state[condition]});
  }

  selectPrecondition(num) {
    this.setState({precondition: num});
  }

  submitForm() {
    fetch('/records/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
        precondition: this.state.precondition,
        c1: this.state.c1,
        c2: this.state.c2,
        c3: this.state.c3,
        c4: this.state.c4,
        c5: this.state.c5,
      }),
    })
      .then(res => {
        if (!res.ok) {
          throw Error(res.statusText);
        }
        return res;
      })
      .then(res => res.json())
      .then(records => {
        let error;
        records.length ? (error = false) : (error = true);
        this.setState({campaignsRecords: records, error});
      })
      .catch(err => console.log(err));
  }

  //true enables submit button
  //false disables submit button
  isConditionSelected() {
    if (
      this.state.c1 ||
      this.state.c2 ||
      this.state.c3 ||
      this.state.c4 ||
      this.state.c5
    ) {
      return true;
    } else {
      return false;
    }
  }

  render() {
    return (
      <div>
        <Title />
        <NavBar
          selectDateRange={this.selectDateRange.bind(this)}
          selectPrecondition={this.selectPrecondition.bind(this)}
          toggleCondition={this.toggleCondition.bind(this)}
          precondition={this.state.precondition}
          c1={this.state.c1}
          c2={this.state.c2}
          c3={this.state.c3}
          c4={this.state.c4}
          c5={this.state.c5}
          submitForm={this.submitForm.bind(this)}
          isConditionSelected={this.isConditionSelected.bind(this)}
        />
        <CampaignsRecords
          error={this.state.error}
          campaignsRecords={this.state.campaignsRecords}
        />
      </div>
    );
  }
}

export default Home;
