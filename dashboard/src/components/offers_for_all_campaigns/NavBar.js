//@format
import React, {Component} from 'react';
import DatesDropdown from './DatesDropdown';
import ConditionCheckboxes from './ConditionCheckboxes';

class NavBar extends Component {
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
          <DatesDropdown
            selectDateRange={this.props.selectDateRange}
            dateRange={this.props.dateRange}
          />
          <ConditionCheckboxes
            toggleCondition={this.props.toggleCondition}
            setConditionValue={this.props.setConditionValue}
            c1={this.props.c1}
            c1Value={this.props.c1Value}
            c2={this.props.c2}
            c2Value={this.props.c2Value}
            c3={this.props.c3}
            c3Value={this.props.c3Value}
            c4={this.props.c4}
            c4Value={this.props.c4Value}
            c5={this.props.c5}
          />
          <div style={{marginBottom: 10}}>
            Remember the clicks, cost, CPC, EPC, CPA and CVR are going to be
            just estimates and not very accurate, because they're based on
            Voluum's total received clicks, not on MGID's legit billable clicks.
          </div>

          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}

export default NavBar;
