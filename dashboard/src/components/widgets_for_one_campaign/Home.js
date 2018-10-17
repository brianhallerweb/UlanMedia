//@format
import React, {Component} from 'react';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';
import GlobalNavBar from '../GlobalNavBar';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      volid: this.props.match.params.volid,
      widgetRecords: [],
      dateRange: 'seven',
      precondition: 2,
      error: false,
      loading: false,
      c1: false,
      c2: false,
    };
  }

  selectDateRange(dateRange) {
    this.setState({dateRange: dateRange});
  }

  toggleCondition(condition) {
    this.setState({[condition]: !this.state[condition]});
  }

  selectPrecondition(num) {
    this.setState({precondition: num});
  }

  submitForm() {
    this.setState({loading: true});

    fetch('/records/widgetsForOneCampaign', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        dateRange: this.state.dateRange,
        volid: this.state.volid,
        precondition: this.state.precondition,
        c1: this.state.c1,
        c2: this.state.c2,
      }),
    })
      .then(res => res.json())
      .then(records => {
        let error;
        records.length ? (error = false) : (error = true);
        this.setState({widgetRecords: records, error, loading: false});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        <Title name={this.props.match.params.name} />
        <GlobalNavBar />
        <NavBar
          datasetsCreated={this.state.datasetsCreated}
          selectDateRange={this.selectDateRange.bind(this)}
          selectPrecondition={this.selectPrecondition.bind(this)}
          toggleCondition={this.toggleCondition.bind(this)}
          precondition={this.state.precondition}
          c1={this.state.c1}
          c2={this.state.c2}
          submitForm={this.submitForm.bind(this)}
        />
        <Records
          loading={this.state.loading}
          error={this.state.error}
          widgetRecords={this.state.widgetRecords}
        />
      </div>
    );
  }
}

export default Home;
