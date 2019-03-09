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
        className={this.state.clicked && 'clicked'}
        onClick={e => {
          this.setState({clicked: !this.state.clicked});
        }}>
        <td>
          {this.props.widgetRecord.widget_id}
          <div>
            <div>
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
                  c widgets
                </Link>
              </div>
            )}

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
