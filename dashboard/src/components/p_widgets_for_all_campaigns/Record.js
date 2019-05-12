//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import InternalLink from '../utilities/InternalLink';
import ExternalLink from '../utilities/ExternalLink';

class Record extends Component {
  constructor(props) {
    super(props);

    this.countriesURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_7f6f8173-3293-4891-a078-da864a6da65b/report/custom-variable-1,country-code?dateRange=last-30-days&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=customVariable1&columns=countryName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
      this.props.widgetRecord.widget_id
    }&limit=100&reportType=table&include=ACTIVE&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc
`;

    this.languagesURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_74bf4b44-0272-43f3-92f1-28a82de188cb/report/custom-variable-1,language?dateRange=last-30-days&sortKey=visits&sortDirection=desc&page=1&chart=0&columns=customVariable1&columns=countryName&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
      this.props.widgetRecord.widget_id
    }&limit=100&reportType=table&include=ACTIVE&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc
`;

    this.ISPURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_2bcf039b-b777-4d24-ad0d-2dd9fa978470/report/custom-variable-1,isp?dateRange=last-30-days&sortKey=profit&sortDirection=asc&page=1&chart=0&columns=customVariable1&columns=isp&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
      this.props.widgetRecord.widget_id
    }&limit=1000&reportType=tree&include=ALL&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`;

    this.deviceOSURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_5a5a89b9-b146-4fb6-9ea4-128f8e675251/report/custom-variable-1,device,os?dateRange=last-30-days&sortKey=profit&sortDirection=asc&page=1&chart=0&columns=customVariable1&columns=isp&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
      this.props.widgetRecord.widget_id
    }&limit=1000&reportType=tree&include=ALL&reportDataType=0&tagsGrouping=custom-variable-1&valueFiltersGrouping=custom-variable-1&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`;

    this.monthsURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_27e1fe2c-3a24-4946-b334-8e7df1b50e2d/report/month,custom-variable-1?dateRange=last-30-days&sortKey=month&sortDirection=desc&page=1&chart=0&columns=month&columns=customVariable1&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
      this.props.widgetRecord.widget_id
    }&limit=1000&reportType=table&include=ACTIVE&reportDataType=0&tagsGrouping=month&valueFiltersGrouping=month&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`;

    this.daysURL = `https://panel.voluum.com/?clientId=7f44bde0-bb64-410b-b72c-6579c9683de0#/7f44bde0-bb64-410b-b72c-6579c9683de0_32154ab0-b614-4ac5-b017-6d5a18447bc5/report/day,custom-variable-1?dateRange=last-30-days&sortKey=day&sortDirection=desc&page=1&chart=0&columns=day&columns=customVariable1&columns=visits&columns=suspiciousVisitsPercentage&columns=conversions&columns=revenue&columns=cost&columns=profit&columns=cpv&columns=cv&columns=roi&columns=epv&filter=${
      this.props.widgetRecord.widget_id
    }&limit=1000&reportType=table&include=ALL&reportDataType=0&tagsGrouping=day&valueFiltersGrouping=day&filter1=traffic-source&filter1Value=37bbd390-ed90-4978-9066-09affa682bcc`;

    this.state = {clicked: false, hovered: false};
  }

  componentDidMount() {
    if (
      this.props.widgetRecord.global_status === 'p_blacklist' ||
      this.props.widgetRecord.global_status === 'c_blacklist' ||
      this.props.widgetRecord.global_status === 'pc_blacklist'
    ) {
      this.setState({clicked: true});
    }
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
            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/campaignsforonepwidget/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}`}
              target={'_blank'}
              label={'campaigns'}
            />

            {this.props.widgetRecord.has_children && (
              <InternalLink
                className={'rowLink'}
                stopPropagation={true}
                to={`/cwidgetsforonepwidget/${this.props.widgetRecord.widget_id.match(
                  /^\d*/,
                )}`}
                target={'_blank'}
                label={'c_widgets'}
              />
            )}

            <ExternalLink
              className={'rowLink'}
              href={this.countriesURL}
              target={'_blank'}
              label={'countries'}
            />

            <ExternalLink
              className={'rowLink'}
              href={this.languagesURL}
              target={'_blank'}
              label={'languages'}
            />

            <ExternalLink
              className={'rowLink'}
              href={this.deviceOSURL}
              target={'_blank'}
              label={'device/os'}
            />

            <ExternalLink
              className={'rowLink'}
              href={this.ISPURL}
              target={'_blank'}
              label={'isp'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/monthsforonepwidgetforallcampaigns/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}`}
              target={'_blank'}
              label={'months'}
            />

            <InternalLink
              className={'rowLink'}
              stopPropagation={true}
              to={`/daysforonepwidgetforallcampaigns/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}`}
              target={'_blank'}
              label={'days'}
            />

            <InternalLink
              className={'rowLink'}
              to={`/excludepwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}`}
              target={'_blank'}
              label={'exclude'}
            />
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
            <InternalLink
              className={'rowLink'}
              to={`/listpwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}/white`}
              target={'_blank'}
              label={'white'}
            />
            <InternalLink
              className={'rowLink'}
              to={`/listpwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}/grey`}
              target={'_blank'}
              label={'grey'}
            />
            <InternalLink
              className={'rowLink'}
              to={`/listpwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                /^\d*/,
              )}/black`}
              target={'_blank'}
              label={'black'}
            />
          </div>
        </td>
      </tr>
    );
  }
}

export default Record;
