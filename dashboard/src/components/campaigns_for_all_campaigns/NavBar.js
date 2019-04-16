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
            c15={this.props.c15}
            c16={this.props.c16}
            c17={this.props.c17}
            c18={this.props.c18}
            c19={this.props.c19}
            c20={this.props.c20}
            c21={this.props.c21}
            c22={this.props.c22}
            c1Value={this.props.c1Value}
            c2Value={this.props.c2Value}
            c3Value={this.props.c3Value}
            c4Value={this.props.c4Value}
            c11Value={this.props.c11Value}
            c12Value={this.props.c12Value}
            c13Value={this.props.c13Value}
            c14Value={this.props.c14Value}
            c15Value={this.props.c15Value}
            c16Value={this.props.c16Value}
            c17Value={this.props.c17Value}
            c18Value={this.props.c18Value}
            c19Value={this.props.c19Value}
            c20Value={this.props.c20Value}
            c21Value={this.props.c21Value}
            c22Value={this.props.c22Value}
          />
          <input type="submit" value="Submit" />
        </form>
      </div>
    );
  }
}

export default NavBar;
