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
      c1: true,
      c2: true,
      c3: true,
      c4: true,
      error: false,
      campaignsRecords: [],
    };
  }

  selectDateRange(dateRange) {
    this.setState({dateRange: dateRange});
  }

  toggleCondition(condition) {
    this.setState({[condition]: !this.state[condition]});
  }

  submitForm() {
    fetch('/records/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
        c1: this.state.c1,
        c2: this.state.c2,
        c3: this.state.c3,
        c4: this.state.c4,
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

  isConditionSelected() {
    if (this.state.c1 || this.state.c2 || this.state.c3 || this.state.c4) {
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
          toggleCondition={this.toggleCondition.bind(this)}
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
