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
            <th className="ttc1">
              c1
              <span className="tttextc1">{'c1 = profit < maxSaleCpa'}</span>
            </th>
            <th className="ttc2">
              c2
              <span className="tttextc2">
                {'c2 = clicks > 1000 AND leads = 0'}
              </span>
            </th>
            <th className="ttc3">
              c3
              <span className="tttextc3">
                {'c3 = cost > 0.3*maxSaleCPA AND leadCPA > 2*maxLeadCPA'}
              </span>
            </th>
            <th className="ttc4">
              c4
              <span className="tttextc4">
                {'c4 = cost > 0.5*maxSaleCPA AND leadCPA > 1.5*maxLeadCPA'}
              </span>
            </th>
            <th className="ttc5">
              c5
              <span className="tttextc5">
                {'c5 = cost > 2*maxSaleCPA AND leadCPA > maxLeadCPA'}
              </span>
            </th>
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
