//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {clicked: false};
  }

  render() {
    return (
      <tr className={this.state.clicked && 'clicked'}>
        <td>
          {this.props.widgetRecord.widget_id}
          <div>
            <div className="rowLink">
              <Link
                to={{
                  pathname: `/campaignsforonecwidget/${
                    this.props.widgetRecord.widget_id
                  }`,
                }}
                target="_blank">
                campaigns
              </Link>
            </div>

            <div className="rowLink">
              <Link
                to={{
                  pathname: `/excludecwidgetconfirmation/${
                    this.props.widgetRecord.widget_id
                  }`,
                }}
                target="_blank">
                exclude
              </Link>
            </div>
          </div>
        </td>
        <td>{`${this.props.widgetRecord.classification} (${
          this.props.widgetRecord.good_campaigns_count
        }g/${this.props.widgetRecord.bad_campaigns_count}b/${
          this.props.widgetRecord.wait_campaigns_count
        }w)`}</td>
        <td>${this.props.widgetRecord.cost}</td>
        <td>${this.props.widgetRecord.revenue}</td>
        <td>${this.props.widgetRecord.profit}</td>
        <td>{this.props.widgetRecord.clicks}</td>
        <td>{this.props.widgetRecord.cpc}</td>
        <td>{this.props.widgetRecord.epc}</td>
        <td>{this.props.widgetRecord.leads}</td>
        <td>${this.props.widgetRecord.cpl}</td>
        <td>${this.props.widgetRecord.epl}</td>
        <td>{this.props.widgetRecord.lead_cvr}%</td>
        <td>{this.props.widgetRecord.sales}</td>
        <td>${this.props.widgetRecord.cps}</td>
        <td>${this.props.widgetRecord.eps}</td>
        <td>
          {this.props.widgetRecord.global_status}
          <div onClick={() => this.setState({clicked: true})}>
            <div className="rowLink">
              <Link
                to={{
                  pathname: `/listcwidgetconfirmation/${
                    this.props.widgetRecord.widget_id
                  }/white`,
                }}
                target="_blank">
                white
              </Link>
            </div>
            <div className="rowLink">
              <Link
                to={{
                  pathname: `/listcwidgetconfirmation/${
                    this.props.widgetRecord.widget_id
                  }/grey`,
                }}
                target="_blank">
                grey
              </Link>
            </div>
            <div className="rowLink">
              <Link
                to={{
                  pathname: `/listcwidgetconfirmation/${
                    this.props.widgetRecord.widget_id
                  }/black`,
                }}
                target="_blank">
                black
              </Link>
            </div>
            <div className="rowLink">
              <span className="fakeLink">wait</span>
            </div>
          </div>
        </td>
      </tr>
    );
  }
}

export default Record;