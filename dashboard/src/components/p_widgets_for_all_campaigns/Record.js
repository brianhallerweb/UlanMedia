//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {clicked: false};
  }

  addTrainingData(decision) {
    fetch('/api/pWidgetsForAllCampaignsTrainingData', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'x-auth': localStorage.getItem('token'),
      },
      body: JSON.stringify({
        widgetID: this.props.widgetRecord.widget_id,
        clicks: this.props.widgetRecord.clicks,
        cost: this.props.widgetRecord.cost,
        revenue: this.props.widgetRecord.revenue,
        profit: this.props.widgetRecord.profit,
        leads: this.props.widgetRecord.leads,
        leadCPA: this.props.widgetRecord.lead_cpa,
        leadCVR: this.props.widgetRecord.lead_cvr,
        sales: this.props.widgetRecord.sales,
        saleCPA: this.props.widgetRecord.sale_cpa,
        globalStatusDecision: decision,
      }),
    }).then(res => {
      if (!res.ok) {
        throw Error(res.statusText);
      }
    });
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
                  to={{
                    pathname: `/cwidgetsforonepwidget/${this.props.widgetRecord.widget_id.match(
                      /^\d*/,
                    )}`,
                  }}
                  target="_blank">
                  c widgets
                </Link>
              </div>
            )}

            <div className="rowLink">
              <a
                href={`http://ulanmedia.com/mgid/exclude-widgets-form.php?campaignIDs=all&widgetIDs=${this.props.widgetRecord.widget_id.match(
                  /^\d*/,
                )}`}
                target="_blank">
                exclude
              </a>
            </div>
          </div>
        </td>
        <td>{this.props.widgetRecord.clicks}</td>
        <td>${this.props.widgetRecord.cost}</td>
        <td>${this.props.widgetRecord.revenue}</td>
        <td>${this.props.widgetRecord.profit}</td>
        <td>{this.props.widgetRecord.leads}</td>
        <td>${this.props.widgetRecord.lead_cpa}</td>
        <td>{this.props.widgetRecord.lead_cvr}%</td>
        <td>{this.props.widgetRecord.sales}</td>
        <td>${this.props.widgetRecord.sale_cpa}</td>
        <td>
          {this.props.widgetRecord.global_status}
          {this.props.widgetRecord.global_status === 'not yet listed' ? (
            <div onClick={() => this.setState({clicked: true})}>
              <div className="rowLink">
                <a
                  onClick={() => this.addTrainingData('white')}
                  target="_blank"
                  href={`http://ulanmedia.com/mgid/add-widgets-to-list-form.php?widgetIDs=${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}&list=whitelist`}>
                  white
                </a>
              </div>
              <div className="rowLink">
                <a
                  onClick={() => this.addTrainingData('grey')}
                  target="_blank"
                  href={`http://ulanmedia.com/mgid/add-widgets-to-list-form.php?widgetIDs=${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}&list=greylist`}>
                  grey
                </a>
              </div>
              <div className="rowLink">
                <a
                  onClick={() => this.addTrainingData('black')}
                  target="_blank"
                  href={`http://ulanmedia.com/mgid/add-widgets-to-list-form.php?widgetIDs=${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}&list=blacklist`}>
                  black
                </a>
              </div>
            </div>
          ) : (
            ''
          )}
        </td>
      </tr>
    );
  }
}

export default Record;
