//@format
import React, {Component} from 'react';

class CampaignByDay extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <tr>
        <td>{this.props.dayRecord.day}</td>
        <td>{this.props.dayRecord.clicks}</td>
        <td>${this.props.dayRecord.cost}</td>
        <td>${this.props.dayRecord.cpc}</td>
        <td>${this.props.dayRecord.revenue}</td>
        <td>{this.props.dayRecord.conversions}</td>
        <td>${this.props.dayRecord.conversion_cpa}</td>
      </tr>
    );
  }
}

export default CampaignByDay;
