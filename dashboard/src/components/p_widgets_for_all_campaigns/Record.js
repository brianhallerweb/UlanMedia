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
                  pathname: `/campaignsforonepwidget/${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}/${this.props.widgetRecord.classification}/${
                    this.props.widgetRecord.good_campaigns_count
                  }/${this.props.widgetRecord.bad_campaigns_count}/${
                    this.props.widgetRecord.bad_campaigns_included_count
                  }/${this.props.widgetRecord.wait_campaigns_count}`,
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
        <td>{`${this.props.widgetRecord.classification} (${
          this.props.widgetRecord.good_campaigns_count
        }g/${this.props.widgetRecord.bad_campaigns_count}b/${
          this.props.widgetRecord.bad_campaigns_included_count
        }B/${this.props.widgetRecord.wait_campaigns_count}w)`}</td>
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
                <Link
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
                  to={{
                    pathname: `/listpwidgetconfirmation/${this.props.widgetRecord.widget_id.match(
                      /^\d*/,
                    )}/black`,
                  }}
                  target="_blank">
                  black
                </Link>
              </div>
              <div className="rowLink">
                <span className="fakeLink">wait</span>
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
