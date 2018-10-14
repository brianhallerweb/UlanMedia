//@format
import React, {Component} from 'react';
import Title from './Title';
import NavBar from './NavBar';
import Records from './Records';

class Home extends Component {
  constructor(props) {
    super(props);
    this.state = {
      widgetID: this.props.match.params.widgetID,
      widgetRecords: [],
      dateRange: 'seven',
      precondition: 5,
      error: false,
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
    fetch(`/records/createCampaignsForOneParentWidgetDataset`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        widgetID: this.state.widgetID,
        dateRange: this.state.dateRange,
      }),
    })
      .then(res => {
        if (!res.ok) {
          throw Error(res.statusText);
        }
        return res;
      })
      .then(() =>
        fetch(`/records/campaignsForOneParentWidget`, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            dateRange: this.state.dateRange,
            widgetID: this.state.widgetID,
            precondition: this.state.precondition,
            c1: this.state.c1,
            c2: this.state.c2,
          }),
        }),
      )
      .then(res => res.json())
      .then(records => {
        let error;
        records.length ? (error = false) : (error = true);
        this.setState({widgetRecords: records, error});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        <Title ID={this.props.match.params.widgetID} />
        <NavBar
          selectDateRange={this.selectDateRange.bind(this)}
          selectPrecondition={this.selectPrecondition.bind(this)}
          toggleCondition={this.toggleCondition.bind(this)}
          precondition={this.state.precondition}
          c1={this.state.c1}
          c2={this.state.c2}
          submitForm={this.submitForm.bind(this)}
        />
        <Records
          error={this.state.error}
          widgetRecords={this.state.widgetRecords}
        />
      </div>
    );
  }
}

export default Home;
