//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {clicked: false};
  }

  componentDidMount() {
    if (this.props.widgetRecord.status === 'excluded') {
      this.setState({clicked: true});
    }
  }

  stylizeClassification(row) {
    if ((row === 'bad') | (row === 'half bad')) {
      return <td style={{color: 'red', fontWeight: 900}}>{row}</td>;
    } else if ((row === 'good') | (row === 'half good')) {
      return <td style={{color: 'green', fontWeight: 900}}>{row}</td>;
    } else {
      return <td>{row}</td>;
    }
  }

  addRowLinks() {
    return (
      <div>
        <div className="rowLink">
          <Link
            to={{
              pathname: `/campaignsforonepwidget/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}`,
            }}
            target="_blank">
            campaigns
          </Link>
        </div>

        <div className="rowLink">
          <Link
            to={{
              pathname: `/cwidgetsforonepwidget/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}`,
            }}
            target="_blank">
            c widgets
          </Link>
        </div>

        <div className="rowLink">
          <Link
            to={{
              pathname: `/excludecampaignforonepwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}/${this.props.widgetRecord.mgid_id}`,
            }}
            target="_blank">
            exclude
          </Link>
        </div>

        <div className="rowLink">
          <a
            href={`https://dashboard.mgid.com/advertisers/campaign-quality-analysis/id/${
              this.props.widgetRecord.mgid_id
            }?search=${this.props.widgetRecord.widget_id.match(/^\d*/)}`}
            target="_blank">
            mgid
          </a>
        </div>
      </div>
    );
  }

  render() {
    return (
      <tr
        style={
          this.props.widgetRecord.is_bad_and_included
            ? {backgroundColor: '#f7d9d9'}
            : null
        }
        className={this.state.clicked && 'clicked'}
        onClick={e => {
          this.setState({clicked: !this.state.clicked});
        }}>
        <td>
          {this.props.widgetRecord.widget_id}
          {this.props.widgetRecord.widget_id !== 'summary' &&
            this.addRowLinks()}
        </td>

        {this.stylizeClassification(this.props.widgetRecord.classification)}

        <td>${this.props.widgetRecord.cost}</td>
        <td>${this.props.widgetRecord.revenue}</td>
        <td>${this.props.widgetRecord.profit}</td>
        <td>{this.props.widgetRecord.clicks}</td>
        <td>${this.props.widgetRecord.cpc}</td>
        <td>${this.props.widgetRecord.epc}</td>
        <td>${this.props.widgetRecord.mpc}</td>
        <td>{this.props.widgetRecord.leads}</td>
        <td>${this.props.widgetRecord.cpl}</td>
        <td>${this.props.widgetRecord.epl}</td>
        <td>${this.props.widgetRecord.mpl}</td>
        <td>{this.props.widgetRecord.sales}</td>
        <td>${this.props.widgetRecord.cps}</td>
        <td>${this.props.widgetRecord.eps}</td>
        <td>${this.props.widgetRecord.mps}</td>
        <td>{this.props.widgetRecord.status}</td>
        <td>{this.props.widgetRecord.global_status}</td>
      </tr>
    );
  }
}

export default Record;
