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
            c2={this.props.c2}
            c3={this.props.c3}
            c4={this.props.c4}
            c5={this.props.c5}
            c6={this.props.c6}
            c7={this.props.c7}
            c8={this.props.c8}
            c9={this.props.c9}
            c10={this.props.c10}
            c11={this.props.c11}
            c12={this.props.c12}
            c13={this.props.c13}
            c14={this.props.c14}
            c1Value={this.props.c1Value}
            c2Value={this.props.c2Value}
            c9Value={this.props.c9Value}
            c10Value={this.props.c10Value}
            c11Value={this.props.c11Value}
            c12Value={this.props.c12Value}
            c13Value={this.props.c13Value}
            c14Value={this.props.c14Value}
          />
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}

export default NavBar;
