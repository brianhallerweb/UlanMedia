//@format
import React, {Component} from 'react';
import CampaignsByWidgetsDatesDropdown from './CampaignsByWidgetsDatesDropdown';
import CampaignsByWidgetsConditionCheckboxes from './CampaignsByWidgetsConditionCheckboxes';

class CampaignByWidgetsNavBar extends Component {
  constructor(props) {
    super(props);
    this.state = {};
  }

  render() {
    return (
      <div>
        <form
          onSubmit={e => {
            e.preventDefault();
            this.props.submitForm();
          }}>
          <CampaignsByWidgetsDatesDropdown
            selectDateRange={this.props.selectDateRange}
          />
          <p>
            Widget cost greater than
            <input
              type="number"
              name="quantity"
              min="0"
              max="20"
              step="1"
              value={this.props.precondition}
              onChange={e => this.props.selectPrecondition(e.target.value)}
            />
          </p>
          <CampaignsByWidgetsConditionCheckboxes
            toggleCondition={this.props.toggleCondition}
            c1={this.props.c1}
            c2={this.props.c2}
          />
          <input type="submit" value="submit" />
        </form>
      </div>
    );
  }
}

export default CampaignByWidgetsNavBar;
