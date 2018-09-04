//@format
import React, {Component} from 'react';
import CampaignRecord from './CampaignRecord';

class CampaignsRecords extends Component {
  constructor(props) {
    super(props);
    this.state = {
      error: false,
      campaignsRecords: [],
    };
  }

  getRecords() {
    const timePeriod = this.props.match.params.navitem
      .toLowerCase()
      .replace(/ /g, '');
    fetch(`/records/${timePeriod}`)
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

  componentDidMount() {
    this.getRecords();
  }

  componentDidUpdate(prevProps, prevState) {
    // runs when a new time period is chosen from
    // within a previous time period
    const prevTimePeriod = prevProps.match.params.navitem;
    const currentTimePeriod = this.props.match.params.navitem;
    if (prevTimePeriod !== currentTimePeriod) {
      return this.getRecords();
    }

    if (prevState.page !== this.state.page) {
      return this.getRecords();
    }
  }

  createTable() {
    return (
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Clicks</th>
            <th>Cost</th>
            <th>Revenue</th>
            <th>Profit</th>
            <th>Leads</th>
            <th>Lead_cpa</th>
            <th>Max_Lead_cpa</th>
            <th>Sales</th>
            <th>Sale_cpa</th>
            <th>Max_Sale_cpa</th>
            <th>epc</th>
            <th>c1</th>
            <th>c2</th>
            <th>c3</th>
            <th>c4</th>
            <th>c5</th>
          </tr>
        </thead>
        <tbody>
          {this.state.campaignsRecords.map(campaignRecord => (
            <CampaignRecord
              key={campaignRecord.name}
              campaign={campaignRecord}
            />
          ))}
        </tbody>
      </table>
    );
  }

  render() {
    return (
      <div>
        {this.state.error && <p>no campaigns found</p>}
        {this.state.campaignsRecords.length > 0 && this.createTable()}
      </div>
    );
  }
}

export default CampaignsRecords;
