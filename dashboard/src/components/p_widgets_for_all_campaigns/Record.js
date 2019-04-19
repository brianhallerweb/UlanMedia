//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {clicked: false, hovered: false};
  }

  colorizeRow(classification) {
    if (classification === 'white') {
      //green
      return '#eafcea';
    } else if (classification === 'black') {
      //red
      return '#f7d9d9';
    } else if (classification === 'grey') {
      //grey
      return '#ededed';
    } else if (classification === 'not yet') {
      //light grey
      return '#fafafa';
    }
  }

  outlineRow(
    hovered,
    hasMismatchClassificationAndGlobalStatus,
    hasBadAndIncludedCampaigns,
  ) {
    if (
      hasMismatchClassificationAndGlobalStatus ||
      hasBadAndIncludedCampaigns
    ) {
      return 'red';
    } else if (hovered) {
      return 'black';
    } else {
      return 'transparent';
    }
  }

  render() {
    return (
      <tr
        style={{
          backgroundColor: this.colorizeRow(
            this.props.widgetRecord.classification,
          ),
          outlineStyle: 'solid',
          outlineColor: this.outlineRow(
            this.state.hovered,
            this.props.widgetRecord
              .has_mismatch_classification_and_global_status,
            this.props.widgetRecord.has_bad_and_included_campaigns,
          ),
        }}
        className={this.state.clicked && 'clicked'}
        onMouseEnter={e => {
          this.setState({hovered: !this.state.hovered});
        }}
        onMouseLeave={e => {
          this.setState({hovered: !this.state.hovered});
        }}
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
                  pathname: `/campaignsforonepwidget/${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}`,
                }}
                target="_blank">
                campaigns
              </Link>
            </div>
            {this.props.widgetRecord.has_children && (
              <div className="rowLink">
                <Link
                  onClick={e => e.stopPropagation()}
                  to={{
                    pathname: `/cwidgetsforonepwidget/${this.props.widgetRecord.widget_id.match(
                      /^\d*/,
                    )}`,
                  }}
                  target="_blank">
                  c_widgets
                </Link>
              </div>
            )}

            <div className="rowLink">
              <a
                href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_7f6f8173-3293-4891-a078-da864a6da65b/report/custom-variable-1,country-code?dateRange=last-30-days&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=customVariable1&columns=countryName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
                  this.props.widgetRecord.widget_id
                }&limit=100&reportType=table&include=ACTIVE&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc
`}
                target="_blank">
                countries
              </a>
            </div>

            <div className="rowLink">
              <a
                href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_74bf4b44-0272-43f3-92f1-28a82de188cb/report/custom-variable-1,language?dateRange=last-30-days&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=customVariable1&columns=countryName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
                  this.props.widgetRecord.widget_id
                }&limit=100&reportType=table&include=ACTIVE&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc
`}
                target="_blank">
                languages
              </a>
            </div>

            <div className="rowLink">
              <a
                href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_27e1fe2c-3a24-4946-b334-8e7df1b50e2d/report/month,custom-variable-1?dateRange=last-30-days&sortKey=month&sortDirection=desc&page=1&chart=0&columns=month&columns=customVariable1&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
                  this.props.widgetRecord.widget_id
                }&limit=1000&reportType=table&include=ACTIVE&reportDataType=0&tagsGrouping=month&valueFiltersGrouping=month&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`}
                target="_blank">
                months
              </a>
            </div>

            <div className="rowLink">
              <a
                href={`https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_32154ab0-b614-4ac5-b017-6d5a18447bc5/report/day,custom-variable-1?dateRange=last-30-days&sortKey=day&sortDirection=desc&page=1&chart=0&columns=day&columns=customVariable1&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
                  this.props.widgetRecord.widget_id
                }&limit=1000&reportType=table&include=ALL&reportDataType=0&tagsGrouping=day&valueFiltersGrouping=day&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`}
                target="_blank">
                days
              </a>
            </div>

            <div className="rowLink">
              <Link
                onClick={e => e.stopPropagation()}
                to={{
                  pathname: `/excludepwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}`,
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
                  pathname: `/listpwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}/${this.props.widgetRecord.classification}`,
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
        <td>${this.props.widgetRecord.cpc}</td>
        <td>${this.props.widgetRecord.epc}</td>
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
                  pathname: `/listpwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}/white`,
                }}
                target="_blank">
                white
              </Link>
            </div>
            <div className="rowLink">
              <Link
                onClick={e => e.stopPropagation()}
                to={{
                  pathname: `/listpwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}/grey`,
                }}
                target="_blank">
                grey
              </Link>
            </div>
            <div className="rowLink">
              <Link
                onClick={e => e.stopPropagation()}
                to={{
                  pathname: `/listpwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}/black`,
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
