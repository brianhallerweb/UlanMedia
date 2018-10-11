//@format
import React, {Component} from 'react';
import CampaignByWidgetsTitle from './CampaignByWidgetsTitle';
import CampaignByWidgetsNavBar from './CampaignByWidgetsNavBar';
import CampaignByWidgetsRecords from './CampaignByWidgetsRecords';

class CampaignByWidgetsHome extends Component {
  constructor(props) {
    super(props);
    this.state = {
      volid: this.props.match.params.volid,
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
    fetch('/records/byCampaignByWidgets', {
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
        this.setState({widgetRecords: records, error});
      })
      .catch(err => console.log(err));
  }

  render() {
    return (
      <div>
        <CampaignByWidgetsTitle name={this.props.match.params.name} />
        <CampaignByWidgetsNavBar
          datasetsCreated={this.state.datasetsCreated}
          selectDateRange={this.selectDateRange.bind(this)}
          selectPrecondition={this.selectPrecondition.bind(this)}
          toggleCondition={this.toggleCondition.bind(this)}
          precondition={this.state.precondition}
          c1={this.state.c1}
          c2={this.state.c2}
          submitForm={this.submitForm.bind(this)}
        />
        <CampaignByWidgetsRecords
          error={this.state.error}
          widgetRecords={this.state.widgetRecords}
        />
      </div>
    );
  }
}

export default CampaignByWidgetsHome;
