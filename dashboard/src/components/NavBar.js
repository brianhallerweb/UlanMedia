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
          <DatesDropdown selectDateRange={this.props.selectDateRange} />
          <ConditionCheckboxes toggleCondition={this.props.toggleCondition} />
          <input
            type="submit"
            value="Submit"
            disabled={!this.props.isConditionSelected()}
          />
        </form>
      </div>
    );
  }
}

export default NavBar;
