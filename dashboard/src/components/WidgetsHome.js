//@format
import React, {Component} from 'react';
import WidgetsTitle from './WidgetsTitle';
import WidgetsNavBar from './WidgetsNavBar';
import WidgetsRecords from './WidgetsRecords';

class WidgetsHome extends Component {
  constructor(props) {
    super(props);
    this.state = {
      widgetType: this.props.match.params.widgetType,
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
    fetch(`/records/${this.state.widgetType}/createByWidgetsDataset`, {
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
        fetch(
          `/records/By${this.state.widgetType.charAt(0).toUpperCase() +
            this.state.widgetType.slice(1)}Widgets`,
          {
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
          },
        ),
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
        <WidgetsTitle ID={this.props.match.params.widgetID} />
        <WidgetsNavBar
          selectDateRange={this.selectDateRange.bind(this)}
          selectPrecondition={this.selectPrecondition.bind(this)}
          toggleCondition={this.toggleCondition.bind(this)}
          precondition={this.state.precondition}
          c1={this.state.c1}
          c2={this.state.c2}
          submitForm={this.submitForm.bind(this)}
        />
        <WidgetsRecords
          error={this.state.error}
          widgetRecords={this.state.widgetRecords}
        />
      </div>
    );
  }
}

export default WidgetsHome;
