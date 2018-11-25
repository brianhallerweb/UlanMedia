//@format
import React, {Component} from 'react';
import {Link} from 'react-router-dom';

class Record extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <tr>
        <td>
          {this.props.widgetRecord.widget_id}
          <div>
            <div className="rowLink">
              <Link
                to={{
                  pathname: `/widget/parent/${this.props.widgetRecord.widget_id.match(
                    /^\d*/,
                  )}`,
                }}
                target="_blank">
                parent widget
              </Link>
            </div>

            <div className="rowLink">
              <Link
                to={{
                  pathname: `/widget/child/${
                    this.props.widgetRecord.widget_id
                  }`,
                }}
                target="_blank">
                child widget
              </Link>
            </div>

            <div className="rowLink">
              <a href={`http://ulanmedia.com/mgid/exclude-widgets-form.php?campaignIDs=all&widgetIDs=${this.props.widgetRecord.widget_id.match(/^\d*/,)}`} target="_blank">
                exclude
              </a>
            </div>
          </div>
        </td>
        <td>{this.props.widgetRecord.clicks}</td>
        <td>${this.props.widgetRecord.cost.toFixed(2)}</td>
        <td>${this.props.widgetRecord.revenue}</td>
        <td>${this.props.widgetRecord.profit.toFixed(2)}</td>
        <td>{this.props.widgetRecord.leads}</td>
        <td>${this.props.widgetRecord.lead_cpa.toFixed(2)}</td>
        <td>{this.props.widgetRecord.sales}</td>
        <td>${this.props.widgetRecord.sale_cpa.toFixed(2)}</td>
        <td>
	    {this.props.widgetRecord.global_status}
	    {this.props.widgetRecord.global_status === "not yet listed" ? 
			    <div>
			      <div className="rowLink">
                                <a target="_blank" href={`http://ulanmedia.com/mgid/add-widgets-to-list.php?widgetIDs=${this.props.widgetRecord.widget_id.match(/^\d*/,)}&list=whitelist`}>white</a>
			      </div>
			      <div className="rowLink">
                                <a target="_blank" href={`http://ulanmedia.com/mgid/add-widgets-to-list.php?widgetIDs=${this.props.widgetRecord.widget_id.match(/^\d*/,)}&list=blacklist`}>black</a>
			      </div>
			      <div className="rowLink">
                                <a target="_blank" href={`http://ulanmedia.com/mgid/add-widgets-to-list.php?widgetIDs=${this.props.widgetRecord.widget_id.match(/^\d*/,)}&list=greylist`}>grey</a>
			      </div>
			    </div> 
			    : ""}
	</td>
      </tr>
    );
  }
}

export default Record;
