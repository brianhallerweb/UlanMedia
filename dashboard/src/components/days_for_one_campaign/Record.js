//@format
import React, {Component} from 'react';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <tr>
        <td>{this.props.dayRecord.day}</td>
        <td>{this.props.dayRecord.clicks}</td>
        <td>${this.props.dayRecord.cost.toFixed(2)}</td>
        <td>${this.props.dayRecord.cpc.toFixed(3)}</td>
        <td>${this.props.dayRecord.revenue}</td>
        <td>{this.props.dayRecord.conversions}</td>
        <td>${this.props.dayRecord.conversion_cpa.toFixed(2)}</td>
      </tr>
    );
  }
}

export default Record;
