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
      <tr
        style={
          this.props.widgetRecord
            .has_mismatch_classification_and_global_status ||
          this.props.widgetRecord.has_bad_and_included_campaigns
            ? {backgroundColor: '#f7d9d9'}
            : null
        }
        className={this.state.clicked && 'clicked'}
        onClick={e => {
          this.setState({clicked: !this.state.clicked});
        }}>
        <td>
          {this.props.widgetRecord.widget_id}
          <div>
            <div className="rowLink">
              <Link
                onClick={e => e.stopPropagation()}
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
              <a
                href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_32154ab0-b614-4ac5-b017-6d5a18447bc5/report/month?dateRange=last-30-days&sortKey=month&sortDirection=desc&page=1&chart=0&columns=month&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=100&reportType=&include=ACTIVE&reportDataType=0&tagsGrouping=month&valueFiltersGrouping=month&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc&filter2=custom-variable-1&filter2Value=$
            {this.props.widgetRecord.widget_id}`}
                target="_blank">
                months
              </a>
            </div>
            <div className="rowLink">
              <a
                href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_32154ab0-b614-4ac5-b017-6d5a18447bc5/report/day?dateRange=last-30-days&sortKey=day&sortDirection=desc&page=1&chart=0&columns=day&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=&limit=100&reportType=&include=ACTIVE&reportDataType=0&tagsGrouping=day&valueFiltersGrouping=day&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc&filter2=custom-variable-1&filter2Value=${
                  this.props.widgetRecord.widget_id
                }`}
                target="_blank">
                days
              </a>
            </div>
            <div className="rowLink">
              <Link
                onClick={e => e.stopPropagation()}
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
        <td>
          {this.props.widgetRecord.classification !== 'not yet' ? (
            <div>
              <Link
                onClick={e => e.stopPropagation()}
                to={{
                  pathname: `/listcwidgetconfirmation/${
                    this.props.widgetRecord.widget_id
                  }/${this.props.widgetRecord.classification}`,
                }}
                target="_blank">
                {this.props.widgetRecord.classification}
              </Link>
              <div>
                {`(${this.props.widgetRecord.good_campaigns_count}g/${
                  this.props.widgetRecord.bad_campaigns_count
                }b/${this.props.widgetRecord.not_yet_campaigns_count}ny)`}
              </div>
            </div>
          ) : (
            <div>
              <div>not yet</div>
              <div>
                {`(${this.props.widgetRecord.good_campaigns_count}g/${
                  this.props.widgetRecord.bad_campaigns_count
                }b/${this.props.widgetRecord.not_yet_campaigns_count}ny)`}
              </div>
            </div>
          )}
        </td>
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
                onClick={e => e.stopPropagation()}
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
                onClick={e => e.stopPropagation()}
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
                onClick={e => e.stopPropagation()}
                to={{
                  pathname: `/listcwidgetconfirmation/${
                    this.props.widgetRecord.widget_id
                  }/black`,
                }}
                target="_blank">
                black
              </Link>
            </div>
          </div>
        </td>
      </tr>
    );
  }
}

export default Record;
